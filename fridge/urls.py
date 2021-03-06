from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

from rest_framework import routers

from food import views


router = routers.DefaultRouter()
router.register(r'food', views.FoodViewSet)
router.register(r'recipes', views.RecipeViewSet)

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^api-auth/', 
        include('rest_framework.urls', namespace='rest_framework')
    ),

    # Django admin
    url(r'^admin/', include(admin.site.urls)),
)

