from django.urls import path
from item.views import BuyView

urlpatterns = [
    path('buy/<int:id>/', BuyView.as_view(), name='buy'),
]
