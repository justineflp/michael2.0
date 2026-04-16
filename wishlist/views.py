from django.shortcuts import render
from django.views import View
from .models import Wishlist

class IndexView(View):
    template_name = 'wishlist/index.html'
    
    def get(self, request):
        items = Wishlist.objects.all()
        return render(request, self.template_name, {'items': items})