FROM python:3.9

WORKDIR /tests

RUN pip install pytest flask numpy pandas matplotlib

