# Generated by Django 3.1.7 on 2021-02-25 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210222_1904'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='signedIn',
            field=models.CharField(max_length=20, null=True),
        ),
    ]