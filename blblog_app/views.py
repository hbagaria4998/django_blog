from django.shortcuts import render
from .models import Post


def home(request):
	context = {
		'posts' : Post.objects.all()
	}
	return render(request,'blblog_app/home.html',context)

def about(request):
	return render(request,'blblog_app/about.html',{'title':'About'})