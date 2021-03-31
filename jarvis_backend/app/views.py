from django.shortcuts import render
from rest_framework import permissions
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from .Exceldata import ReadExcel
from django.conf import settings
# Create your views here.

test_crdentials='admin@gmail.com'
password="admin"

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
    login_template = 'index.html'

    def get(self, request):
        value = 'authorized'
        return render(request,self.template_name,{'auth': True})

    def post(self, request, format=None):
        auth = False
        if request.data['email']==test_crdentials and request.data['password']==password:
            auth = True
            print('authentication',auth)
            return render(request, self.template_name,{'auth':auth})
        
        print('authentication',auth)
        return render(request, self.login_template, {'auth':auth, 'error':'Incorrect Email or Password'})

class PnlReport(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        return Response({'test':123})


class TradeData(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        excel_instance = ReadExcel(settings.EXCEL_PATH)
        trade_data = excel_instance.get_trade_data()
        return Response({'data':trade_data})

class Strategies(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        """
        some dummy strategies
        """
        data=[
            {
            'description':'Day Trading','status':'Start'
            },
            {
            'description':'Position Trading','status':'Stop'
            }
            ]
        return Response({'data':data})

class LineData(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        excel_instance = ReadExcel(settings.EXCEL_PATH)
        portfolio_data = excel_instance.get_line_data()
        return Response(portfolio_data)


class BarData(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request):
        excel_instance = ReadExcel(settings.EXCEL_PATH)
        bar_data = excel_instance.get_bar_data()
        seq = [x['entry_qty'] for x in bar_data]
        print(round(max(seq)))
        print(min(seq))
        data={'max_val':max(seq), 'bar_data':bar_data}
        return Response(data)