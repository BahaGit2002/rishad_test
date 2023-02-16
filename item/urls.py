from django.urls import path
from item.views import BuyView, ItemView

urlpatterns = [
    path('buy/<int:id>/', BuyView.as_view(), name='buy'),
    path('item/<int:id>/', ItemView.as_view(), name='item'),
]
