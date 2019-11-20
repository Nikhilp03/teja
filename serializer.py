from rest_framework import serializers
from .models import notes_note
class notes_noteSerializers(serializers.ModelSerializer):
    class Meta:
        model = notes_note
        fields= "__all__"
