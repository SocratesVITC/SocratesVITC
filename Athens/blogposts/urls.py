from django.urls import path
from .views import markdown_view, home_view

urlpatterns = [
	path('', home_view, name='home_view'),
	path('markdown/<int:pk>/', markdown_view, name='markdown_view'),
]