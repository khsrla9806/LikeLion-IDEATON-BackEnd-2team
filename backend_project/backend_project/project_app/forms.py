from django import forms
from .models import Post, Schedule, Comment, Company_Comment

class PostForm(forms.ModelForm):
    class Meta:
        model =Post
        fields = ['author', 'title', 'content', 'category',] # author는 일단 추가해놓음
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
            'content' : '내용',
            'category' : '카테고리',
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

class Company_CommentForm(forms.ModelForm):
    class Meta:
        model = Company_Comment
        fields = ['writer','comment_text','image','grade']
        widgets = {
            'writer' : forms.TextInput(attrs={'class' : 'form-control'}),
            'comment_text' : forms.Textarea(attrs={'class' : 'form-control'}),
            'image' :  forms.FileInput(attrs={'class':'form-control p-3'}), 
            'grade': forms.Select(attrs={'class' : 'form-select '}) 
        }     
        labels = {
            'writer' : '닉네임',
            'comment_text' : '내용',
            'image' : '사진업로드',
            'grade' : '평점',
        }