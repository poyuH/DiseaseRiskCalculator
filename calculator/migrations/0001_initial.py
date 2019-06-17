# Generated by Django 2.2.2 on 2019-06-17 04:39

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
            name='CalculatorModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('age', models.PositiveSmallIntegerField()),
                ('gender', models.IntegerField(choices=[(0, 'female'), (1, 'male')])),
                ('race', models.PositiveSmallIntegerField(choices=[(0, 'Other'), (1, 'African American')])),
                ('weight', models.PositiveSmallIntegerField()),
                ('height', models.PositiveSmallIntegerField()),
                ('sbp', models.PositiveSmallIntegerField()),
                ('is_dm', models.PositiveSmallIntegerField(choices=[(0, 'Not diagnosed with DM'), (1, 'Has DM')])),
                ('tc', models.PositiveSmallIntegerField()),
                ('hdl', models.PositiveSmallIntegerField()),
                ('is_treated_htn', models.PositiveSmallIntegerField(choices=[(0, 'Not treated with HTN'), (1, 'Currently under HTN medication')])),
                ('smoker', models.PositiveSmallIntegerField(choices=[(0, 'Non-smoker'), (1, 'Ex-smoker'), (2, 'Current smoker')])),
                ('family_hx', models.PositiveSmallIntegerField(choices=[(0, 'No diabetic 1st-degree relatives'), (1, 'Parent or sibling with DM'), (2, 'Parent and sibling with DM')])),
                ('is_steroid', models.PositiveSmallIntegerField(choices=[(0, 'Not using steroid'), (1, 'Currently using steroid')])),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('uid', 'date')},
            },
        ),
    ]
