from django.urls import path
from . import views
urlpatterns = [
    path('add/<quiz_id>/', views.index, name='index'),
    path('list/',views.QuizListView.as_view() , name='list quiz'),
    path('createquiz/',views.addQuiz , name='create quiz'),
]
