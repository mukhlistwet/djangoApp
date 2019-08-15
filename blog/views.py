from django.shortcuts import render

# Create your views here.
def index(request):
	context = {
		'judul':'My Blog App',
		'kontributor' : 'Mukhlis',
		'nav' : [
			['/' ,'Home' ],
			['/blog','Blog'],
			['/about','About'],
			[ '/contact','Contact'],
		]
	}
	return render(request,'blog/index.html',context)

def news(request):
	context = {
		'judul':'My News App',
		'kontributor' : 'Pembuat berita',
	}
	return render(request,'blog/index.html',context)

def cerita(request):
	context = {
		'judul':'My Cerita App',
		'kontributor' : 'Penulis',
	}
	return render(request,'blog/index.html',context)