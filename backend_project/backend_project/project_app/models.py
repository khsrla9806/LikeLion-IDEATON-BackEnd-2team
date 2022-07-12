from django.db import models

class Post(models.Model):
    author = models.CharField(max_length=20, blank=True)
    title = models.CharField(max_length=50, blank=True)
    content = models.TextField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"[{self.id}] {self.title}"
    
class Schedule(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    sequence = models.IntegerField(blank=True)
    place = models.CharField(max_length=20, blank=True)
    detail_content = models.TextField(max_length=200, blank=True)
    
    def __str__(self):
        return f"[{self.id}] 순서: {self.sequence} 일정내용: {self.detail_content} 게시물 id: {self.post_id}"