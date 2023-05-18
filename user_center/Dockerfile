# 使用官方的 Python 基础镜像
FROM python:3.8-slim-buster

# 设置工作目录
WORKDIR /app

# 将当前目录的内容复制到 Docker 中的 /app 目录
COPY . /app

# 安装项目依赖
RUN pip install --no-cache-dir -r requi.txt

# 开放端口
EXPOSE 5000

# 运行 Flask 服务
CMD ["flask", "run", "--host=0.0.0.0"]
