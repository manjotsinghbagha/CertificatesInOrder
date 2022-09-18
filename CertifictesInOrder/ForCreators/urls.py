from django.urls import path

from .views import QuizListView, QuizCreateView

urlpatterns = [
    # ...
    path('quiz', QuizListView.as_view(), name="Quiz_list"),
    # path('quiz', QuizListView.as_view(), name="Quiz_list"),
    path('quiz/create', QuizCreateView.as_view(), name="Quiz_form"),
    # ...
]