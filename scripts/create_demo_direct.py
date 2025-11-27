import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()

username = 'admin'
email = 'admin@example.com'
password = 'P@ssw0rd123'

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print('Superuser created:', username)
else:
    print('Superuser already exists:', username)

from myapp.models import Todo

Todo.objects.create(title='Buy groceries', description='Milk, eggs, bread')
Todo.objects.create(title='Finish report', description='Complete by Monday')
print('Sample todos created')
