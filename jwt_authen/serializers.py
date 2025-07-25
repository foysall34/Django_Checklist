from rest_framework import serializers
from .models import User
import random
from django.contrib.auth.password_validation import validate_password
class RegisterSerializer(serializers.ModelSerializer):
    re_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 're_password']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        if data['password'] != data['re_password']:
            raise serializers.ValidationError("Passwords do not match")
        return data

    def create(self, validated_data):
        validated_data.pop('re_password')
        otp = str(random.randint(1000, 9999))
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
        )
        user.otp = otp
        user.is_verified = False
        user.save()

        # Send OTP email
        from django.core.mail import send_mail
        send_mail(
            'Your OTP Code',
            f'Your OTP is {otp}',
            'noreply@example.com',
            [user.email],
        )

        return user

class VerifyOTPSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(max_length=4)

    def validate(self, data):
        try:
            user = User.objects.get(email=data['email'], otp=data['otp'])
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid OTP or email")
        return data

    def save(self):
        user = User.objects.get(email=self.validated_data['email'])
        user.is_verified = True
        user.otp = ''
        user.save()

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)




# for Forget Password 
class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    new_password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    def validate(self, data):
        if data['new_password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match.")
        validate_password(data['new_password'])  # Optional: checks strength
        return data

    def save(self):
        email = self.validated_data['email']
        password = self.validated_data['new_password']
        try:
            user = User.objects.get(email=email)
            user.set_password(password)
            user.save()
        except User.DoesNotExist:
            raise serializers.ValidationError("User with this email does not exist.")
