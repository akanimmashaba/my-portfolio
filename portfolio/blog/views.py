from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import ListView





class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'
    paginate_by = 10  # Number of posts to display per page

    def get_queryset(self):
        return Post.objects.filter(status='published').order_by('-created_at')



def post_detail(request, slug):
    # Retrieve the post or return a 404 error
    post = get_object_or_404(Post, slug=slug)

    # Retrieve the hit count object for the post
    hit_count = post.hit_count

    # Increase the hit count
    if not request.session.session_key:
        request.session.save()
    hit_count_response = hit_count.hit(request.session.session_key)

    # Pass the post and hit count to the template
    context = {
        'post': post,
        'hit_count': hit_count_response.hit_count,
    }

    return render(request, 'post_detail.html', context)
