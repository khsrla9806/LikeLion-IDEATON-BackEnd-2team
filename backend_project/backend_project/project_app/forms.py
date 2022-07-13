from django import forms
from .models import Post, Schedule, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model =Post
        fields = ['author', 'title', 'content'] # author는 일단 추가해놓음
        widgets = {
            'author' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : '',
                },
            ),
            'title' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : '',
                }
            ),
            'content' : forms.Textarea(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : '',
                }
            )
        }
        labels = {
            'author' : '닉네임',
            'title' : '제목',
            'content' : '내용'
        }
        

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['sequence', 'place', 'detail_content',]
        widgets = {
            'sequence' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : '',
                }
            ),
            'place' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : '',
                }
            ),
            'detail_content' : forms.Textarea(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : '',
                }
            ),
        }
        labels = {
            'sequence' : '일정 순서',
            'place' : '장소',
            'detail_content' : '세부 내용'
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