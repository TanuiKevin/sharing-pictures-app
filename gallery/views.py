from django.shortcuts import render, redirect
from .forms import MultiPhotoForm
from .models import Photo
from django.contrib import messages

def upload_photo(request):
    if request.method == 'POST':
        form = MultiPhotoForm(request.POST, request.FILES)
        
        if form.is_valid():
            files = request.FILES.getlist('images')
            if not files:
                messages.error(request, 'No files were selected!')
            else:
                for f in files:
                    Photo.objects.create(image=f)
                messages.success(request, f'Successfully uploaded {len(files)} files!')
                return redirect('index')
    else:
        form = MultiPhotoForm()
    
    return render(request, 'upload.html', {'form': form})

def gallery(request):
    photos = Photo.objects.all().order_by('-uploaded_at')
    return render(request, 'index.html', {'photos': photos})