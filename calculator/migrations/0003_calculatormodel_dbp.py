# Generated by Django 2.2.2 on 2019-06-23 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0002_auto_20190617_0457'),
    ]

    operations = [
        migrations.AddField(
            model_name='calculatormodel',
            name='dbp',
            field=models.PositiveSmallIntegerField(default=100),
            preserve_default=False,
        ),
    ]