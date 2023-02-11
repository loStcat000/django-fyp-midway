from django.urls import path
from .views import HomePageView
from pages import views

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
     path('userdata/',views.User_Data, name="userdata"),
]
