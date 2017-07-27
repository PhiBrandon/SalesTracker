def calculate_CR(closed, total):
	close_rate = closed / total
	rate_string = "If you close {} out of {}, your close rate is {} %".format(closed,total,close_rate)
	#print(rate_string)
	pack = {'close_rate':close_rate,'rate_string':rate_string}
	return pack
#Enter the income you wish to make per year and the comission that you make from your product
import math

def sales_goal(income, comission):
	total_sales = income / comission
	sales_string = "If you want to make {} per year @ ${} per unit, you need to sell {} units.".format(income,comission,int(total_sales))
	#print(sales_string)
	pack = {'sale_string':sales_string, 'total_sales':int(total_sales)}
	return pack

def interaction_goal(total_sales, close_rate):
	total_talks = total_sales / close_rate
	percent = close_rate * 100
	per_month = int(math.ceil(total_talks)/12)
	per_week = int(math.ceil(per_month)/4)
	per_day = int(math.ceil(per_week)/5)
	talks_string = """In order to reach your goal of {} with a {} percent close rate you need to talk to {} people per year, 
	{} per month, {} per week and {} per day ( 5 days a week)""".format(total_sales,percent,total_talks,per_month,per_week,per_day)
	#print(talks_string)
	return talks_string


# total1 = 10
# close1 = int(input("How many people can you close out of every 10 you speak to?\n"))
# close_rate_final = calculate_CR(close1,total1)
# #print(close_rate_final)

# goal = int(input("What is your yearly income goal with this position? (No commas in number)\n"))
# commin = int(input("What is the amount you make in comissions?\n"))
# total_sales_final = sales_goal(goal,commin)
# print(int(total_sales_final))
# interaction_goal(total_sales_final,close_rate_final)

