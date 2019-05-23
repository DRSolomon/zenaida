# Generated by Django 2.2 on 2019-05-09 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0013_auto_20190425_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domain',
            name='status',
            field=models.CharField(choices=[('inactive', 'INACTIVE'), ('to_be_deleted', 'TO BE DELETED'), ('to_be_restored', 'TO BE RESTORED'), ('blocked', 'BLOCKED'), ('unknown', 'UNKNOWN'), ('active', 'ACTIVE')], default='inactive', max_length=32),
        ),
    ]