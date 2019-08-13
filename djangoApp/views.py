from django.http import HttpResponse


#method view

def index(request):
	judul = "<h1>Halaman Home"
	subjudul = "<h2>Selamat datang di mywebsite<h2>"
	output = judul + subjudul
	return HttpResponse(output)

def blog(request):
	return HttpResponse("Halaman Blog")

def about(request):
	return HttpResponse("Halaman About")
