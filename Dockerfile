FROM python:3.9.7
WORKDIR /opt/source-code/
COPY . /opt/source-code/
RUN pip install -r requirements.txt
RUN python new.py

