import numpy as np


def get_ascvd_risk(age, is_diabetes, gender, race, is_smoker, tc, hdl, sbp,
                   is_treated_htn):
    """
    Calculate 10-years ASCVD risk based on 2013ACC/AHA guideline
    Link: https://www.ahajournals.org/doi/pdf/10.1161/01.cir.0000437741.48606.98

    Citation:
        Research Paper
        Goff DC Jr, et. al. 2013 ACC/AHA Guideline on the Assessment of
        Cardiovascular Risk A Report of the American College of
        Cardiology/American Heart Association Task Force on Practice
        Guidelines. Circulation. 2014 Jun 24;129(25 Suppl 2):S49-73.
        doi: 10.1161/01.cir.0000437741.48606.98. Epub 2013 Nov 12.

    The following is based upon models.py
    Gender: 0 = female, 1 = male
    race: 0 = Other, 1 = African American
    is_treated_htn: 0 = not taking antihypertensive, 1 = currently taking
    is_diabetes: 0 = without diabetes, 1 = with diabetes
    is_smoker: 0 = non-smoker, 1 = ex-smoker, 2 = Current smoker
    """
    # Other women coefficient
    COE_WOMEN_O = np.array([-29.799,         # Ln age
                             4.884,          # Ln age squared
                             13.540,         # Ln total cholesterol (mg/dL)
                            -3.114,          # Ln age * Ln total cholesterol
                            -13.578,         # Ln HDL–C
                             3.149,          # Ln age * Ln HDL-C
                             2.019,          # Ln treated SBP (mmHg)
                             0,              # Ln age * Ln treated SBP
                             1.957,          # Ln untreated SBP (mmHg)
                             0,              # Ln age * Ln untreated SBP
                             7.574,          # smoking (1=yes, 0=no)
                             -1.665,         # Ln age * smoking
                             0.661           # diabets (1=yes, 0=no)
    ])

    # African American women coefficient
    COE_WOMEN_A = np.array([17.114,          # Ln age
                             0,              # Ln age squared
                             0.94,           # Ln total cholesterol (mg/dL)
                             0,              # Ln age * Ln total cholesterol
                            -18.920,         # Ln HDL–C
                             4.475,          # Ln age * Ln HDL-C
                             29.291,         # Ln treated SBP (mmHg)
                             -6.432,         # Ln age * Ln treated SBP
                             27.82,          # Ln untreated SBP (mmHg)
                             -6.087,         # Ln age * Ln untreated SBP
                             0.691,          # smoking (1=yes,0=no)
                             0,              # Ln age * smoking
                             0.874           # diabets
    ])

    # Other men coefficient
    COE_MEN_O = np.array([   12.344,         # Ln age
                             0,              # Ln age squared
                             11.853,         # Ln total cholesterol (mg/dL)
                             -2.664,         # Ln age * Ln total cholesterol
                             -7.99,          # Ln HDL–C
                             1.769,          # Ln age * Ln HDL-C
                             1.797,          # Ln treated SBP (mmHg)
                             0,              # Ln age * Ln treated SBP
                             1.764,          # Ln untreated SBP (mmHg)
                             0,              # Ln age * Ln untreated SBP
                             7.837,          # smoking (1=yes, 0=no)
                             -1.795,         # Ln age * smoking
                             0.658           # diabets (1=yes, 0=no)
    ])

    # African American men coefficient
    COE_MEN_A = np.array([   2.469,          # Ln age
                             0,              # Ln age squared
                             0.302,          # Ln total cholesterol (mg/dL)
                             0,              # Ln age * Ln total cholesterol
                             -0.307,         # Ln HDL–C
                             0,              # Ln age * Ln HDL-C
                             1.916,          # Ln treated SBP (mmHg)
                             0,              # Ln age * Ln treated SBP
                             1.809,          # Ln untreated SBP (mmHg)
                             0,              # Ln age * Ln untreated SBP
                             0.549,          # smoking (1=yes, 0=no)
                             0,              # Ln age * smoking
                             0.645           # diabets (1=yes, 0=no)
    ])
    # survival rate baseline
    SURV_WOMEN_O = 0.9665
    SURV_WOMEN_A = 0.9533
    SURV_MEN_O   = 0.9144
    SURV_MEN_A   = 0.8954

    # mean score
    SCORE_WOMEN_O = -29.18
    SCORE_WOMEN_A = 86.61
    SCORE_MEN_O   = 61.18
    SCORE_MEN_A   = 19.54
    if is_smoker != 0:
        is_smoker = is_smoker / is_smoker

    x = np.array([
        np.log(age), np.log(age)**2, np.log(tc), np.log(tc)*np.log(age),
        np.log(hdl), np.log(age)*np.log(hdl), is_treated_htn*np.log(sbp),
        is_treated_htn*np.log(age)*np.log(sbp),
        (1-is_treated_htn)*np.log(sbp),
        (1-is_treated_htn)*np.log(sbp)*np.log(age), is_smoker,
        np.log(age)*is_smoker, is_diabetes
    ])
    if gender == 1 and race == 1:
        coefficient = COE_MEN_A
        mean_score = SCORE_MEN_A
        surv = SURV_MEN_A
    elif gender == 1 and race == 0:
        coefficient = COE_MEN_O
        mean_score = SCORE_MEN_O
        surv = SURV_MEN_O
    elif gender == 0 and race == 1:
        coefficient = COE_WOMEN_A
        mean_score = SCORE_WOMEN_A
        surv = SURV_WOMEN_A
    elif gender == 0 and race == 0:
        coefficient = COE_WOMEN_O
        mean_score = SCORE_WOMEN_O
        surv = SURV_WOMEN_O

    score = np.sum(x.dot(coefficient))
    risk = 1 - np.power(surv, np.exp(score - mean_score))
    return round(risk*100, 2)

def get_dm_risk(age, gender, is_treated_htn, is_steroid, smoker,
                family_hx, bmi):
    """
    Cambridge Diabetes Risk Score

    Website: https://www.mdcalc.com/cambridge-diabetes-risk-score

    Citation: Research Paper
    Griffin SJ, Little PS, Hales CN, Kinmonth AL, Wareham NJ.
    Diabetes risk score: towards earlier detection of type 2 diabetes in
    general practice. Diabetes Metab Res Rev. 2000;16(3):164-71.
    """
    coefficient = np.array([
        -0.879,     # gender, male = 0, female = 1
        1.222,      # taking antihypertensive agents = 1, none = 0
        2.191,      # taking steroids = 1, none = 0
        0.063,      # age in years
    ])
    x = np.array([
        1-gender,
        is_treated_htn,
        is_steroid,
        age
    ])
    if bmi < 25:
        bmi_val = 0
    elif bmi >= 25 and bmi < 27.5:
        bmi_val = 0.699
    elif bmi >= 27.5 and bmi < 30:
        bmi_val = 1.97
    else:
        bmi_val = 2.581
    if family_hx == 0: # no diabetic 1st-degree relative
        family_hx_val = 0
    elif family_hx == 1: #  if parent or sibling with diabetes
        family_hx_val = 0.728
    elif family_hx == 2: # if parent and sibling with diabetes
        family_hx_val = 0.753
    if smoker == 0: # non-smoker
        smoker_val = 0
    elif smoker == 1: # ex-smoker
        smoker_val = -0.218
    elif smoker == 2: # current smoker
        smoker_val = 0.855
    val = sum([smoker_val, bmi_val, family_hx_val, -6.322]) + \
        x.dot(coefficient)
    risk = 1 / (1 + np.exp(-1*val))
    return round(risk * 100, 2)
