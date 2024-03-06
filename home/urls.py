from django.urls import path
from .views import UserView, UserRetrieveView



urlpatterns = [
    path('', UserView.as_view(), name='users'),
    path('<int:pk>/', UserRetrieveView.as_view(), name='user-pk')
]