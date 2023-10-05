from django.db.models import Q
from django.http import FileResponse
from django.shortcuts import render, redirect, get_object_or_404

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
    search_query = request.GET.get('search', '')
    documents = UploadedDocument.objects.all()

    if search_query:
        documents = documents.filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query)
        )
    documents.order_by("title")
    context = {'page_name': 'hub', 'documents': documents}
    return render(request, 'hub/index.html', context)


def serve_document(request, doc_id):
    document = get_object_or_404(UploadedDocument, id=doc_id)
    return FileResponse(document.file, content_type='application/pdf')
