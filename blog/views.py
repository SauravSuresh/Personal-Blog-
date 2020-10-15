from django.shortcuts import render,get_object_or_404,redirect
from blog.models import Post,Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.forms import Postform,CommentForm
from django.urls import reverse_lazy
from django.views.generic import (TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView,View)
from django.utils import timezone
from django.contrib.auth.decorators import login_required
# Create your views here.
def Aboutview(request):
    return render(request,'blog/about.html')

class PostListView(ListView):
    model = Post
    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostView(DetailView):
    model = Post

class PostCreateView(CreateView,LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = Postform
    model = Post

class PostUpdateView(UpdateView,LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = Postform
    model = Post

class PostDeleteView(DeleteView,LoginRequiredMixin):
    model=Post
    success_url = reverse_lazy('post_list')

class DraftlistView(LoginRequiredMixin,ListView):
    model=Post
    login_url='/login/'
    redirect_field_name='blog/post_list.html'
    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True)

@login_required
def post_publish(request,pk):
    post=get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('post_list')

@login_required
def add_comment_to_post(request,pk):
    post=get_object_or_404(Post,pk=pk)
    if request.method == 'POST':
        form= CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.Post = post
            comment.save()
            return redirect('post_detail',pk=pk)
    else:
        form = CommentForm()
    return render(request,'blog/comment_form.html',{'form':form})

@login_required
def comment_approve(request,pk):
    comment=get_object_or_404(Comment,pk=pk)
    comment.approve()
    return redirect('post_detail',pk=comment.Post.pk)

@login_required
def comment_delete(request,pk):
    comment=get_object_or_404(Comment,pk=pk)
    post_pk=comment.Post.pk
    comment.delete()
    return redirect('post_detail',pk=post_pk)
