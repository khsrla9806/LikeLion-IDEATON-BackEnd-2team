from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model =Post
        fields = ['author', 'title', 'content'] # author는 일단 추가해놓음
        widgets = {
            'author' : forms.TextInput(
                attrs={
                    'class' : 'form-control'
                }
            ),
            'title' : forms.TextInput(
                attrs={
                    'class' : 'form-control'
                }
            ),
            'content' : forms.Textarea(
                attrs={
                    'class' : 'form-control'
                }
            )
        }
        labels = {
            'author' : '닉네임',
            'title' : '제목',
            'content' : '내용'
        }
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['writer','comment_text']
        widgets = {
            'writer' : forms.TextInput(attrs={'class' : 'form-control'}),
            'comment_text' : forms.Textarea(attrs={'class' : 'form-control'})}
        labels = {
            'writer' : '닉네임',
            'comment_text' : '내용'
        }