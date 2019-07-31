from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from .models import Imageview, Comment
from django.shortcuts import render
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .forms import PostForm
from django.views.generic import ListView, CreateView 

def imageview(request):
    imageviews = Imageview.objects
    return render(request, 'portfolio/image.html', {'imageviews':imageviews})

class CreatePostView(CreateView): # new
    model = Imageview
    form_class = PostForm
    template_name = 'postimage.html'
    success_url = reverse_lazy('imageview')

def postimage(request):
    return render(request, 'postimage.html')

def image_detail(request, post_id):
    post = get_object_or_404(Imageview, pk =post_id)

    var = {
        'posts':post,
    }
    return render(request, 'image_detail.html', var)

def comment_write(request, post_pk):
    if request.method == 'POST':
        post = get_object_or_404(Imageview, pk=post_pk)
        content = request.POST.get('content')

        conn_user = request.user
        conn_profile =  User.objects.get(username=request.user.get_username())

        Comment.objects.create(post=post, comment_writer=conn_profile, comment_contents=content)
        return redirect('/imageview/image_detail/' + str(post.id))
