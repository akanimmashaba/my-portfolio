
from django.urls import path
from .views import PostListView,post_detail

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', PostListView.as_view(), name='post-list'),
    path('posts/<slug:slug>/', PostListView.as_view(), name='post-detail'),


]
