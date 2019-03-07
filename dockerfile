FROM python:3.6-alpine
COPY entrypoint.sh /opt/
COPY cloud_test_app /opt/cloud_test_app
COPY etc/conf.py /etc/cloud_test/
RUN apk add --no-cache \
      bash \
      gcc \
      curl \
      g++ \
      libstdc++ \
      linux-headers \
      musl-dev \
      postgresql-dev \
      mariadb-dev;

RUN mkdir /code
WORKDIR /code
COPY cloud_test_app/requirements.txt /code/
RUN pip install -r requirements.txt\
      && pip install gunicorn gevent  
COPY . /code/
 

# TODO: install django app requirements and gunicorn

EXPOSE 8000
WORKDIR /opt

COPY ./entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]


# TODO: set entrypoint and command (see entrypoint.sh)
