from django.views import View
from django.shortcuts import render
from .models import Message

class IndexView(View):
    template_name = 'message/index.html'
    
    def get(self, request):
        items = Message.objects.all()
        return render(request, self.template_name, {'items': items})
