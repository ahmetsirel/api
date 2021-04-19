FROM ubuntu
RUN apt-get update && apt-get install -y python3
RUN apt-get install -y python3-pip
COPY . /opt/source_code
RUN pip3 install -r /opt/source_code/requirements.txt
EXPOSE 5000
ENTRYPOINT python3 /opt/source_code/app.py