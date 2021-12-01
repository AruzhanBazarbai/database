import random
# 2021-11-30 07:42:26.971059 +00:00
# 2008-10-23
f1=open("package.txt","w")
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
year=['2020','2021']
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
id=1
customer_id=[]
for i in range(60):
    cust_id=random.randint(1,20)
    customer_id.append(cust_id)
    weight=random.randint(0,100)
    price=random.randint(3,10000)

    address_from=country[random.randint(0,int(len(country))-1)]
    
    if address_from=='Kazakhstan':
        city_from=city_Kazakhstan[random.randint(0,len(city_Kazakhstan)-1)]
        street_from=street_Khazakhstan[random.randint(0,len(street_Khazakhstan)-1)]
        city_to=city_Kazakhstan[random.randint(0,len(city_Kazakhstan)-1)]
        street_to=street_Khazakhstan[random.randint(0,len(street_Khazakhstan)-1)]
    elif address_from=='Russian':
        city_from=city_Russian[random.randint(0,len(city_Russian)-1)]
        street_from=street_Russian[random.randint(0,len(street_Russian)-1)]
        city_to=city_Russian[random.randint(0,len(city_Russian)-1)]
        street_to=street_Russian[random.randint(0,len(street_Russian)-1)]  
    elif address_from=='British':
        city_from=city_British[random.randint(0,len(city_British)-1)]
        street_from=street_British[random.randint(0,len(street_British)-1)]
        city_to=city_British[random.randint(0,len(city_British)-1)]
        street_to=street_British[random.randint(0,len(street_British)-1)]
    elif address_from=='China':
        city_from=city_China[random.randint(0,len(city_China)-1)]
        street_from=street_China[random.randint(0,len(street_China)-1)]
        city_to=city_China[random.randint(0,len(city_China)-1)]
        street_to=street_China[random.randint(0,len(street_China)-1)]
    elif address_from=='Germany':
        city_from=city_Germany[random.randint(0,len(city_Germany)-1)]
        street_from=street_Germany[random.randint(0,len(street_Germany)-1)]
        city_to=city_Germany[random.randint(0,len(city_Germany)-1)]
        street_to=street_Germany[random.randint(0,len(street_Germany)-1)]

    
    from_home_num=random.randint(1,20)
    to_home_num=random.randint(1,20)
    a=year[random.randint(0,len(year)-1)]+"-"+month[random.randint(0,len(month)-1)]+'-'
    b=random.randint(0,len(day)-1)
    delivery_start=a+day[b]
    delivery_end=a+day[random.randint(0,20)]
    f1.write("insert into Package values(%d,%d,%d,%d,\'%s\',\'%s\',%d,\'%s\',\'%s\',%d,\'%s\',\'%s\');\n" 
        %(id,cust_id,weight,price,city_from,street_from,from_home_num,city_to,street_to,to_home_num,delivery_start,delivery_end))
    # fc.write("\'C%d\',\'%s\',\'%s\',\'male\',\'%s\',\'+7(7%d7)%d%d%d%d%d%d%d\',%d\n" 
    #     %(id,name,sname,c,a1,a2,a3,a4,a5,a6,a7,a8,salary))
    id+=1
f1.close()
