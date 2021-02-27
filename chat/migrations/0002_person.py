# Generated by Django 3.1.6 on 2021-02-16 07:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('users', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, primary_key=True, serialize=False, to='auth.user')),
                ('name', models.CharField(max_length=50, verbose_name='full name')),
                ('user_ava', models.CharField(max_length=250, verbose_name='User Photo')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.group')),
            ],
        ),
    ]
