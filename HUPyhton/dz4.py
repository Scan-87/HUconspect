ip = ["192.168.8.34","192.168.4.57","192.168.6.29","192.168.8.112","192.168.8.28","192.168.8.66",]
newip = list(filter((lambda x: x[0:10] == "192.168.8."), ip)); newip2 = list(map(lambda x: x.split("."), newip)); newip3 = list(map(lambda x: tuple(map(int, x)), newip2)); newip4 = list(sorted(newip3, key=lambda x:x[3]))
print(newip4)