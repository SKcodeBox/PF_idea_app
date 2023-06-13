from django.urls import path
from AI_app.views import index

app_name = 'AI_app'
urlpatterns = [
    path('', index, name='index'),
]