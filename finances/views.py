from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Finance
from .serializers import FinanceSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsFinanceOwnerOrAdmin
from django.shortcuts import get_object_or_404


class FinanceView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsFinanceOwnerOrAdmin]
    serializer_class = FinanceSerializer

    lookup_url_kwarg = "list_id"

    def get_queryset(self):
        list_id = self.kwargs["list_id"]
        return Finance.objects.filter(list_id=list_id)

    def perform_create(self, serializer):
        list_id = self.kwargs["list_id"]
        category_id = self.request.data.get("category_id")
        serializer.save(list_id=list_id, category_id=category_id)


class FinanceDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsFinanceOwnerOrAdmin]
    serializer_class = FinanceSerializer
    queryset = Finance.objects.all()

    lookup_url_kwarg = "finance_id"

    def get_queryset(self):
        list_id = self.kwargs["list_id"]
        return Finance.objects.filter(list_id=list_id)
