# Generated by Django 3.1.2 on 2020-10-12 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pictures', '0002_auto_20201012_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='pictures.category'),
        ),
        migrations.AlterField(
            model_name='image',
            name='location',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='pictures.location'),
        ),
    ]
