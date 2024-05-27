import time 

Beatles = []

Beatles.append("John Lennon")
Beatles.append("Paul McCartney")
Beatles.append("George Harrison")

for i in range(2): 
    Beatles.append(input("Nome de um membro da banda: "))
    
del Beatles[-2:]
del Beatles[-1:] #remove o stu e pete

Beatles.insert(0, "Ringo Starr")

print(Beatles)

time.sleep(0.1)







