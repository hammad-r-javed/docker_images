FROM arm64v8/python:3

RUN apt-get -y update &&\
	apt-get -y upgrade

RUN apt-get -y install net-tools

RUN pip3 install jupyterlab netifaces numpy matplotlib

EXPOSE 3000

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--no-browser", "--port=3000", "--allow-root", "--NotebookApp.token=''", "--NotebookApp.password=''"]
