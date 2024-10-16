import calendar, time as t
from datetime import date as d

class date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    def __str__(self):
        week_days = list(calendar.day_name); month_names = list(calendar.month_name)
        week_day = week_days[calendar.weekday(self.year, self.month, self.day )]
        self.date = f"{week_day}, {month_names[self.month]} {self.day}, {self.year}"
        return self.date
    def __add__(self, other):
        year = self.year; m = self.month; day = self.day
        for i in range(self.day, other + self.day):
            month_days = {1: 31, 2: 29 if year % 4 == 0 and year % 100 != 0 else 28, 3: 31, 4: 30, 5: 31, 6:30, 7: 31, 8: 31, 9: 30, 10:31, 11: 30, 12: 31}
            day = day + 1
            if day == month_days[m] + 1 and m != 12:
                day = 1; m = m + 1
            if day == month_days[m] + 1 and m == 12:
                day = 1; m = 1; year = year + 1
        return date(year, m, day)
    def __sub__(self, other):
        year = self.year; m = self.month; day = self.day
        for i in range(self.day, other + self.day):
            month_days = {1: 31, 2: 29 if year % 4 == 0 and year % 100 != 0 else 28, 3: 31, 4: 30, 5: 31, 6:30, 7: 31, 8: 31, 9: 30, 10:31, 11: 30, 12: 31}
            day = day - 1
            if day == 0 and m != 1:
                m = m - 1; day = month_days[m]
            if day == 0 and m == 1:
                day = 31; m = 12; year = year - 1
        return date(year, m, day)
    def calc_date(self, other):
        "Must be formatted in Year-Month-Day or date object"
        n = [self.year, self.month, self.day]
        try: n2 = [int(i) for i in other.split("-")]
        except: n2 = [other.year, other.month, other.day]
        first, second = n, n2
        if n2[0] <= n[0]:
            if n2[0] < n[0]:
                first = n2; second = n
            elif n2[1] <= n[1]:
                if n2[1] < n[1]:
                    first = n2; second = n
                elif n2[2] < n[2]:
                    first = n2; second = n
        years = second[0] - first[0]
        days = (365 * years) + calendar.leapdays(first[0], second[0])
        month_days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6:30, 7: 31, 8: 31, 9: 30, 10:31, 11: 30, 12: 31}
        days = days + sum([month_days[i] for i in range(first[1], second[1])])
        days = days + (second[2] - first[2])
        status = "days" if days != 1 else "day"
        first = date(first[0], first[1], first[2])
        second = date(second[0], second[1], second[2])
        print(f"{first} - {second}\n\t\t    {days} {status}.")
        
s = str(d.today()); k = [int(i) for i in s.split("-")]
today = date(k[0], k[1], k[2])
def time(time_format = "%B %d, %Y, %I:%M:%S %p"):
    return t.strftime(time_format, t.localtime())
