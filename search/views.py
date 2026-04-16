from django.shortcuts import render
from django.views import View
from .models import SearchLog

class IndexView(View):
    template_name = 'search/index.html'
    
    def get(self, request):
        items = SearchLog.objects.all()
        return render(request, self.template_name, {'items': items})