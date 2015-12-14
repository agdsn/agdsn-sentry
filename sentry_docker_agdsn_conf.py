import logging

import ldap
from django_auth_ldap.config import LDAPSearch, NestedGroupOfNamesType

# get all the configuration from the original image
from sentry_docker_conf import *  # noqa

# to see how slafs does it:
# https://github.com/slafs/sentry-docker/blob/master/sentry_docker_conf.py#L187

AUTH_LDAP_SERVER_URI = os.getenv('LDAP_SERVER', "")
AUTH_LDAP_BIND_DN = os.getenv('LDAP_BIND_DN')
AUTH_LDAP_BIND_PASSWORD = os.getenv('LDAP_BIND_PASSWORD')

AUTH_LDAP_USER_SEARCH = LDAPSearch(
    os.getenv('LDAP_USER_DN'),
    ldap.SCOPE_SUBTREE,
    os.getenv('LDAP_USER_FILTER'),
)

AUTH_LDAP_GROUP_SEARCH = LDAPSearch(
    os.getenv('LDAP_GROUP_DN'),
    ldap.SCOPE_SUBTREE,
    os.getenv('LDAP_GROUP_FILTER'),
)

AUTH_LDAP_GROUP_TYPE = NestedGroupOfNamesType()
AUTH_LDAP_REQUIRE_GROUP = os.getenv('LDAP_GROUP_REQUIRE')
AUTH_LDAP_DENY_GROUP = None

AUTH_LDAP_USER_ATTR_MAP = {
    'first_name': 'givenName',
    'last_name': 'sn',
    'email': 'mail'
}


ldap_is_active = config('LDAP_GROUP_ACTIVE', default='')
ldap_is_superuser = config('LDAP_GROUP_SUPERUSER', default='')
ldap_is_staff = config('LDAP_GROUP_STAFF', default='')

if ldap_is_active or ldap_is_superuser or ldap_is_staff:
    AUTH_LDAP_USER_FLAGS_BY_GROUP = {
        'is_active': ldap_is_active,
        'is_superuser': ldap_is_superuser,
        'is_staff': ldap_is_staff,
    }

AUTH_LDAP_FIND_GROUP_PERMS = False
AUTH_LDAP_CACHE_GROUPS = True
AUTH_LDAP_GROUP_CACHE_TIMEOUT = 3600

AUTH_LDAP_DEFAULT_SENTRY_ORGANIZATION = u'AG DSN'
AUTH_LDAP_SENTRY_ORGANIZATION_MEMBER_TYPE = 'MEMBER'
AUTH_LDAP_SENTRY_ORGANIZATION_GLOBAL_ACCESS = True

AUTHENTICATION_BACKENDS = AUTHENTICATION_BACKENDS + (
    'sentry_ldap_auth.backend.SentryLdapBackend',
)

logger = logging.getLogger('django_auth_ldap')
logger.addHandler(logging.StreamHandler())
logger.setLevel('DEBUG')
