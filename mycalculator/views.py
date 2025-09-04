from django.shortcuts import render

# Create your views here.


def calculator_view(request):
		results= None
		error =None	
		if request.method == 'POST':
			try:
				num1 = float(request.POST.get('num1'))
				num2= float(request.POST.get('num2'))
				operation = request.POST .get('operation')

				if operation  == "add":
					results	= num1	+ num2
				elif operation	== "subraction":
					results = num2 - num1
				elif operation	== 'division':
					results	= num2/num1
				elif operation	=='multiply':
					results = num1 * num2
				else:
					error = 'invalid error'
			except ValueError:
				error = 'wrong value'
			except ZeroDivisionError:
				error = "Cant devide by zero"
		return render(request,'mycalculator/index.html',{ "results"	: results	, "error ": error	 })
