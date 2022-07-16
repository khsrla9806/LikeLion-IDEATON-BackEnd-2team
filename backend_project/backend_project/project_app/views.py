from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, UpdateView, TemplateView
from .forms import PostForm, ScheduleForm, Company_CommentForm
from .models import Post, Schedule, Category
from django.shortcuts import render,redirect, get_object_or_404
from django.views.generic import CreateView
from .forms import PostForm, CommentForm
from .models import Post, Comment, Company_Comment
from django.urls import reverse
import ast

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
    schedule_detail_object = Schedule.objects.get(post_id=pk)
    sequence_list = ast.literal_eval(schedule_detail_object.sequence) # str 형태의 리스트를 list 형태로 바꿔주는 메서드입니다. 
    place_list = ast.literal_eval(schedule_detail_object.place)
    detail_list = ast.literal_eval(schedule_detail_object.detail_content)
    schedule_loop = zip(sequence_list, place_list, detail_list)
    comment_form=CommentForm()
    return render(request, 'post_detail.html',{'post_detail_object':post_detail_object,'comment_form':comment_form, 'schedule_loop':schedule_loop})

def post_create(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        schedule_form = ScheduleForm(request.POST)
        context = {'post_form':post_form, 'schedule_form':schedule_form}
        if schedule_form.is_valid():
            schedule = schedule_form.save(commit=False)
            schedule.sequence = request.POST.getlist('sequence')
            schedule.place = request.POST.getlist('place')
            schedule.detail_content = request.POST.getlist('detail_content')
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
    schedule_obj = Schedule.objects.get(post_id=pk)
    if request.method == 'POST':
        post_form = PostForm(request.POST, instance=post)
        schedule_form = ScheduleForm(request.POST, instance=schedule_obj)
        context = {'post_form':post_form, 'schedule_form':schedule_form}
        if schedule_form.is_valid():
            schedule = schedule_form.save(commit=False)
            schedule.sequence = request.POST.getlist('sequence')
            schedule.place = request.POST.getlist('place')
            schedule.detail_content = request.POST.getlist('detail_content')
            if post_form.is_valid():
                post = post_form.save(commit=False)
                schedule.post_id = post.pk
                post.created_at = post.updated_at
                post_form.save()
                schedule_form.save()
            return redirect('post_detail', post.pk)
    else:
        post_form = PostForm(instance=post) # instance = post 를 사용하면 post에 저장되어 있던 이전 내용들을 모두 불러옵니다.
        sequence_list = ast.literal_eval(schedule_obj.sequence) # str 형태의 리스트를 list 형태로 바꿔주는 메서드입니다. 
        place_list = ast.literal_eval(schedule_obj.place)
        detail_list = ast.literal_eval(schedule_obj.detail_content)
        schedule_loop = zip(sequence_list, place_list, detail_list)
        context = {'post_form':post_form, 'schedule_loop':schedule_loop}
        return render(request, 'post_edit.html', context)

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')
        
def company_list(request):
    return render(request, 'company_list.html')

def company_detail(request):
    company_comment_object = Company_Comment.objects.all()
    CC_form=Company_CommentForm()
    return render(request, 'company_detail.html',{'CC_form':CC_form,'company_comment_object':company_comment_object})

# <댓글구현>
# 댓글 생성
def new_comment(request,pk):
    comment_form=CommentForm(request.POST)
    if comment_form.is_valid():
        finish_form=comment_form.save(commit=False)
        finish_form.post=get_object_or_404(Post,pk=pk)
        finish_form.save()

    return redirect('post_detail',pk) 

# 댓글 수정
def comment_update(request, detail_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    pk=detail_pk
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment.save()
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


# 기업 댓글 생성
def new_Company_Comment(request):
    if request.method=='POST' or request.method=='FILES':
        CC_form=Company_CommentForm(request.POST,request.FILES)
        if CC_form.is_valid():
            finish_form=CC_form.save(commit=False)
            # finish_form.post=get_object_or_404(Company_Comment,pk=pk)
            finish_form.save()
            return redirect('company_detail') 
    else:
        CC_form=Company_CommentForm
    return render(request,'company_detail.html',{'CC_form':CC_form})


# 기업 댓글 수정
def companycomment_update(request, comment_pk): #detail_pk
    comment = get_object_or_404(Company_Comment, pk=comment_pk)
    # pk=detail_pk
    pk=comment_pk
    if request.method == "POST" or request.method=='FILES':
        CCU_form = Company_CommentForm(request.POST, request.FILES, instance=comment)
        if CCU_form.is_valid():
            comment.save()
            # return redirect('company_detail/',detail_pk) #company_detail 연결
            return redirect ('company_detail') #pk
    else:
        CCU_form = Company_CommentForm(instance=comment)
    return render(request, 'edit_companycomment.html', {'CCU_form': CCU_form})

# 기업 댓글 삭제
def companycomment_delete(request, comment_pk):
    comment = get_object_or_404(Company_Comment, pk = comment_pk)
    comment.delete()
    return redirect ('company_detail') 