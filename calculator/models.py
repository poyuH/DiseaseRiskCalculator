from django.db import models

# Create your models here.
class Calculator(models.Model):
    """docstring for Calculator"""
    # TODO add member as foreignkey
    # member = models.ForeignKey(PATH_TO_MEMBER_CLASS, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    GENDER = [
        ( 0,'female' ),
        ( 1,'male' )
    ]
    RACE = [
        ( 0, 'Other' ),
        ( 1, 'African American' )
    ]
    FAMILY_HX = [
        ( 0, 'No diabetic 1st-degree relatives' ),
        ( 1, 'Parent or sibling with DM' ),
        ( 2, 'Parent and sibling with DM' )
    ]
    SMOKER = [
        ( 0, 'Non-smoker' ),
        ( 1, 'Ex-smoker' ),
        ( 2, 'Current smoker' ),
    ]
    IS_DM = [
        ( 0, 'No DM' ),
        ( 1, 'With DM' )
    ]
    IS_TREATED_HTN = [
        ( 0, 'Not taking antihypertensive' ),
        ( 1, 'Currently taking antihypertensive' )
    ]
    IS_STEROID = [
        ( 0, 'Not taking steroids' ),
        ( 1, 'Currently taking steroids' )
    ]

    ###### General Information ######
    # TODO only 40-79 y/o for 10-year ASCVD risk
    age = models.PositiveSmallIntegerField()
    gender = models.IntegerField(choices=GENDER)
    race = models.PositiveSmallIntegerField(choices=RACE)

    ###### Parameters for undiagnosed DM ######
    weight = models.PositiveSmallIntegerField()
    height = models.PositiveSmallIntegerField()
    family_hx = models.PositiveSmallIntegerField(choices=FAMILY_HX)
    is_steroid = models.PositiveSmallIntegerField(choices=IS_STEROID)

    ###### Parameters for 10-year ASCVD risk ######
    tc = models.PositiveSmallIntegerField()
    hdl = models.PositiveSmallIntegerField()
    is_dm = models.PositiveSmallIntegerField(choices=IS_DM)

    ###### Parameters for both calculator ######
    is_treated_htn = models.PositiveSmallIntegerField(choices=IS_TREATED_HTN)
    smoker = models.PositiveSmallIntegerField(choices=SMOKER)
    def calculate_cv(self):
        # TODO
        return
    def calculate_dm(self):
        # TODO
        return


