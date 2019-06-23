from django.db import models
from . import globalvalues

# Create your models here.
class CalculatorModel(models.Model):
    uid = models.ForeignKey('user.CustomUser', on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    class Meta:
        unique_together = (('uid', 'date'))

    GENDER = globalvalues.get_gender()
    RACE = globalvalues.get_race()
    FAMILY_HX = globalvalues.get_family_hx()
    SMOKER = globalvalues.get_smoking_status()
    IS_DM = globalvalues.get_dm_status()
    IS_TREATED_HTN = globalvalues.get_treated_htn_status()
    IS_STEROID = globalvalues.get_steroid_status()

    ###### General Information ######
    # TODO only 40-79 y/o for 10-year ASCVD risk
    age = models.PositiveSmallIntegerField()
    gender = models.IntegerField(choices=GENDER)
    race = models.PositiveSmallIntegerField(choices=RACE)
    weight = models.PositiveSmallIntegerField()
    height = models.PositiveSmallIntegerField()
    sbp = models.PositiveSmallIntegerField()
    dbp = models.PositiveSmallIntegerField()

    ###### Parameters for 10-year ASCVD risk ######
    is_dm = models.PositiveSmallIntegerField(choices=IS_DM)
    tc = models.PositiveSmallIntegerField()
    hdl = models.PositiveSmallIntegerField()

    ###### Parameters for both calculator ######
    is_treated_htn = models.PositiveSmallIntegerField(choices=IS_TREATED_HTN)
    smoker = models.PositiveSmallIntegerField(choices=SMOKER)

    ###### Parameters for undiagnosed DM ######
    family_hx = models.PositiveSmallIntegerField(choices=FAMILY_HX)
    is_steroid = models.PositiveSmallIntegerField(choices=IS_STEROID)

    ###### risks and bmi ######
    ascvd_risk = models.FloatField(null=True)
    bmi = models.FloatField(null=True)
    dm_risk = models.FloatField(null=True)
