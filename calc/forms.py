from django import forms

class calculateForm(forms.Form):
	close_rate = forms.CharField(label='Close Rate')
	total_calls = forms.CharField(label="Total Calls")
	comission_goal = forms.CharField(label='Sales Goal')
	income_goal = forms.CharField(label='Income Goal')
