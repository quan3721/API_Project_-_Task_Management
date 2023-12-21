from rest_framework import serializers
from .models import User

# serialize for model User #
class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = User # model
        
        fields = ['id', 'name', 'email', 'password', 'role'] # field

        # don't show password when testing on Postman #
        extra_kwargs = {
            'password': {'write_only': True}
        }
        
    # Convert password to harsh code #  
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        
        if password is not None:
            instance.set_password(password) # set password is being harshed
        instance.save()
        return instance