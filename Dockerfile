FROM python:3

WORKDIR /usr/src/app

COPY . /usr/src/app

RUN pip3 install --user -r requirements.txt

CMD [ "python3", "server.py" ]