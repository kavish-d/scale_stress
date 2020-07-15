FROM python:3.8.3

ENV C_FORCE_ROOT 1

ENV PYTHONUNBUFFERED 1

ENV admin_name=admin

ENV admin_password=admin

ENV deploy_date=backup

RUN echo $admin_name

RUN echo $admin_password

RUN echo $deploy_date

# RUN apt-get update && apt-get -y install stress-ng

RUN mkdir /pydash

WORKDIR  /pydash

ADD . /pydash/

# RUN pip install --upgrade pip
RUN pip install -r requirements.txt

#RUN touch db.sqlite3

RUN chmod 777 strss.sh
