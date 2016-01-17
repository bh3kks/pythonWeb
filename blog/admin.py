from django.contrib import admin
from blog.models import Categories, TagModel, Entries, Comments

# Register your models here.
admin.site.register(Categories)
admin.site.register(TagModel)
admin.site.register(Entries)

