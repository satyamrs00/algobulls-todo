from rest_framework import serializers
from .models import Todo, STATUS_CHOICES, Tag, User

class TodoSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(
        many=True,
        read_only=False,
        queryset=Tag.objects.all(),
        slug_field='name',
        required=False,
        allow_null=True
    )
    owner = serializers.SlugRelatedField(
        read_only=False,
        slug_field='username',
        queryset=User.objects.all(),
    )

    class Meta:
        model = Todo
        fields = ['id', 'title', 'description', 'status', 'due_date', 'timestamp', 'tags', 'owner']

    def to_internal_value(self, data):
        if 'tags' in data:
            tags = data.pop('tags')
            data['tags'] = [tag.strip() for tag in tags]
            for tag in data['tags']:
                Tag.objects.get_or_create(name=tag)
        
        if 'status' in data:
            data['status'] = [status[0] for status in STATUS_CHOICES if status[1].lower() == data['status'].lower()][0]
        
        data['owner'] = self.context['request'].user
        print(data)
        return super().to_internal_value(data)
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['status'] = STATUS_CHOICES[instance.status][1]
        return representation