AG DSN Sentry Configuration
===========================

This is a docker image based on
[slafs/sentry](https://github.com/slafs/sentry-docker) using the
advantages of
[sentry-ldap-auth](https://github.com/Banno/getsentry-ldap-auth).


Deployment
----------

Similiar to using the `slafs/sentry` image, just build the docker
image using `docker build -t $desired_image_name .`, and run from
it. The environment variables stay the same, execept you should *not*
set `SENTRY_USE_LDAP=True`, since this will result in the original
`slafs/sentry` implementation being used.
