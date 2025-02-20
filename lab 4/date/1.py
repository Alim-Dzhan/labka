import datetime

now = datetime.datetime.now()
delta=datetime.timedelta(days=5)
new_date=now - delta
print(new_date)
