from django.views import View
from django.shortcuts import render
from .models import IdentityDocument

class IndexView(View):
    template_name = 'identity_document/index.html'
    
    def get(self, request):
        items = IdentityDocument.objects.all()
        return render(request, self.template_name, {'items': items})
