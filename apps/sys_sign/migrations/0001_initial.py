# Generated by Django 4.2.1 on 2023-05-11 01:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SysLogin',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('active', models.BooleanField(default=True)),
                ('created_by', models.IntegerField(null=True)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_by', models.IntegerField(null=True)),
                ('updated_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('ip', models.CharField(max_length=32, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'sys_login',
                'abstract': False,
            },
        ),
    ]
