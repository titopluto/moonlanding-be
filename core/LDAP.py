from django.conf import settings
import sys, ldap, ldapurl
from .ResponseStatus import ResponseStatus

LDAP_URL = settings.LDAP_URL
LDAP_ROOT_USER_DN = settings.LDAP_USER_DN
LDAP_ROOT_USER_PASS = settings.LDAP_USER_PASS
LDAP_USER_SEARCH_BASE = "ou=users,dc=inwk,dc=dal,dc=ca"

def changePassword(user_email, old_pass, new_pass):

    ldap.set_option(ldap.OPT_DEBUG_LEVEL,0)

    lu = ldapurl.LDAPUrl(LDAP_URL)

    l = ldap.initialize(lu.initializeUrl())

    l.protocol_version=ldap.VERSION3

    l.simple_bind_s(LDAP_ROOT_USER_DN,LDAP_ROOT_USER_PASS)

    user_dn = get_user_dn(l, user_email)

    if user_dn:
        try:
            output = l.passwd_s(user_dn, old_pass, new_pass)
            res = ResponseStatus(200, "SUCCESS", "Password changed successfully")
        except ldap.UNWILLING_TO_PERFORM:
            res = ResponseStatus(400, "OLDPASSWRONG","Old Password not correct")
        except:
            res = ResponseStatus(400, "WENTWRONG", "Something went wrong")
    else:
        res = ResponseStatus(400, "NOUSERNAMEFOREMAIL", "No dn found for email")

    l.unbind_s()

    return res

def get_user_dn(l, email):

    result = l.search_s(LDAP_USER_SEARCH_BASE,ldap.SCOPE_ONELEVEL,'(mail={})'.format(email),['uid'])

    if result and result[0]:
        cn, detail = result[0]
        return cn
    else:
        return None


