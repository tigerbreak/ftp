from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import os
# Create your views here.
from django.conf import settings

def upload(request):
    if request.method == 'POST':
        # 获取当前文件所在目录

        fs = FileSystemStorage(
            location=os.path.join(settings.MEDIA_ROOT, 'uploads'),
            base_url=settings.MEDIA_URL + 'uploads/'
        )
        uploads_files = request.FILES.getlist('uploads')
        for upload in uploads_files:
            fs.save(upload.name, upload)
    return render(request, 'upload.html')

def list_uploads(requset):
    uploads_dir = os.path.join(settings.MEDIA_ROOT, 'uploads')
    if not os.path.exists(uploads_dir):
        files = []
    else:
        files = os.listdir(uploads_dir)
        print(files)
    file_list = []
    for file in files:
        file_list.append(os.path.join(settings.MEDIA_URL, 'uploads', file))
        print(file_list)
    return render(requset, 'list_uploads.html', {'file_list': file_list})
