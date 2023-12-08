# syntax=docker/dockerfile:1

FROM python:3.6

WORKDIR /graded_project

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5000
CMD [ "python" "model.py"]
CMD [ "flask", "run","--host","0.0.0.0","--port","5000"]