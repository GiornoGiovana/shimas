# Generated by Django 3.1.1 on 2020-10-20 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('edad', models.IntegerField(default=18)),
            ],
        ),
    ]