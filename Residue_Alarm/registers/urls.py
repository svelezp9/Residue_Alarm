from django.urls import path,include
from rest_framework.routers import DefaultRouter
from registers import views
router = DefaultRouter()
router.register('residue',views.ResidueViewSet)

app_name = 'registers'

urlpatterns = [
    path('',include(router.urls))
]

