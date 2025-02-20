import datetime  
 
date1_str = input("YYYY-mm-dd hh:mm:ss : ")  
date2_str = input("YYYY-mm-dd hh:mm:ss : ")  

date1 = datetime.datetime.strptime(date1_str, "%Y-%m-%d %H:%M:%S")  
date2 = datetime.datetime.strptime(date2_str, "%Y-%m-%d %H:%M:%S")  

diff = abs((date1 - date2).total_seconds())

print(diff)