from django.shortcuts import render, redirect
from rest_framework import permissions
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from .Exceldata import ReadExcel
from django.conf import settings
from app.ui_methods import authenticate,get_net_worth,get_pnl,get_open_positions,get_trades_history,get_strategy_list_status
from django.http import HttpResponse

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
        if authenticate(request.data['email'],request.data['password']):
            auth = True
            print('authentication',auth)
            net_worth =get_net_worth(request.data['email'])
            print(net_worth,"jkl")
            pnl = get_pnl(request.data['email'])
            print(pnl)
            request.session['username'] = 'myvalue'

            return render(request, self.template_name,{'auth':auth, 'net_worth':round(net_worth),"pnl":pnl,"username":request.data['email']})
        
        print('authentication',auth)
        return render(request, self.login_template, {'auth':auth, 'error':'Incorrect Email or Password'})

class PnlReport(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        return Response({'test':123})


class TradeData(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request,username):       
        trade_data = get_trades_history(username)
        return Response({'data':trade_data})

class TradeDataDownload(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request,username):       
        trade_data = get_trades_history(username)
        
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=trade.csv'

        trade_data.to_csv(path_or_buf=response,sep=';',float_format='%.2f',index=False,decimal=",")
        return response

class OpenPositions(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request,username):
        data = get_open_positions(username)
        print(data)
        return Response({'data':data})

class OpenPositionsDownload(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request,username):
        data = get_open_positions(username)
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=pos.csv'

        data.to_csv(path_or_buf=response,sep=';',float_format='%.2f',index=False,decimal=",")
        return response


class Strategies(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request,username):
        """
        some dummy strategies
        """
        # data=[
        #     {
        #     'description':'Day Trading','status':'Start'
        #     },
        #     {
        #     'description':'Position Trading','status':'Stop'
        #     }
        #     ]
        data =get_strategy_list_status(username)
        print(data)
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
        # print(round(max(seq)))
        # print(min(seq))
        data={'max_val':max(seq), 'bar_data':bar_data}
        return Response(data)

class Logout(APIView):
    def get(self, request):
        return redirect('/login')
