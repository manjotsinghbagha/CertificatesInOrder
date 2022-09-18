from django import forms
from django.forms import inlineformset_factory

from .models import Quiz, QuesModel


class QueizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ('name', 'desc','time_in_sec','certificteImg')


class QuesModelForm(forms.ModelForm):
    class Meta:
        model = QuesModel
        fields = ('quiz', 'question','op1','op2','op3','op4','ans')


QuesModelInlineFormset = inlineformset_factory(
    Quiz,
    QuesModel,
    form=QuesModelForm,
    extra=1,
    # max_num=5,
    # fk_name=None,
    # fields=None, exclude=None, can_order=False,
    can_delete=True, max_num=None,
    #  formfield_callback=None,
    # widgets=None, validate_max=False, localized_fields=None,
    # labels=None, help_texts=None, error_messages=None,
    # min_num=None, validate_min=False, field_classes=None
)