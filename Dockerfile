FROM python:3.8.8

WORKDIR ./

RUN pip install -r requirements.txt

EXPOSE 8000
CMD ["python", "manage.py", "runserver"]