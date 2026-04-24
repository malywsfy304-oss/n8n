FROM python:3.9

WORKDIR /code

# نسخ ملف المكتبات وتثبيتها
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# نسخ باقي الملفات (app.py و cookies.json)
COPY . .

# أمر تشغيل السيرفر
CMD ["python", "app.py"]