from django.urls import path

from . import views

urlpatterns = [
    path('events/', views.EventOrderListCreate.as_view(), name='event-order-list-create'),
    path('events/<int:pk>/', views.EventOrderRetrieveUpdateDestroy.as_view(), name='update'),
]
