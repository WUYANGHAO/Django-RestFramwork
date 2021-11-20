from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Sitesource import views

router = DefaultRouter()
router.register('sitesources',views.SitesourceViewSet)
urlpatterns = [
    path('',include(router.urls))
]
