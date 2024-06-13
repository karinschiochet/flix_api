from django.urls import path
from . import views

urlpatterns = [
    path('reviews/', views.ReviewCreateListView.as_view(),
         name='review-create-view'),
    path('reviews/<int:pk>/', views.ReviewRetrieveUpdateDetroyView.as_view(),
         name='review-detail-view'),
]
