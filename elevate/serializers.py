from rest_framework import serializers
from .models import *

class art_serializers(serializers.ModelSerializer):
    class Meta:
        model=ARTTable
        fields="__all__"

class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMembersTable
        fields ="__all__"

