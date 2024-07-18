from datetime import datetime, timedelta, date

def mk_weekname(datetime_obj):
    '''mk_weekname()

        >>> datetime_obj = date(2024, 3, 4)
        >>> print(mk_weekname(datetime_obj))
        3/4週
    '''
    m = int(datetime.strftime(datetime_obj, "%m"))
    d = int(datetime.strftime(datetime_obj, "%d"))

    wname = f"{m}/{d}週"

    return(wname)
