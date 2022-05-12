from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView,DetailView, CreateView

from .forms import CommentForm
from main.models import Post

# def blog(request):
#     context = {
#         'title' : 'blog',
#         'blog': 'active',
#         "posts": Post.objects.all()[:9]
#
#     }
#     return render(request, 'blog.html', context)

class Blog(ListView):
    model = Post
    template_name = 'blog.html'
    context_object_name = 'posts'
    paginate_by = 9

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context.update({
            'title': 'blog',
            'blog': 'active'
        })
        return context


#
# def blog_detail(request, pk):
#     blog = get_object_or_404(Post, pk=pk)
#     if request.method == 'POST':
#         form  = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save()
#             comment.blog = blog
#             comment.save()
#     form = CommentForm()
#     context = {
#         'title' : 'blog-detail',
#         'blog': blog,
#         'form' : form
#     }
#     return render(request, 'blog-details.html', context)


class Blog_detail(DetailView):
    template_name = 'blog-details.html'
    model = Post
    context_object_name = 'blog'


    def post(self,  request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save()
            comment.blog = self.get_object()
            comment.save()
        return redirect('blog')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': 'blog-detail',
            'form': CommentForm()
        })
        return context


