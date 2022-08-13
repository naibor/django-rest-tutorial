from django.urls import path, include
from snippets import views

urlpatterns = [
    path('', include('snippets.urls')),
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail),
]

