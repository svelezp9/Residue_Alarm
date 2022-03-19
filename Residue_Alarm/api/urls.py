from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('profiles',views.UserProfileViewSet)

urlpatterns = [
    path('/description',views.descriptionAPI().as_view()),
    path('login/',views.UserLoginApiView.as_view()),
    path('',include(router.urls))
]