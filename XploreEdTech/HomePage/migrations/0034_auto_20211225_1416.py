# Generated by Django 3.2.9 on 2021-12-25 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomePage', '0033_alter_techtool_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='techtool',
            name='desc',
            field=models.CharField(max_length=1500, null=True),
        ),
        migrations.AlterField(
            model_name='techtool',
            name='concept',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='techtool',
            name='grade_level',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
