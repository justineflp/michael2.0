from django.views import View
from django.shortcuts import render
from .models import Review

class IndexView(View):
    template_name = 'reviews/index.html'
    
    def get(self, request):
        items = Review.objects.all()
        return render(request, self.template_name, {'items': items})
