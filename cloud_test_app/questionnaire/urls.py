from django.urls import path
from .models import FilledQuestionnaire
from questionnaire import views

urlpatterns = [
    path('', views.index, name="index"),
    path('questionnaire.html', views.questionnaire, name="questionnaire"),
    path('results.html', views.results, name="results")
]
