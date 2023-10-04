from django.shortcuts import render, redirect

from .forms import DocumentUploadForm
from .models import UploadedDocument


def upload_document(request):
    if request.method == 'POST':
        form = DocumentUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('hub')
    else:
        form = DocumentUploadForm()
    context = {'page_name': 'hub', 'form': form}
    return render(request, 'hub/upload.html', context)


def list_documents(request):
    documents = UploadedDocument.objects.all()
    context = {'page_name': 'hub', 'documents': documents}
    return render(request, 'hub/index.html', context)
