list = []
elemanlar = int(input("kaç tane eleman eklemek istiyorsunuz: "))

for i in range(elemanlar):
  eleman = int(input("eleman: "))
  list.append(eleman)

for j in list:
    if(j % 5 == 0):
        print(j)