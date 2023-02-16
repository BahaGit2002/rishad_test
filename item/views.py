import stripe
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views import View
from django.http.response import JsonResponse

from RishadTEst import settings
from item.models import Item
from django.shortcuts import get_object_or_404


class BuyView(View):
    def get(self, request, *args, **kwargs):
        domain_url = 'http://127.0.0.1:8000/'
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            checkout_session = stripe.checkout.Session.create(
                success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'cancelled/',
                payment_method_types=['card'],
                mode='payment',
                line_items=[
                    {
                        'quantity': 1,
                        'price_data': {
                        'currency': "usd",
                        'unit_amount': 100,
                        'product_data': {
                              'name': 'T-shird',
                              'description': 'sfsdf',
                                }
                        },
                    }
                    ]
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})


class ItemView(TemplateView):
    template_name = 'buy.html'

    def get_context_data(self, **kwargs):
        context = super(ItemView, self).get_context_data(**kwargs)
        context['item'] = get_object_or_404(Item, id=kwargs['id'])
        return context




