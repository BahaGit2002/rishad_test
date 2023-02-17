from django.urls import path
from item.views import BuyView, ItemView, OrderView, OrderBuyView

urlpatterns = [
    path('buy/<int:id>/', BuyView.as_view(), name='buy'),
    path('item/<int:id>/', ItemView.as_view(), name='item'),
    path('order/<int:id>/', OrderBuyView.as_view(), name='order'),
    path('order_detail/<int:id>/', OrderView.as_view(), name='order_detail')
]
