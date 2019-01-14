from django.contrib import admin

from .models import Article
#admin.site.register(Article)
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title","author","created_date"]
    list_display_links = ["title","created_date"]
    search_fields = ["title","content"]
    list_filter = ["author","created_date"]
    class Meta:
        model = Article