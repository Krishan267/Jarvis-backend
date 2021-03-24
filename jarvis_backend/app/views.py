from django.shortcuts import render
from rest_framework import permissions
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

class LoginPage(APIView):
    permission_classes = (permissions.AllowAny,)
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index.html'

    def get(self, request):
        print('here')
        value = 'authorized'
        return render(request,self.template_name,{'access_grant': value})

class Dashboard(APIView):
    permission_classes = (permissions.AllowAny,)
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'jarvis-dashboard.html'

    def post(self, request, format=None):
        print(request.data)
        return render(request,self.template_name,{})