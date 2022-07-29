from django.urls import path
from .views import List_rider, Detail_rider

urlpatterns = [
    path('', List_rider.as_view()),
    path('<int:pk>/', Detail_rider.as_view())
]
