from django.contrib import admin
from .models import *

admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Portfolio)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Order)

