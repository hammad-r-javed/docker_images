FROM arm64v8/python:3

RUN apt-get -y update &&\
	apt-get -y upgrade

RUN apt-get -y install net-tools

RUN pip3 install jupyterlab netifaces

COPY run.py /run.py

EXPOSE 8888

ENTRYPOINT ["python3", "run.py"]
