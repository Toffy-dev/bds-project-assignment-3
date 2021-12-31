from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from .forms import Payment
from main.models import Customer
from django.db.models import F
import decimal
from django.db import transaction


def process_payment(request):
	if request.method == 'POST':
		form = Payment(request.POST)

		if form.is_valid():
			x = form.cleaned_data['payor']
			y = form.cleaned_data['payee']
			z = decimal.Decimal(form.cleaned_data['amount'])

			with transaction.atomic():
				payor = Customer.objects.select_for_update().get(username=x)
				payor.balance -= z
				payor.save()
				payee = Customer.objects.select_for_update().get(username=y)
				payee.balance += z
				payee.save()

		# Customer.objects.filter(name=x).update(balance=F('balance') - z)
		# customer.objects.filter(name=y).update(balance=F('balance') + z)
				return HttpResponseRedirect('/')
	else:
		form = Payment()
	return render(request, 'transaction/payment.html', {'form': form})