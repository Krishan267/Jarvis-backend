from .views import LoginPage, Dashboard, TradeData, Strategies, LineData, BarData
from django.urls import path


urlpatterns = [
    path('login/', LoginPage.as_view(), name='login'),
    path('dashboard/', Dashboard.as_view(), name='user-dashboard-page'),
    path('dashboard/trade_data', TradeData.as_view(), name='trade-data'),
    path('dashboard/strategies', Strategies.as_view(), name='strategies'),
    path('dashboard/portfolio', LineData.as_view(), name='portfolio'),
    path('dashboard/bar_data', BarData.as_view(), name='bar_data'),
]