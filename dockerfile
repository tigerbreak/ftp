# 使用Python官方镜像作为基础镜像
FROM python:3.10

# 设置工作目录
WORKDIR /app

# 设置环境变量
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 安装系统依赖
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        gcc \
        python3-dev \
    && rm -rf /var/lib/apt/lists/*

# 复制项目文件
COPY ./ftpserver /app
COPY ./requirements.txt /app

# 安装Python依赖
RUN pip install --no-cache-dir -r requirements.txt


# 设置权限
RUN chmod -R 777 /app/ftpserver/quick_ftp/media/uploads

# 暴露端口
EXPOSE 8000

# 启动命令git
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]