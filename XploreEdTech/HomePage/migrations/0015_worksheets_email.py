# Generated by Django 3.2.9 on 2021-12-17 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomePage', '0014_worksheets'),
    ]

    operations = [
        migrations.AddField(
            model_name='worksheets',
            name='email',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
