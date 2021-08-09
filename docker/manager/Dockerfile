FROM python
RUN apt-get update && apt-get install -y supervisor

RUN mkdir /usr/local/app
RUN cd /usr/local/app
WORKDIR /usr/local/app

COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY ./docker/manager/supervisord.conf /etc/supervisord.conf

# CMD: What command should your script manager perform?
# Manager is responsible for loading items into the queue.
#   Where do they come from? how do they get here?
#   Using a placeholder of "tail -f requirements.txt" for now
CMD ["tail", "-f", "requirements.txt"]
