from django.contrib import admin
from django.urls import path
from ideas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_ideas, name='main_ideas')
]
