from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def home(request):
    context = {'page_name': 'home'}
    return render(request, 'index.html', context)


@login_required
def dashboard(request):
    context = {'page_name': 'dashboard'}
    return render(request, 'dashboard.html', context)
