from django.conf import settings
import sys, ldap, ldapurl
from .ResponseStatus import ResponseStatus
import hashlib, base64, binascii
import re

LDAP_URL = settings.LDAP_URL
LDAP_ROOT_USER_DN = settings.LDAP_USER_DN
LDAP_ROOT_USER_PASS = settings.LDAP_USER_PASS
LDAP_USER_SEARCH_BASE = "ou=users,dc=inwk,dc=dal,dc=ca"

ldap.set_option(ldap.OPT_DEBUG_LEVEL,0)
ldap.set_option(ldap.OPT_X_TLS_REQUIRE_CERT, ldap.OPT_X_TLS_NEVER)

EMAIL_REGEX = re.compile("[^@]+@[^@]+\.[^@]+")

def changePassword(user_identifier, old_pass, new_pass):


    lu = ldapurl.LDAPUrl(LDAP_URL)

    l = ldap.initialize(lu.initializeUrl())

    l.protocol_version=ldap.VERSION3

    l.simple_bind_s(LDAP_ROOT_USER_DN, LDAP_ROOT_USER_PASS)

    user_dn, detail = get_user_dn(l, user_identifier)

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

def get_user_dn(l, identifier):

    search_attribute = "uid"
    if EMAIL_REGEX.match(identifier):
        search_attribute = "mail"

    result = l.search_s(LDAP_USER_SEARCH_BASE,ldap.SCOPE_ONELEVEL,'({attribute}={value})'.format(attribute=search_attribute, value=identifier),['uid', 'mail'])

    if result and result[0]:
        cn, detail = result[0]
        return cn, detail
    else:
        return None, None


def get_email_from_identifier(user_identifier):
    lu = ldapurl.LDAPUrl(LDAP_URL)

    l = ldap.initialize(lu.initializeUrl())

    l.protocol_version = ldap.VERSION3

    l.simple_bind_s(LDAP_ROOT_USER_DN, LDAP_ROOT_USER_PASS)

    user_dn, detail = get_user_dn(l, user_identifier)

    if detail and "mail" in detail and detail["mail"]:
        return detail["mail"][0].decode("utf-8")
    else:
        return None

def reset_password(user_email, new_pass):

    lu = ldapurl.LDAPUrl(LDAP_URL)

    l = ldap.initialize(lu.initializeUrl())
    l.set_option(ldap.OPT_REFERRALS, 0)
    l.set_option(ldap.OPT_PROTOCOL_VERSION, 3)
    l.set_option(ldap.OPT_X_TLS, ldap.OPT_X_TLS_DEMAND)
    l.set_option(ldap.OPT_X_TLS_DEMAND, True)
    l.simple_bind_s(LDAP_ROOT_USER_DN, LDAP_ROOT_USER_PASS)

    user_dn, detail = get_user_dn(l, user_email)

    if not user_dn:
        res = ResponseStatus(400, "NOUSERNAMEFOREMAIL", "No dn found for email")
    else:
        sha1coded = hashlib.sha1(bytes(new_pass, "utf-8")).hexdigest()
        password_value = bytes(
            "{SHA}" + base64.b64encode(binascii.unhexlify(sha1coded)).decode('utf-8'),
            'utf-8')

        add_pass = [(ldap.MOD_REPLACE, 'userPassword', [password_value])]
        try:
            l.modify_s(user_dn, add_pass)
            res = ResponseStatus(200, "SUCCESS", "Password changed successfully")
        except Exception as e:
            res = ResponseStatus(400, "WENTWRONG", e.args[0])

    l.unbind_s()

    return res
