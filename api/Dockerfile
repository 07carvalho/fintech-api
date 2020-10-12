FROM python:3.8
ENV PYTHONUNBUFFERED 1
WORKDIR /app/fintech
COPY requirements.txt /app/fintech
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
COPY . /app/fintech