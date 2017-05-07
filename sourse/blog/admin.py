from django.contrib import admin
from blog import models


class ArticleAdmin(admin.ModelAdmin):
    # marked
    list_display = ['title', 'summary', 'create_time', 'update_time']
    search_fields = ['title', 'summary']
    list_filter = ['create_time', 'update_time']

admin.site.register(models.Article, ArticleAdmin)
