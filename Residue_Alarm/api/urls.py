from django.urls import path
from . import views


urlpatterns = [
    path('',views.descriptionAPI().as_view()),
]