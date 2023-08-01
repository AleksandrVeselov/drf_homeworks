from rest_framework import viewsets, generics

from users.models import User
from users.serializiers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):

    serializer_class = UserSerializer
    queryset = User.objects.all()