from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.
def index(request):
	context = {
		'judul':'My Django App',
		'kontributor' : 'Mukhlis',
	}
	return render(request,'index.html',context)

