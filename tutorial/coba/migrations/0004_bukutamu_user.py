# Generated by Django 3.2.7 on 2021-09-29 02:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('coba', '0003_auto_20210928_2215'),
    ]

    operations = [
        migrations.AddField(
            model_name='bukutamu',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
