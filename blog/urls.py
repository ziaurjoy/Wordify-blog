from django.urls import path

from blog.views import post_details,filter_of_category

urlpatterns = [
    path('post/details/<int:post_id>', post_details, name='post-details'),
    path('post/category/<category_name>', filter_of_category, name='category-filter'),
]