FROM python:3.12-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

COPY script.py . 
COPY app.py .

ENTRYPOINT ["python3"]

CMD ["app.py"]