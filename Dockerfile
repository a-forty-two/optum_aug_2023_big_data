FROM python:3

WORKDIR app

COPY . .

RUN apt-get update 

RUN pip3 install -r requirements.txt 

EXPOSE 5000

ENTRYPOINT ["python3", "app.py"]
