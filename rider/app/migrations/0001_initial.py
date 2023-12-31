# Generated by Django 4.2.4 on 2023-08-19 12:28

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('tour_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('actual_net_amount', models.IntegerField(blank=True, null=True)),
                ('tour_date', models.DateField(blank=True, null=True)),
                ('total_tasks', models.IntegerField(blank=True, null=True)),
                ('completed_tasks', models.IntegerField(blank=True, null=True)),
                ('ongoing_tasks', models.IntegerField(blank=True, null=True)),
                ('rider_name', models.CharField(blank=True, max_length=255, null=True)),
                ('rider_phone', models.CharField(blank=True, max_length=15, null=True)),
                ('tour_status', models.CharField(blank=True, choices=[('COMPLETED', 'COMPLETED'), ('QUEUED', 'QUEUED'), ('STARTED', 'STARTED')], max_length=20, null=True)),
                ('tour_start_time', models.DateTimeField(blank=True, null=True)),
                ('tour_end_time', models.DateTimeField(blank=True, null=True)),
                ('dispatch_time', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'locus_tour_brief',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('task_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('awb', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(blank=True, choices=[('ACCEPTED', 'ACCEPTED'), ('CANCELLED', 'CANCELLED'), ('CLOSED', 'CLOSED'), ('COMPLETED', 'COMPLETED'), ('ONGOING', 'ONGOING'), ('STARTED', 'STARTED'), ('WAITING', 'WAITING')], max_length=20, null=True)),
                ('rider_id', models.CharField(blank=True, max_length=255, null=True)),
                ('rider_name', models.CharField(blank=True, max_length=255, null=True)),
                ('rider_phone', models.CharField(blank=True, max_length=15, null=True)),
                ('task_start_time', models.DateTimeField(blank=True, null=True)),
                ('task_end_time', models.DateTimeField(blank=True, null=True)),
                ('customer_name', models.CharField(blank=True, max_length=255, null=True)),
                ('customer_address', models.CharField(blank=True, max_length=255, null=True)),
                ('instruction', models.TextField(blank=True, null=True)),
                ('tour_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.tour')),
            ],
            options={
                'db_table': 'locus_task_brief',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('password', models.CharField(max_length=255)),
                ('profile_picture', models.BinaryField(blank=True, editable=True, null=True)),
                ('aadhaar_card', models.BinaryField(blank=True, editable=True, null=True)),
                ('pan_card', models.BinaryField(blank=True, editable=True, null=True)),
                ('contact_number', models.CharField(max_length=15, unique=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('bank_name', models.CharField(blank=True, max_length=100, null=True)),
                ('account_number', models.CharField(blank=True, max_length=50, null=True)),
                ('passbook_picture', models.BinaryField(blank=True, editable=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'User',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
