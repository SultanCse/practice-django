from django.shortcuts import render, HttpResponse

# Create your views here.

def home (request):
	name = 'sultan'
	lists=[1, 2, 3, 4]
	args={'myName': name, 'lists': lists}
	#return render(request,'accounts/login.html', args)
	return render(request,'accounts/home.html', args)
