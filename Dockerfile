FROM python:3.10
ENV PYTHONUNBUFFERED=1
WORKDIR /django
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]