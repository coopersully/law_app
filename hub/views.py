from django.db.models import Q
from django.http import FileResponse, HttpResponse, HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404

from .forms import DocumentUploadForm
from .models import UploadedDocument


def upload_document(request):
    # Check if the user is an admin (staff or superuser)
    allowedRoles = ['staff', 'Staff', 'admin', 'Admin']
    if not (any([request.user.role == allowedRole for allowedRole in allowedRoles])):
        return HttpResponseForbidden("You don't have permission to access this page.")

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

    # check if allowed user
    allowedRoles = ['staff', 'Staff', 'admin', 'Admin']
    allowed_user = any([request.user.role == allowedRole for allowedRole in allowedRoles])

    context = {'page_name': 'hub', 'documents': documents, 'allowed_user':allowed_user}
    return render(request, 'hub/index.html', context)


def serve_document(request, doc_id):
    document = get_object_or_404(UploadedDocument, id=doc_id)
    response = FileResponse(document.file)
    response['Content-Disposition'] = f'inline; filename="{document.file.name.split("/")[-1]}"'
    return response