from rest_framework.serializers import IntegerField, CharField, Serializer, \
    ModelSerializer, HyperlinkedIdentityField
from notes.models import Note


class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__',


class ThinNoteSerializer(ModelSerializer):
    # url = HyperlinkedIdentityField(view_name='notes-detail')

    class Meta:
        model = Note
        fields = 'id', 'title', 'created',
# class NoteSerializer(Serializer):
#     id = IntegerField(read_only=True)
#     title = CharField(required=True, max_length=255)
#     text = CharField(required=False, allow_blank=True) # allow_blank - указывает что поле может быть пустым
#
#     # описываем поведние формы
#     def create(self, validated_data):
#         return Note.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.text = validated_data.get('text', instance.text)
#         instance.save()
#         return instance
# return super(NoteSerializer, self).update(instance, validated_data)
