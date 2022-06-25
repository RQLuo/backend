from django.contrib import admin
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_authors', 'rate', 'create_date', 'update_date')
    list_filter = ('title', 'creator')
    list_per_page = 7

    def get_authors(self, obj):
        return "\n".join([i.authors for i in obj.authors.all()])


admin.site.register(Article, ArticleAdmin)