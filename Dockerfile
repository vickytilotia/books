FROM python:3.8-alpine

# Allows docker to cache installed dependencies between builds
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Mounts the application code to the image
COPY . books
WORKDIR /books

EXPOSE 8000

# runs the production server
ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]

















# ENV PATH="/scripts:${PATH}"

# COPY ./requirements.txt /requirements.txt

# RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers

# RUN pip install -r /requirements.txt
# RUN apk del .tmp

# RUN mkdir /books
# COPY ./books /books

# WORKDIR /books

# COPY ./scripts /scripts

# RUN chmod +x /scripts/*