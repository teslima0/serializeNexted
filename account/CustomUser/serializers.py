from rest_framework import serializers
from .models import User
from rest_framework.authtoken.models import Token

from rest_framework.validators import ValidationError
'''
class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=4, write_only=True)

    class Meta:
        model = User
        fields = ["email", "username", "password"]

    def validate_email(self, attrs):
        if User.objects.filter(email=attrs).exists():
            raise ValidationError("Email already exists")
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
'''
class SignUpSerializer(serializers.ModelSerializer):
    email= serializers.CharField(max_length=80)
    username= serializers.CharField(max_length=45)
    password= serializers.CharField(min_length=4, write_only=True)

    class Meta:
        model=User
        fields=["email","username","password"]


    def validate(self, attrs):

        #email_exists=self.instance.__class__.objects.filter(email=attrs['email']).exists()

        email_exists=User.objects.filter(email=attrs['email']).exists()

        if email_exists:
            raise ValidationError("email already exist")
        
        return attrs 

    def create(self, validate_data):
        password=validate_data.pop('password')
        user= super().create(validate_data)
        user.set_password(password)
        user.save()
        #create token for each user
        Token.objects.create(user=user)
        return user
