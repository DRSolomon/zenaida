# Generated by Django 2.1.5 on 2019-01-27 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0008_auto_20190127_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='description',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]