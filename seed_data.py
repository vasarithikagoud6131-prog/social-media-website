import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'socialsite.settings')
import django
django.setup()
from django.contrib.auth import get_user_model
from social.models import Post, Profile

User = get_user_model()
user, created = User.objects.get_or_create(username='demo', defaults={'email': 'demo@example.com'})
if created:
    user.set_password('demo123')
    user.save()
Profile.objects.get_or_create(user=user, defaults={'bio': 'Hello from demo'})
Post.objects.get_or_create(user=user, defaults={'content': 'Welcome to Mini Social!'})
print('Seed data ready')
