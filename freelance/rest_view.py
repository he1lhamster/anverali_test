from django.db import transaction
from rest_framework import viewsets
from .models import CustomUser, Customer, Performer, OrderCategory, Status, Order
from .serializers import CustomUserSerializer, CustomerSerializer, PerformerSerializer, OrderSerializer


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class PerformerViewSet(viewsets.ModelViewSet):
    queryset = Performer.objects.all()
    serializer_class = PerformerSerializer


class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = CustomerSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_update(self, serializer):
        serializer.save()
        transaction.commit()

    def perform_create(self, serializer):
        serializer.save()
        transaction.commit()

