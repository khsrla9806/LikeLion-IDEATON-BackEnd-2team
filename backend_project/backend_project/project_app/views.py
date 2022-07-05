from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def post_list(request):
    return render(request, 'post_list.html')

def company_list(request):
    return render(request, 'company_list.html')
