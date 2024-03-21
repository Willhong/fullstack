# Python 이미지를 기반으로 사용
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

ENV PYTHONUNBUFFERED 1
# 필요한 패키지 설치
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the project dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the project files to the working directory
COPY . .

# Expose the port that the Django app will run on
EXPOSE 8000

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
