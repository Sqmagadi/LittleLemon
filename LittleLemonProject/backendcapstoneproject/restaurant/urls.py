from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("menu/", views.MenuItemView.as_view(), name="menu"),
    path("menu/<int:pk>", views.SingleMenuItemView.as_view()),
    path("message/", views.msg),
    path("bookings/", views.BookingViewSet.as_view(
        {
            'get': 'list',
            'post': 'create',
            'delete': 'destroy'
        }
    ))
]
