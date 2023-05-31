from rest_framework import serializers
from .models import Todo, STATUS_CHOICES, Tag

class TodoSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(
        many=True,
        read_only=False,
        queryset=Tag.objects.all(),
        slug_field='name',
        required=False,
        allow_null=True
    )

    class Meta:
        model = Todo
        fields = ['id', 'title', 'description', 'status', 'due_date', 'timestamp', 'tags']

    def to_internal_value(self, data):
        if 'tags' in data:
            tags = data.pop('tags')
            data['tags'] = [tag.strip() for tag in tags]
            for tag in data['tags']:
                Tag.objects.get_or_create(name=tag)
        return super().to_internal_value(data)
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['status'] = STATUS_CHOICES[instance.status][1]
        return representation