FROM python:alpine3.17
WORKDIR /usr/app/src
COPY passgen.py ./
ENTRYPOINT ["python", "./passgen.py"]
