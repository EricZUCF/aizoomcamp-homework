import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from django.contrib.auth import get_user_model
from myapp.models import Todo

User = get_user_model()
print('Superuser exists:', User.objects.filter(username='admin').exists())
print('Todos count:', Todo.objects.count())
for t in Todo.objects.all():
    print('TODO:', t.pk, t.title, repr(t.description), 'resolved=' + str(t.resolved))
