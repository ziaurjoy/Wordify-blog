from django.urls import path

from blog.views import post_details

urlpatterns = [
    path('post/details/<int:post_id>', post_details, name='post-details'),
]