from django.shortcuts import render
from . import models as blob_models
from . import forms


# Create your views here.
def blob_home(request):
    context = {
        'posts': blob_models.Post.objects.all()
    }
    return render(request, 'blob/blob_home.html', context)


def blob_post(request, post_id=None):
    post = blob_models.Post.objects.get(id=post_id)
    context = {
        'blob_post': post
    }
    return render(request, 'blob/blob_post.html',
                  context)


def blob_add_post(request):
    form = forms.AddPostForm()
    if request.method == 'POST':
        form = forms.AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            print("-" * 20)
            print(form.cleaned_data)

    context = {
        'form': form
    }
    return render(request,
                  'blob/blob_add_post.html',
                  context)
