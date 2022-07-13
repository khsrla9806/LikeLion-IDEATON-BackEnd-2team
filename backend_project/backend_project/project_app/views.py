from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, UpdateView, TemplateView
from .forms import PostForm, ScheduleForm
from .models import Post, Schedule, Category
from django.shortcuts import render,redirect, get_object_or_404
from django.views.generic import CreateView
from .forms import PostForm, CommentForm
from .models import Post, Comment
from django.urls import reverse

def home(request):
    post_objects = Post.objects.order_by('-created_at')
    context = {'post_objects' : post_objects}
    return render(request, 'index.html', context)

def team_intro(request):
    return render(request, 'backend_team.html')

def post_list(request):
    post_objects = Post.objects.order_by('-created_at')
    context = {'post_objects' : post_objects}
    return render(request, 'post_list.html', context)

def post_detail(request, pk):
    post_detail_object = Post.objects.get(pk=pk)
    # context = {'post_detail_object' : post_detail_object}
    comment_form=CommentForm()
    return render(request, 'post_detail.html',{'post_detail_object':post_detail_object,'comment_form':comment_form}) #수정

# class PostCreate(CreateView):
#     model = Post
#     form_class = PostForm
#     template_name = 'post_create.html'
#     success_url = '/post_list/'

def post_create(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        schedule_form = ScheduleForm(request.POST)
        context = {'post_form':post_form, 'schedule_form':schedule_form}
        if schedule_form.is_valid():
            schedule = schedule_form.save(commit=False)
            if post_form.is_valid():
                post = post_form.save() # post_form이 DB에 저장됨.
                # post_form DB에 저장된 내용 중 post_id에 해당하는 값을 schedule_form의 post_id에 저장해야 한다.
                schedule.post_id = post.pk
                schedule_form.save()
                return redirect('post_list')
        else:
            return render(request, 'post_create.html', context)
    else:
        post_form = PostForm(request.POST)
        schedule_form = ScheduleForm(request.POST)
        context = {'post_form':post_form, 'schedule_form':schedule_form}
        return render(request, 'post_create.html', context)
        
def post_edit(request, pk):
    post = Post.objects.get(pk=pk)
    schedule = Schedule.objects.get(post_id=pk)
    if request.method == 'POST':
        post_form = PostForm(request.POST, instance=post)
        schedule_form = ScheduleForm(request.POST, instance=schedule)
        context = {'post_form':post_form, 'schedule_form':schedule_form}
        if post_form.is_valid() and schedule_form.is_valid():
            post_form.save(commit=False)
            post.created_at = post.updated_at
            post_form.save()
            schedule_form.save()
            return redirect('post_detail', post.pk)
    else:
        post_form = PostForm(instance=post) # instance = post 를 사용하면 post에 저장되어 있던 이전 내용들을 모두 불러옵니다.
        schedule_form = ScheduleForm(instance=schedule)
        context = {'post_form':post_form, 'schedule_form':schedule_form}
        return render(request, 'post_edit.html', context)
    
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')
        
def company_list(request):
    return render(request, 'company_list.html')

def company_detail(request):
    return render(request, 'company_detail.html')

# <댓글구현>
# 댓글 생성
def new_comment(request,pk):
    comment_form=CommentForm(request.POST)
    if comment_form.is_valid():
        finish_form=comment_form.save(commit=False)
        finish_form.post=get_object_or_404(Post,pk=pk)
        finish_form.save()

    return redirect('post_detail',pk) 

# # 댓글 수정
def comment_update(request, detail_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    pk=detail_pk
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment.save()
            # return redirect('post_detail/',detail_pk) #손보기
            return redirect ('post_detail', pk)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'edit_comment.html', {'form': form})

# 댓글 삭제
def comment_delete(request, detail_pk, comment_pk):
    comment = get_object_or_404(Comment, pk = comment_pk)
    comment.delete()
    pk=detail_pk
    return redirect ('post_detail', pk)