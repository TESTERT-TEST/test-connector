# Используйте официальный Python 3.6 образ
FROM python:3.6-slim

# Установите необходимые системные зависимости
RUN apt-get update && apt-get install -y --no-install-recommends \
    libcurl4-openssl-dev \
    libssl-dev \
    python3-dev \
    python3-pip \
    python3-venv \
    qttools5-dev-tools \
    python3-pyqt5 \
    ruby \
    ruby-dev \
    rubygems \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Установите fpm
RUN gem install --no-document fpm

# Установите рабочую директорию
WORKDIR /app

# Скопируйте файлы зависимостей и установите их
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Скопируйте все остальные файлы проекта
COPY . .

# Команда по умолчанию для сборки приложения
CMD ["fbs", "freeze"]
