from django.shortcuts import render
from .models import Post
from django.shortcuts import get_object_or_404


# Create your views here.
def post_list(request):
	post_list = Post.objects.all()
	context = {
		"stuff_list": post_list,
	}
	return render(request, 'posts_list.html', context)

def post_detail(request, post_id):
	obj = get_object_or_404(Post, id=post_id)
	context = {
		"instance": obj,
		"user": request.user,		

	}
	return render(request, 'post_detail.html', context)