FROM python:3.6

 LABEL maintainer Tito

 ENV PYTHONUNBUFFERED 1

 RUN apt-get update && apt-get install -y python3-dev libsasl2-dev libldap2-dev vim
 RUN curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -
 RUN apt-get install -y nodejs

 WORKDIR /docker_moonlight

 COPY . /docker_moonlight

# RUN mkdir -p /docker_moonlight/static

 RUN pip3 install -r requirements.txt
 RUN npm install
