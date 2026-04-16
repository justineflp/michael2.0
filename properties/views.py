from django.shortcuts import render
from django.views import View
from .models import Listing, Booking

class IndexView(View):
    template_name = 'properties/index.html'
    
    def get(self, request):
        items = Listing.objects.all()
        bookings = Booking.objects.all()
        return render(request, self.template_name, {'items': items, 'bookings': bookings})
