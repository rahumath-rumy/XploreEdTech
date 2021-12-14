# Generated by Django 3.2.9 on 2021-12-13 15:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('HomePage', '0006_remove_reguser_last_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reguser',
            name='email',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profession', models.CharField(max_length=50, null=True)),
                ('school', models.CharField(max_length=50, null=True)),
                ('grade_level', models.CharField(max_length=50, null=True)),
                ('subjects', models.CharField(max_length=50, null=True)),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
