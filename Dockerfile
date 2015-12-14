FROM slafs/sentry

MAINTAINER Lukas Juhrich der Große <lukasjuhrich@wh2.tu-dresden.de>


RUN pip install sentry-ldap-auth

ADD sentry_docker_agdsn_conf.py /conf/

# make sentry_docker_conf module importable our custom script
ENV PYTHONPATH /conf
# actually use the new config
ENV SENTRY_CONF_FILE /conf/sentry_docker_agdsn_conf.py

# expose the new port
EXPOSE 9000
