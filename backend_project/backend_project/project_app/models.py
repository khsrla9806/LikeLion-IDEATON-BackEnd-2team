from django.db import models

class Post(models.Model):
    author = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"[{self.id}] {self.title}"
    
class Comment(models.Model):
    writer=models.CharField(max_length=20)
    comment_text=models.TextField()
    created_time=models.DateTimeField(auto_now_add=True)
    modified_time=models.DateTimeField(auto_now_add=True)
    post=models.ForeignKey(Post,null=True, blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.writer
