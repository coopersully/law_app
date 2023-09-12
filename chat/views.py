from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def chat(request):
    context = {
        'page_name': 'chat',
    }
    return render(request, 'chat/index.html', context)
