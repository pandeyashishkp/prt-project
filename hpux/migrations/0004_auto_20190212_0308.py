# Generated by Django 2.1.5 on 2019-02-12 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hpux', '0003_auto_20190210_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hpux',
            name='change_number',
            field=models.CharField(max_length=50),
        ),
    ]