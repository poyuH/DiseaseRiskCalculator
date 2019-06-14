def get_gender():
    GENDER = (
        ( 0,'male' ),
        ( 1,'female' )
    )
    return GENDER

def get_race():
    RACE = (
        ( 0, 'African American' ),
        ( 1, 'Other' )
    )
    return RACE

def get_family_hx():
    FAMILY_HX = (
        ( 0, 'No diabetic 1st-degree relatives' ),
        ( 1, 'Parent or sibling with DM' ),
        ( 2, 'Parent and sibling with DM' )
    )
    return FAMILY_HX

def get_smoking_status():
    SMOKER = (
        ( 0, 'Non-smoker' ),
        ( 1, 'Ex-smoker' ),
        ( 2, 'Current smoker' ),
    )
    return SMOKER


def get_steroid_status():
    IS_STEROID = (
        ( 0, 'Not using steroid' ),
        ( 1, 'Currently using steroid' )
    )
    return IS_STEROID

def get_dm_status():
    IS_DM = (
        ( 0, 'Not diagnosed with DM' ),
        ( 1, 'Has DM' )
    )
    return IS_DM

def get_treated_htn_status():
    IS_TREATED_HTN = (
        ( 0, 'Not treated with HTN' ),
        ( 1, 'Currently under HTN medication' )
    )
    return IS_TREATED_HTN
