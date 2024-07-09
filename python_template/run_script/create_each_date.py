from datetime import datetime
from dateutil.relativedelta import relativedelta
import sys, unittest

MONTHS_OF_YEAR = 12


def gen_date_list(start, end, day)-> list:
    date_start_str = f"{start['year']}/{start['month']}/{day['start']}"
    date_end_str = f"{end['year']}/{end['month']}/{day['end']}"
    date_start = datetime.strptime(date_start_str, "%Y/%m/%d")
    date_end = datetime.strptime(date_end_str, "%Y/%m/%d")
    day_start = int(day["start"])
    day_end = int(day["end"])

    term = relativedelta(date_end, date_start)
    months = term.years * MONTHS_OF_YEAR
    days = day_end - day_start

    date_list = []
    for m in range(months+1):
        for d in range(days+1):
            try:
                new_date = date_start + relativedelta(months=m, days=d)
            except ValueError:
                break
            date_list.append(new_date)

    return(date_list)

class Test_create_each_date(unittest.TestCase):

    def setUp(self):
        start = {"year": "2023", "month": "3"}
        end = {"year": "2024", "month": "3"}
        day = {"start": "1", "end": "31"}
        self.args = [start, end, day]

    def test_gen_date_list_type(self):
        self.assertEqual(type(gen_date_list(*self.args)), list)

    def test_gen_date_list_length(self):
        self.assertNotEqual(len(gen_date_list(*self.args)), 0)

    def test_gen_date_list_each_type(self):
        date_list = gen_date_list(*self.args)
        start, end, day = self.args
        container = [start["year"], end["year"]]
        for date in date_list:
            self.assertEqual(type(date), datetime)
            #self.assertIn(date[:3], container, msg="invalid year")

if __name__ == "__main__":
    start = {"year": "2022", "month": "3"}
    end = {"year": "2023", "month": "3"}
    day = {"start": "1", "end": "31"}
    args = [start, end, day]

    date_list = gen_date_list(*args)

    for date in date_list:
        print(date.strftime("%Y%m%d"))
