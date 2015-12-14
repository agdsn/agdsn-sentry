import logging

import ldap
from django_auth_ldap.config import LDAPSearch, GroupOfUniqueNamesType

# get all the configuration from the original image
from sentry_docker_conf import *  # noqa

AUTH_LDAP_SERVER_URI = 'ldap://my.ldapserver.com'
AUTH_LDAP_BIND_DN = ''
AUTH_LDAP_BIND_PASSWORD = ''

AUTH_LDAP_USER_SEARCH = LDAPSearch(
    'dc=domain,dc=com',
    ldap.SCOPE_SUBTREE,
    '(mail=%(user)s)',
)

AUTH_LDAP_GROUP_SEARCH = LDAPSearch(
    '',
    ldap.SCOPE_SUBTREE,
    '(objectClass=groupOfUniqueNames)'
)

AUTH_LDAP_GROUP_TYPE = GroupOfUniqueNamesType()
AUTH_LDAP_REQUIRE_GROUP = None
AUTH_LDAP_DENY_GROUP = None

AUTH_LDAP_USER_ATTR_MAP = {
    'first_name': 'givenName',
    'last_name': 'sn',
    'email': 'mail'
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
