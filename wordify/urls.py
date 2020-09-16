
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

from blog.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    # path('blog/post/details/<int:post_id>',post_details),
    path('blog/',include('blog.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





