from django.db.models import Model, CharField, TextField, DateTimeField, ForeignKey, CASCADE
from django.conf import settings

# Create your models here.
User = settings.AUTH_USER_MODEL


class Note(Model):
    title = CharField(max_length=255)
    text = TextField(blank=True, null=True)
    author = ForeignKey(User, blank=False, on_delete=CASCADE)
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-updated']
