FROM python:3.6.8

ADD ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

ENV WORKDIR '/proj'
ENV PROJECT_NAME 'app'

WORKDIR ${WORKDIR}
ADD ./app ${WORKDIR}

EXPOSE 8000
