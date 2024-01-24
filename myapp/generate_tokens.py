from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


for user in User.objects.all():
    print(user)
    Token.objects.get_or_create(user=user)
    print(f'Token created for user: {user.username}')
