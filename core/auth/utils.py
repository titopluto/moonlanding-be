from __future__ import unicode_literals

from calendar import timegm
from datetime import datetime

from django.conf import settings
from django.utils import six
from django.utils.functional import lazy
from django.utils.timezone import is_naive, make_aware, utc
from django.contrib.auth.models import User

def token_decode(token):
    user = User(id = 13, username = "username", email = "email")
    return user

def create_user_obj(id, email):
    user = User(id=id, username = email, email = email)
    return user

def make_utc(dt):
    if settings.USE_TZ and is_naive(dt):
        return make_aware(dt, timezone=utc)

    return dt


def aware_utcnow():
    return make_utc(datetime.utcnow())


def datetime_to_epoch(dt):
    return timegm(dt.utctimetuple())


def datetime_from_epoch(ts):
    return make_utc(datetime.utcfromtimestamp(ts))


def format_lazy(s, *args, **kwargs):
    return s.format(*args, **kwargs)

format_lazy = lazy(format_lazy, six.text_type)
