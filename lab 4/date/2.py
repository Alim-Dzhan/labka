import datetime

today = datetime.datetime.now()
delta=datetime.timedelta(days=1)
yesterday=today - delta
tomorrow=today + delta
print("yesterday: ", yesterday)
print("today: ", today)
print("tomorrow: ", tomorrow)