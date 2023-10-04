from django.shortcuts import render

from django.shortcuts import render, redirect
from .models import UploadedDocument
from .forms import DocumentUploadForm


def upload_document(request):
    if request.method == 'POST':
        form = DocumentUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('hub')
    else:
        form = DocumentUploadForm()
    return render(request, 'hub/upload.html', {'form': form})


def list_documents(request):
    documents = UploadedDocument.objects.all()
    return render(request, 'hub/index.html', {'documents': documents})
