from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import List
from .serializers import ListSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsListOwnerOrAdmin
from rest_framework.exceptions import APIException
from rest_framework.views import status


class ListView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ListSerializer

    def get_queryset(self):
        return List.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        listFound = List.objects.filter(
            user=self.request.user,
            year=self.request.data["year"],
            month=self.request.data["month"],
        )
        if listFound:
            raise ListDuplicationError()

        serializer.save(user=self.request.user)


class ListDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsListOwnerOrAdmin]
    serializer_class = ListSerializer
    queryset = List.objects.all()

    lookup_url_kwarg = "list_id"


class ListDuplicationError(APIException):
    status_code = status.HTTP_409_CONFLICT
    default_detail = "List with this month and year already exists"
