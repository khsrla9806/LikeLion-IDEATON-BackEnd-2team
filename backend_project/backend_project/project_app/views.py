from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def team_intro(request):
    return render(request, 'backend_team.html')


def post_list(request):
    return render(request, 'post_list.html')

def post_detail(request):
    return render(request, 'post_detail.html')

def company_list(request):
    return render(request, 'company_list.html')

def company_detail(request):
    return render(request, 'company_detail.html')


