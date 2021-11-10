import datetime

datelist = []
z = input()
datelist.append(z)

x = datetime.datetime(int(z[6:]), int(z[0:2]), int(z[3:5]))
y = x.strftime("%A")

print(y.upper())