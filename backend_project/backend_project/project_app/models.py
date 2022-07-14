from django.db import models
from django.views.generic import *

class Category(models.Model):
    name = models.CharField(max_length=15, unique=True)
    slug = models.SlugField(max_length=200, null=True, unique=True, allow_unicode=True) # allow_unicode 는 slug에 한글도 지원한다. 
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'categories'

class Post(models.Model):
    author = models.CharField(max_length=20, blank=True)
    title = models.CharField(max_length=50, blank=True)
    content = models.TextField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    category = models.ForeignKey(Category, blank=True, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"[{self.id}] {self.title}"
    

class Schedule(models.Model):
    post = models.ForeignKey(Post,null=True, blank=True, on_delete=models.CASCADE)
    sequence = models.CharField(max_length=3, blank=True, null=True)
    place = models.CharField(max_length=20, blank=True, null=True)
    detail_content = models.TextField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return f"[일정 id : {self.id}] [일정순서 : {self.sequence}] [일정내용 : {self.detail_content}] [게시물 id : {self.post_id}]"

class Comment(models.Model):
    writer=models.CharField(max_length=20)
    comment_text=models.TextField()
    created_time=models.DateTimeField(auto_now_add=True)
    modified_time=models.DateTimeField(auto_now_add=True)
    post=models.ForeignKey(Post, null=True, blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.writer