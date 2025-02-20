import datetime
date_str= "12-02-2025 13:30"
date_obj=datetime.datetime.strptime(date_str, "%d-%m-%Y %H:%M")
print(date_obj)

now=datetime.datetime.now()
delta=datetime.timedelta(days=5)
new_date=now + delta
print(new_date)

date1= datetime.datetime(2025, 2, 20)
date2= datetime.datetime(2025, 2, 12)
diff=date1-date2
print(diff)


# 2

import datetime

now = datetime.datetime.now()
print(now)


print(now.year)
print(now.month)
print(now.hour)

my_date = datetime.datetime(2023, 9, 21, 22, 35, 0)
print(my_date)