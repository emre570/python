list = []
elemanlar = int(input("kaç tane eleman eklemek istiyorsunuz: "))

for i in range(elemanlar):
  eleman = int(input("eleman: "))
  list.append(eleman)

if(list[0]==list[-1]):
  print(list)
  print("result is true")
else:
  print(list)
  print("result is false")