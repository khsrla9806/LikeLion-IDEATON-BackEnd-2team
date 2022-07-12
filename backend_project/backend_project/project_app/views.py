from django.shortcuts import render,redirect, get_object_or_404
from django.views.generic import CreateView
from .forms import PostForm, CommentForm
from .models import Post, Comment
from django.urls import reverse

def home(request):
    post_objects = Post.objects.order_by('-id')
    context = {'post_objects' : post_objects}
    return render(request, 'index.html', context)

def team_intro(request):
    return render(request, 'backend_team.html')

def post_list(request):
    post_objects = Post.objects.order_by('-id')
    context = {'post_objects' : post_objects}
    return render(request, 'post_list.html', context)

def post_detail(request, pk):
    post_detail_object = Post.objects.get(pk=pk)
    # context = {'post_detail_object' : post_detail_object}
    comment_form=CommentForm()
    return render(request, 'post_detail.html',{'post_detail_object':post_detail_object,'comment_form':comment_form}) #수정

class PostCreate(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post_create.html'
    success_url = '/post_list/'

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