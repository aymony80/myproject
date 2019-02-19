from django.shortcuts import render, redirect
from uploads.forms import DocumentForm

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('article_list')
    else:
        form = DocumentForm()
    return render(request, 'uploads/model_form_upload.html', {'form': form })
