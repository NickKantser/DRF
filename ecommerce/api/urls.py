from django.urls import path
from . import views

urlpatterns = [
    path('import/', views.StoreViewSet.as_view({'post': 'create'})),
    path('detail/<str:model>/', views.StoreViewSet.as_view({'get': 'list'})),
    path('detail/<str:model>/<int:pk>/', views.StoreViewSet.as_view({'get': 'retrieve'})),
]
