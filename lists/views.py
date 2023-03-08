from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import List
from .serializers import ListSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsListOwnerOrAdmin


class ListView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ListSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return List.objects.all()

        return List.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ListDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsListOwnerOrAdmin]
    serializer_class = ListSerializer
    queryset = List.objects.all()

    lookup_url_kwarg = "list_id"
