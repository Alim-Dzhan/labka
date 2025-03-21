import datetime

now = datetime.datetime.now()
now_without_microseconds = now.replace(microsecond=0)

print(now_without_microseconds)



"""
import datetime
now = datetime.datetime.now()
delta=datetime.timedelta(microseconds=0)
new_date=now - delta
print(new_date)
"""