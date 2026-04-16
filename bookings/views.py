from django.views import View
from django.shortcuts import render
from .models import Booking

class IndexView(View):
    template_name = 'bookings/index.html'
    
    def get(self, request):
        items = Booking.objects.all()
        return render(request, self.template_name, {'items': items})
