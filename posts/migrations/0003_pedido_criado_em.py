# Generated by Django 3.0 on 2019-12-10 22:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20191210_1900'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='criado_em',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
