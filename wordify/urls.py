
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

from blog.views import home,contact,about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('contact', contact, name='contact'),
    path('about/<int:profile_id>', about, name='about'),
    path('blog/',include('blog.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





