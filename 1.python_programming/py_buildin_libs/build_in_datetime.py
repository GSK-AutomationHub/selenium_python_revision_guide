import datetime

print(datetime.date.today())
today = datetime.date.today()
print(today.strftime("%d/%m/%Y, %H:%M:%S"))
print(datetime.timezone)

print(dir(datetime))
print(help(datetime.timezone))