from django.urls import path

from . import views

app_name = "ride_manager"
urlpatterns = [
    # /rides
    # path("", views.IndexView.as_view(), name="all_rides"),
    path("", views.all_rides, name="all_rides"),
    
    # /rides/show/<id>
    # path("show/<int:pk>", views.RideView.as_view(), name="show_ride"),
    path("show/<int:ride_id>", views.show_ride, name="show_ride"),
]