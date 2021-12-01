import random
# 2021-11-30 07:42:26.971059 +00:00
# 2008-10-23
f1=open("transport.txt","w")
# f2=open("normal.txt","w")
# f3=open("haz_mat.txt","w")
# f4=open("inter_ship.txt","w")
# f5=open("processing.txt","w")
# f6=open("customer.txt","w")
# f7=open("account.txt","w")
# f8=open("prepaid_ship.txt","w")
# f9=open("contract_ship.txt","w")
# f10=open("infreq.txt","w")
# f11=open("employee.txt","w")
# f12=open("tracking.txt","w")
# f13=open("transport.txt","w")

month=['01','02','03','04','05','06','07','08','09','10','11']
day=['01','02','03','04','05','06','07','08','09','10',
    '11','12','13','14','15','16','17','18','19','20','21','22',
    '23','24','25','26','27','28','29','30']
year=['1975','1978','1985','1990','1995','2000','2003','1992','1997']
country=['Kazakhstan','Russian','British','China','Germany']
city_Kazakhstan=['Almaty','Astana','Karaganda','Shymkent','Atyrau',"Aktobe","Kyzylorda"]
city_Russian=['Moskva','Sankt-Peterburg','Novosybirsk','Ekaterinburg','Kazan']
city_British=['London','Birmingem','Manchester','Liverpool','Oxford','Edinburg']
city_China=['Shankhai','Pekin','Chendu','Guanchjou']
city_Germany=['Berlin','Gamburg','Munhen','Frankfurt','Shtutgart']
street_Khazakhstan=['Abylai',"Abai",'Shamshi','Manshuk','Tolebi']
street_Russian=['Shkolnaya','Sadovaya','Sovetskaya','Novaya','Naberezhnaya']
street_British=['Baker','Cat','Lame',"Lombard"]
street_China=['Chzhao Denui','Tun Linge','Chzhan Czichjun']
street_Germany=['Bahnhofstrabe','Hauptstrabe','Schulstrabe','Gartenstrabe']

name=['John','David','William','James','Alex','Ethan','Aiden','Oliver','Emma',"Anjelina",'Olivia','Stella','Emilia','Christa']
surname=['Jacob','Ryan','Andrew','Theodor','Nathan','Connor','Biden','Donald','Trump',"Hunter",'Anthony','Jack','Samuel','Bob']
status='green'
salary=[10000,15000,20000]
shift_at_work=['Day','Night']
type_of_transport=['plane','ship','truck']
cost=[10000,15000,20000]
id=1 
for i in range(12):
    id=random.randint(1,2000)
    n=random.randint(2,30)
    type=type_of_transport[random.randint(0,len(type_of_transport)-1)]
    c=cost[random.randint(0,len(cost)-1)]
    
    f1.write("insert into Transport values(%d,%d,\'%s\',%d);\n" 
        %(id,n,type,c))
f1.close()