import random
# 2021-11-30 07:42:26.971059 +00:00
# 2008-10-23
f1=open("customer.txt","w")
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
custom_id=[21, 72, 24, 92, 7, 49, 81, 40, 27, 57, 78, 74, 80, 47, 74, 48, 32, 42, 71, 7, 78, 55, 62, 55, 4, 30, 42, 27, 68, 89, 34, 73, 39, 19, 5, 55, 84, 87, 51, 28, 8, 37, 45, 64, 38, 95, 75, 79, 13, 63, 20, 93, 19, 2, 75, 59, 34, 14, 14, 93, 10, 23, 73, 29, 94, 99, 4, 21, 93, 27, 78, 56, 98, 93, 61, 42, 49, 54, 13, 79, 76, 6, 10, 64, 
35, 79, 81, 91, 81, 78, 20, 18, 97, 59, 46, 37, 75, 19, 91, 10, 34, 17, 16, 40, 24, 17, 31, 17, 15, 18, 77, 55, 11, 63, 63, 42, 2, 14, 73, 51, 11, 64, 47, 16, 82, 77, 84, 54, 24, 82, 97, 69, 85, 78, 25, 15, 65, 94, 10, 18, 36, 41, 78, 96, 87, 97, 100, 37, 23, 46, 27, 94, 11, 72, 3, 27, 41, 41, 5, 49, 64, 94, 9, 22, 48, 3, 51, 
35, 76, 26, 13, 30, 88, 89, 11, 32, 54, 96, 57, 61, 11, 15, 41, 3, 67, 81, 59, 5, 16, 68, 21, 98, 90, 51, 22, 80, 10, 89, 80, 17]
custom_id=sorted(custom_id)
customer_id=[custom_id[0]]
for i in range(1,len(custom_id)): 
    if custom_id[i]!=custom_id[i-1]:
        customer_id.append(custom_id[i])
# for i in range(len(customer_id)):
#     print(customer_id[i],end=" ")   
for i in range(20):
    n=name[random.randint(0,len(name)-1)]
    s=surname[random.randint(0,len(surname)-1)]
    num_orders=random.randint(1,10)

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
    f1.write("insert into Customer values(%d,\'%s\',\'%s\',\'%s\',\'%s\',%d,\'%s\',%d,\'%s\');\n" 
        %(i+1,n,s,city_from,street_from,from_home_num,delivery_start,num_orders,status))
f1.close()