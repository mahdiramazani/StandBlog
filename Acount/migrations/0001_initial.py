# Generated by Django 4.0.6 on 2022-07-12 17:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fiestname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('fathername', models.CharField(max_length=50)),
                ('nation_code', models.CharField(max_length=10)),
                ('image', models.FileField(blank=True, null=True, upload_to='Acount/profile/img')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
