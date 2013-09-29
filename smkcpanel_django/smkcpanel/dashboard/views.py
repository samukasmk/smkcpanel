# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect

def Home(request):
	#return HttpResponse('Aloha!')

	return render(request, 'dashboard/aloha.html')


def SayMyName(request, called_name = None):

	if called_name != None:

		return render(request, 'dashboard/content_aloha.html', { 'name': called_name, 'gender': 'male', 'BASE_URL': request.get_host() })

	else:

		return redirect('/server/say_my_name/Heisenberg')

