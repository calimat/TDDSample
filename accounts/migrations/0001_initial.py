# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListUser',
            fields=[
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='superuser status', help_text='Designates that this user has all permissions without explicitly assigning them.')),
                ('email', models.EmailField(serialize=False, primary_key=True, max_length=75)),
                ('groups', models.ManyToManyField(blank=True, related_query_name='user', verbose_name='groups', help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', to='auth.Group', related_name='user_set')),
                ('user_permissions', models.ManyToManyField(blank=True, related_query_name='user', verbose_name='user permissions', help_text='Specific permissions for this user.', to='auth.Permission', related_name='user_set')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
