from django.urls import path
from .views import Search_Handler

urlpatterns = [
    path('<str:name>/', Search_Handler.as_view(), name = "search"),
]