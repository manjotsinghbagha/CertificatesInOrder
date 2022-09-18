from django.shortcuts import render

# Create your views here.
from django.forms import modelformset_factory
from django.shortcuts import render, get_object_or_404
from django.views.generic import UpdateView, ListView, CreateView
from django.shortcuts import redirect
from django.urls import reverse

from .models import Quiz
from .forms import QueizForm, QuesModelInlineFormset

class QuizCreateView(CreateView):
    model = Quiz
    template_name = ".html"


class QuizListView(ListView):
    model = Quiz
    template_name = ".html"


class QuizCreateView(CreateView):
    form_class = QueizForm
    template_name = 'product/product_form.html'

    def get_context_data(self, **kwargs):
        context = super(QuizCreateView, self).get_context_data(**kwargs)

        context['ques_model_formset'] = QuesModelInlineFormset()
        return context

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        ques_model_formset = QuesModelInlineFormset(self.request.POST)
        if form.is_valid() and ques_model_formset.is_valid():
            return self.form_valid(form, ques_model_formset)
        else:
            return self.form_invalid(form, ques_model_formset)

    def form_valid(self, form, ques_model_formset):
        self.object = form.save(commit=False)
        self.object.save()
        # saving ProductMeta Instances
        product_metas = ques_model_formset.save(commit=False)
        for meta in product_metas:
            meta.product = self.object
            meta.save()
        return redirect(reverse("product:product_list"))

    def form_invalid(self, form, ques_model_formset):
        return self.render_to_response(
            self.get_context_data(form=form,
                                  ques_model_formset=ques_model_formset
                                  )
        )