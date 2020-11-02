# Generated by Django 3.1.1 on 2020-10-28 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_movierecomment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activity',
            old_name='activityname',
            new_name='activity_name',
        ),
        migrations.AddField(
            model_name='activity',
            name='activity_type',
            field=models.CharField(default='Some random Activity', max_length=50),
            preserve_default=False,
        ),
    ]