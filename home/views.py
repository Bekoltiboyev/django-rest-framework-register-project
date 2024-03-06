from .serializers import UsersSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.contrib.auth.models import User


class UserView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer


class UserRetrieveView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    
    


# requirements file

# file yaratish comandasi

# pip freeze > requirments.txt


# pip install requirments.txt