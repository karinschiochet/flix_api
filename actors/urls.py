from django.urls import path
from . import views

urlpatterns = [
    path('actors/', views.ActorCreateListView.as_view(),
         name='actor-create-view'),
    path('actors/<int:pk>/', views.ActorRetrieveUpdateDetroyView.as_view(),
         name='actor-detail-view'),
]
