# Generated by Django 3.1.5 on 2021-03-23 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_userad'),
    ]

    operations = [
        migrations.AddField(
            model_name='userad',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='user.customuser'),
            preserve_default=False,
        ),
    ]