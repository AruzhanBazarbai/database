import random
# 2021-11-30 07:42:26.971059 +00:00
# 2008-10-23
f1=open("employee.txt","w")
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
id=1 
st=['created','processed','submitted for delivery','delivered','received','crashed','in the warehouse']
for i in range(20):
    n=name[random.randint(0,len(name)-1)]
    s=surname[random.randint(0,len(surname)-1)]

    address_from=country[random.randint(0,int(len(country))-1)]
    if address_from=='Kazakhstan':
        city_from=city_Kazakhstan[random.randint(0,len(city_Kazakhstan)-1)]
        street_from=street_Khazakhstan[random.randint(0,len(street_Khazakhstan)-1)]
    elif address_from=='Russian':
        city_from=city_Russian[random.randint(0,len(city_Russian)-1)]
        street_from=street_Russian[random.randint(0,len(street_Russian)-1)]
    elif address_from=='British':
        city_from=city_British[random.randint(0,len(city_British)-1)]
        street_from=street_British[random.randint(0,len(street_British)-1)]
    elif address_from=='China':
        city_from=city_China[random.randint(0,len(city_China)-1)]
        street_from=street_China[random.randint(0,len(street_China)-1)]
    elif address_from=='Germany':
        city_from=city_Germany[random.randint(0,len(city_Germany)-1)]
        street_from=street_Germany[random.randint(0,len(street_Germany)-1)]

    from_home_num=random.randint(1,20)

    a=year[random.randint(0,len(year)-1)]+"-"+month[random.randint(0,len(month)-1)]+'-'
    b=random.randint(0,len(day)-1)
    delivery_start=a+day[b]

    sl=salary[random.randint(0,len(salary)-1)]
    work=shift_at_work[i%2]

    f1.write("insert into Employee values(%d,\'%s\',\'%s\',\'%s\',\'%s\',%d,%d,\'%s\',\'%s\');\n" 
        %(i+1,n,s,city_from,street_from,from_home_num,sl,delivery_start,work))
f1.close()