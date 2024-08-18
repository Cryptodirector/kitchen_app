# Используем официальный Python образ
FROM python:3.12-slim

# Устанавливаем рабочую директорию
WORKDIR .

# Копируем файлы с зависимостями
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы вашего приложения в контейнер
COPY . .

# Запускаем приложение: сначала активируем виртуальное окружение, затем запускаем uvicorn и python скрипт
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "6000" && python3 app/telegram_app/router.py]