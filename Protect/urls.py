from django.urls import path

from . import views

urlpatterns = [
    path('ai/public', views.public),
    path('ai/private', views.private),
    path('ai/private-scoped', views.private_scoped),
]
