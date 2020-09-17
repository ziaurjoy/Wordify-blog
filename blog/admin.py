from django.contrib import admin

# Register your models here.
from blog.models import Post,Category,Profile

admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Post)