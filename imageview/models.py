from django.db import models
from django.contrib.auth.models import User



class Imageview(models.Model):
    author = models.CharField(max_length=20, blank=True)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='image/')
    description = models.CharField(max_length=500)
    
    def __str__(self):
        return self.title[:100]
    
class Comment(models.Model):
    post = models.ForeignKey(Imageview, on_delete=models.CASCADE, null=True, related_name='comments')
    comment_date = models.DateTimeField(auto_now_add=True)
    comment_contents = models.CharField(max_length=200)
    comment_writer = models.CharField(max_length=20)

    class Meta:
        ordering = ['-id']
