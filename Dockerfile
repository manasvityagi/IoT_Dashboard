# Dockerfile for asignment 2 7420
FROM python:3.8
# set environment variables
#Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1
# Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1

ADD . /app
# Copy requirement file and run it
RUN pip install -r ./app/requirements.txt

WORKDIR /app

COPY docker-entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
#RUN dos2unix /entrypoint.sh && apt-get --purge remove -y dos2unix && rm -rf /var/lib/apt/lists/*
#CMD ["python", "manage.py", "runserver","0.0.0.0:8000"]
CMD ["gunicorn", "--bind", ":8000", "--workers", "2", "IoT_Dashboard.wsgi:application"]
EXPOSE 8000
ENTRYPOINT [ "/entrypoint.sh" ]



