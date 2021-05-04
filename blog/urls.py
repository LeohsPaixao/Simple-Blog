from django.urls import path
from . import views

app_name = "blog"  # Referencia as url dessa view

urlpatterns = [
    # Conectando a url com a PostListView, sem passar argumentos
    path("", views.PostListView.as_view(), name="list"),
    path("<slug:slug>/", views.PostDetailView.as_view(), name="detail")
]
