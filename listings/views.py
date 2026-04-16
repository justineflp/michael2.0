from django.shortcuts import render
from django.views import View
from .models import Listing

class IndexView(View):
    template_name = 'listings/index.html'
    
    def get(self, request):
        items = Listing.objects.all()
        return render(request, self.template_name, {'items': items})
