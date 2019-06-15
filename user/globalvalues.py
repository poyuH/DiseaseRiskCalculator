import datetime


def get_birthyear():
    cur_year = datetime.date.today().year
    return [(year, year) for year in range(cur_year-100, cur_year + 1)]


def get_gender():
    GENDER = (
        ( 0,'female' ),
        ( 1,'male' )
    )
    return GENDER


def get_race():
    RACE = (
        ( 0, 'Other' ),
        ( 1, 'African American' )
    )
    return RACE
