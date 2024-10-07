from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Q7Cly2NvNdv2IMkgkY5lUOWlIE4bkiUs4QG2wEBiXuSqeMXL2tmBhHFkndWQ1NV0g9JwMY9fa6KHQfzku5PBZF000vTJtuSBZ',
        'client_secret': 'test client secret',
        }

    return render(request, template, context)