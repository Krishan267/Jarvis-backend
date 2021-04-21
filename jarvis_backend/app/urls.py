from .views import LoginPage, Dashboard, TradeData, Strategies, LineData, BarData,OpenPositions,Logout
from django.urls import path


urlpatterns = [
    path('login/', LoginPage.as_view(), name='login'),
    path('dashboard/', Dashboard.as_view(), name='user-dashboard-page'),
    path('dashboard/trade_data/<str:username>', TradeData.as_view(), name='trade-data'),
    path('dashboard/strategies', Strategies.as_view(), name='strategies'),
    path('dashboard/portfolio', LineData.as_view(), name='portfolio'),
    path('dashboard/bar_data', BarData.as_view(), name='bar_data'),
    path('dashboard/open_positions',OpenPositions.as_view(), name='open_positions'),
    path('dashboard/logout',Logout.as_view(), name='logout'),
]