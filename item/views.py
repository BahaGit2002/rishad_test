from django.views.generic.base import TemplateView


class BuyView(TemplateView):
    template_name = 'buy.html'
