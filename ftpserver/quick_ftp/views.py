from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import os
# Create your views here.

def upload(request):
    if request.method == 'POST':
        # 获取当前文件所在目录
        current_dir = os.path.dirname(__file__)
        print(current_dir)
        # 构建上传目录的完整路径
        upload_dir = os.path.join(current_dir, 'media', 'uploads')

        fs = FileSystemStorage(
            location=upload_dir,
            base_url='/media/uploads/'
        )
        uploads_files = request.FILES.getlist('uploads')
        for upload in uploads_files:
            fs.save(upload.name, upload)
    return render(request, 'upload.html')
