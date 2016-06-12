from django.shortcuts import render,get_object_or_404

from .models import Post
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.views.generic import ListView
# Create your views here.

# def post_list(request):
#     # posts = Post.published.all()
#     # return render(request, 'blog/post/list.html', {'posts': posts})
#
#     object_list=Post.published.all()
#     paginator=Paginator(object_list,3)
#     page = request.GET.get('page')
#     try:
#         posts=paginator.page(page)
#     except PageNotAnInteger:
#         posts=paginator.page(1)
#     except EmptyPage:
#         posts=paginator.page(paginator.num_pages)
#     return render(request,'blog/post/list.html',{'page':page,'posts':posts})

class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'

def post_detail(request,year,month,day,post):
    post_d=get_object_or_404(Post,
                           slug=post,
                           publish__year=year,
                           publish__month=month,
                           publish__day=day,
                           status='published')
    return render(request,'blog/post/detail.html',{'post':post_d})

