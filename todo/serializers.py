from rest_framework import serializers
from .models import Todo, STATUS_CHOICES, Tag, User
from django.utils import timezone

class TodoSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(
        many=True,
        read_only=False,
        queryset=Tag.objects.all(),
        slug_field='name',
        required=False,
        allow_null=True
    )
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Todo
        fields = ['id', 'title', 'description', 'status', 'due_date', 'timestamp', 'tags', 'owner']

    def to_internal_value(self, data):
        if 'tags' in data:
            # remove leading and trailing spaces from tags
            tags = data.pop('tags')
            data['tags'] = [tag.strip() for tag in tags]

            # create tags if they don't exist
            for tag in data['tags']:
                Tag.objects.get_or_create(name=tag)
        
        if 'status' in data:
            # convert status to integer
            data['status'] = [status[0] for status in STATUS_CHOICES if status[1].lower() == data['status'].lower()][0]
        
        return super().to_internal_value(data)
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # convert status to string
        representation['status'] = STATUS_CHOICES[instance.status][1]
        return representation
    
    def validate(self, data):
        # check if due date is provided for overdue tasks
        if (data['status'] == 3) and (data.get('due_date') is None):
            raise serializers.ValidationError("Due date is required for overdue tasks")
        
        # check if due date comes before timestamp
        if (data.get('due_date') is not None) and (data.get('due_date') < timezone.now()):
            raise serializers.ValidationError("Due date cannot be before timestamp")
        
        # check if due date is more than 7 days from timestamp
        if (data.get('due_date') is not None) and (data.get('due_date') > timezone.now() + timezone.timedelta(days=7)):
            raise serializers.ValidationError("Due date cannot be more than 7 days from timestamp")
        
        return data