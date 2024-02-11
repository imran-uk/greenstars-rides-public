from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views import generic
from django.shortcuts import get_object_or_404

from .models import Ride

# TODO
# come back to this method later...
# class IndexView(generic.ListView):
#     template_name = 'ride_manager/index.html'
#     context_object_name = 'rides_list'

#     def get_queryset(self):
#         return Ride.objects.all()[:5]

# class RideView(generic.DetailView):
#     model = Ride
#     template_name = 'ride_manager/show.html'


def all_rides(request):
    rides_list = Ride.objects.all()[:5]
    context = {
        "page_title": "All Rides",
        "meta_url": request.build_absolute_uri(),
        "meta_image": request.build_absolute_uri("/static/img/logo.jpg"),
        "rides_list": rides_list,
    }

    return render(request, "ride_manager/index.html", context)

def show_ride(request, ride_id):
    try:
        ride = Ride.objects.get(pk=ride_id)
    except Ride.DoesNotExist:
        raise Http404("Ride does not exist")

    # shortcut for above but how to pass message?
    # ride = get_object_or_404(Ride, pk=ride_id)

    context = {
        "page_title": ride.name,
        "meta_url": request.build_absolute_uri(),
        "meta_image": request.build_absolute_uri("/greenstars/static/img/logo.jpg"),
        "ride" : ride
    }

    return render(request, "ride_manager/show.html", context)
