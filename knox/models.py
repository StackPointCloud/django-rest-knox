from django.conf import settings
from django.db import models
from django.utils import timezone

from knox import crypto
from knox.settings import CONSTANTS, knox_settings


User = settings.AUTH_USER_MODEL


class AuthTokenManager(models.Manager):
    """
    Manager for AuthToken model
    """
    def create(self, **kwargs):
        token = crypto.create_token_string()
        salt = crypto.create_salt_string()
        digest = crypto.hash_token(token, salt)

        expires = kwargs.get('expires')
        if expires is not None:
             expires = timezone.now() + expires

        kwargs.update({
            'digest': digest,
            'salt': salt,
            'expires': expires
        })

        auth_token = super(AuthTokenManager, self).create(**kwargs)
        auth_token.token = token

        return auth_token


class AuthToken(models.Model):
    """
    Model that houses details of an auth token
    """
    objects = AuthTokenManager()

    name = models.CharField(max_length=200, default='')
    digest = models.CharField(max_length=CONSTANTS.DIGEST_LENGTH, primary_key=True)
    salt = models.CharField(max_length=CONSTANTS.SALT_LENGTH, unique=True)
    user = models.ForeignKey(User, null=False, blank=False, related_name="auth_tokens")
    is_system = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    expires = models. DateTimeField(null=True, blank=True)

    def __unicode__(self):
        return "%s <%s>" % (self.user, self.token_id)

    @property
    def token_id(self):
        return self.digest[:10]
