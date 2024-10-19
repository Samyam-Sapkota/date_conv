import datetime
import nepali_datetime


def bs_to_ad(year,month,day):
    return nepali_datetime.date(year,month,day).to_datetime_date().strftime("%Y/%m/%d %A")


def ad_to_bs(year,month,day):
    return nepali_datetime.date.from_datetime_date(datetime.date(year, month, day)).strftime("%Y/%m/%d %G")


