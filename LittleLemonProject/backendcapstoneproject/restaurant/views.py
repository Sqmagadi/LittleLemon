from django.http import HttpResponse
from django.shortcuts import render
from requests import Response
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet

from .serializers import MenuSerializer, BookingSerializer
from .models import Menu, Booking
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


# Create your views here.
def index(request):
    return render(request, 'index.html', {})


def about(request):
    return render(request, 'about.html', {})


@api_view()
@permission_classes([IsAuthenticated])
def msg(request):
    return Response({'message': 'The view is protected'})


class MenuItemView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(RetrieveDestroyAPIView, DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
