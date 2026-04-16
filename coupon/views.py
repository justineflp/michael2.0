from django.views import View
from django.shortcuts import render
from .models import Coupon

class IndexView(View):
    template_name = 'coupon/index.html'
    
    def get(self, request):
        items = Coupon.objects.all()
        return render(request, self.template_name, {'items': items})
