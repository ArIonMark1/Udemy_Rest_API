from django.db.models import Model, CharField, TextField, DateTimeField

# Create your models here.
class Note(Model):
    title = CharField(max_length=255)
    text = TextField(blank=True, null=True)
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-updated']




