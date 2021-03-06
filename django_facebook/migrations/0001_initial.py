# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-04 11:22
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('auth', '0007_alter_validators_add_error_messages'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacebookCustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=30, unique=True, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.')], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('about_me', models.TextField(blank=True, null=True)),
                ('facebook_id', models.BigIntegerField(blank=True, null=True, unique=True)),
                ('access_token', models.TextField(blank=True, help_text='Facebook token for offline access', null=True)),
                ('facebook_name', models.CharField(blank=True, max_length=255, null=True)),
                ('facebook_profile_url', models.TextField(blank=True, null=True)),
                ('website_url', models.TextField(blank=True, null=True)),
                ('blog_url', models.TextField(blank=True, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, choices=[('m', 'Male'), ('f', 'Female')], max_length=1, null=True)),
                ('raw_data', models.TextField(blank=True, null=True)),
                ('facebook_open_graph', models.NullBooleanField(help_text='Determines if this user want to share via open graph')),
                ('new_token_required', models.BooleanField(default=False, help_text='Set to true if the access token is outdated or lacks permissions')),
                ('image', models.ImageField(blank=True, max_length=255, null=True, upload_to='images/facebook_profiles/%Y/%m/%d')),
                ('state', models.CharField(blank=True, max_length=255, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name_plural': 'users',
                'verbose_name': 'user',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='FacebookLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('facebook_id', models.BigIntegerField()),
                ('name', models.TextField(blank=True, null=True)),
                ('category', models.TextField(blank=True, null=True)),
                ('created_time', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FacebookProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_me', models.TextField(blank=True, null=True)),
                ('facebook_id', models.BigIntegerField(blank=True, null=True, unique=True)),
                ('access_token', models.TextField(blank=True, help_text='Facebook token for offline access', null=True)),
                ('facebook_name', models.CharField(blank=True, max_length=255, null=True)),
                ('facebook_profile_url', models.TextField(blank=True, null=True)),
                ('website_url', models.TextField(blank=True, null=True)),
                ('blog_url', models.TextField(blank=True, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, choices=[('m', 'Male'), ('f', 'Female')], max_length=1, null=True)),
                ('raw_data', models.TextField(blank=True, null=True)),
                ('facebook_open_graph', models.NullBooleanField(help_text='Determines if this user want to share via open graph')),
                ('new_token_required', models.BooleanField(default=False, help_text='Set to true if the access token is outdated or lacks permissions')),
                ('image', models.ImageField(blank=True, max_length=255, null=True, upload_to='images/facebook_profiles/%Y/%m/%d')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FacebookUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('facebook_id', models.BigIntegerField()),
                ('name', models.TextField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, choices=[('F', 'female'), ('M', 'male')], max_length=1, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OpenGraphShare',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_domain', models.CharField(max_length=255)),
                ('facebook_user_id', models.BigIntegerField()),
                ('share_dict', models.TextField(blank=True, null=True)),
                ('object_id', models.PositiveIntegerField(blank=True, null=True)),
                ('error_message', models.TextField(blank=True, null=True)),
                ('last_attempt', models.DateTimeField(auto_now_add=True, null=True)),
                ('retry_count', models.IntegerField(blank=True, null=True)),
                ('share_id', models.CharField(blank=True, max_length=255, null=True)),
                ('completed_at', models.DateTimeField(blank=True, null=True)),
                ('removed_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': None,
            },
        ),
        migrations.AlterUniqueTogether(
            name='facebookuser',
            unique_together=set([('user_id', 'facebook_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='facebooklike',
            unique_together=set([('user_id', 'facebook_id')]),
        ),
    ]
