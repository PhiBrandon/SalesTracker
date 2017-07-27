from django.shortcuts import render
from calc.forms import calculateForm
from calc.scripts.sales import *


# Create your views here.
def home(request):
	

	if request.method == 'POST':
		form = calculateForm(request.POST)
		if form.is_valid():
			comission = form.cleaned_data['comission_goal']
			income = form.cleaned_data['income_goal']
			cRate = form.cleaned_data['close_rate']
			tCalls = form.cleaned_data['total_calls']
			value = sales_goal(int(income),int(comission))
			rate = calculate_CR(int(cRate),int(tCalls))
			total = value['total_sales']
			crate = rate['close_rate']
			final_string = interaction_goal(total,crate)
		return render(request, 'calc/home.html',{'form':form, 'goal':final_string, 'sales_string':value['sale_string'],'rate_string':rate['rate_string']})
	else:
		form = calculateForm()
		return render(request, 'calc/home.html',{'form':form})