from django.shortcuts import render
from django.views import View
from .models import ListingApproval

class IndexView(View):
    template_name = 'approvals/index.html'
    
    def get(self, request):
        items = ListingApproval.objects.all()
        return render(request, self.template_name, {'items': items})