from django.db import models
from ckeditor.fields import RichTextField

class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE, verbose_name="Yazar")
    title = models.CharField(max_length = 50, verbose_name = "Başlık")
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturma Tarihi")
    article_image = models.FileField(blank=True, null=True,verbose_name="Makaleye Resim Ekle")
    def __str__(self):
        return self.title
    class Meta:
        ordering = ["-created_date"]

class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete = models.CASCADE, verbose_name="Makale", related_name="comments")
    comment_author = models.CharField(max_length = 50, verbose_name = "İsim Soyisim")
    comment_content = models.CharField(max_length = 250, verbose_name = "Yorumunuz")
    comment_created_date = models.DateTimeField(auto_now_add=True,verbose_name="Yorum Oluşturma Tarihi")
    def __str__(self):
        return self.comment_content
    class Meta:
        ordering = ["-comment_created_date"]