from django.views import View
from django.shortcuts import render
from .models import ReportTicket

class IndexView(View):
    template_name = 'report_ticket/index.html'
    
    def get(self, request):
        items = ReportTicket.objects.all()
        return render(request, self.template_name, {'items': items})
