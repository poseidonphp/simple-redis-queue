FROM python
RUN apt-get update && apt-get install -y supervisor

RUN mkdir /usr/local/app
RUN cd /usr/local/app
WORKDIR /usr/local/app

COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY ./docker/manager/supervisord.conf /etc/supervisord.conf

# CMD will be agent that connects to threadfix
CMD ["tail", "-f", "requirements.txt"]