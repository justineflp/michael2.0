from django.views import View
from django.shortcuts import render
from .models import CouponUsage

class IndexView(View):
    template_name = 'coupon_usage/index.html'
    
    def get(self, request):
        items = CouponUsage.objects.all()
        return render(request, self.template_name, {'items': items})
