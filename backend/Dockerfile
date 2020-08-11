FROM python:3.7.7-alpine
WORKDIR /project
ADD . /project
RUN pip install -r requirements.txt
CMD ["python","src/server.py"]