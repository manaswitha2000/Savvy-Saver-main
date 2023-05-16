FROM python:3.8.8

COPY . /Savvy-Saver-main
WORKDIR /Savvy-Saver-main

RUN pip install -r requirements.txt

EXPOSE 8000
CMD ["python", "manage.py", "runserver"]