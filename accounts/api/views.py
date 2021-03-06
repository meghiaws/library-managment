from django.contrib.auth import get_user_model

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser

from ..models import Librarian, Member
from .permissions import IsAdminOrLibrarian
from .serializers import (
    MemberSerializer,
    CreateMemberSerializer,
    LibrarianSerializer,
    CreateLibrarianSerializer,
)


User = get_user_model()


class MemberViewset(ModelViewSet):
    queryset = Member.objects.select_related("user").all()
    permission_classes = [IsAdminOrLibrarian]

    def get_serializer_class(self):
        if self.action == "create":
            return CreateMemberSerializer
        return MemberSerializer

    def perform_destroy(self, instance):
        instance.user.delete()
        return super().perform_destroy(instance)


class LibrarianViewset(ModelViewSet):
    queryset = Librarian.objects.select_related("user").all()
    permission_classes = [IsAdminUser]

    def get_serializer_class(self):
        if self.action == "create":
            return CreateLibrarianSerializer
        return LibrarianSerializer

    def perform_destroy(self, instance):
        instance.user.delete()
        return super().perform_destroy(instance)
