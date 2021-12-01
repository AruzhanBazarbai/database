import random
# 2021-11-30 07:42:26.971059 +00:00
# 2008-10-23
f1=open("processing.txt","w")
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
time_h=['07:','08:','09:','10:','11:','12:','01:','02:','03:','04:','05:','06:']
time_m=['42:','34:','35:','15:','17:','05:','55:','41:','22:','09:','38:','48:']
time_s=['41','31','14','16','21','44','59','18','26','37','33','20']

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
    p_id=random.randint(1,60)
    em=random.randint(1,20)
    i1=random.randint(0,11)
    i2=random.randint(0,11)
    i3=random.randint(0,11)
    a=year[random.randint(0,len(year)-1)]+"-"+month[random.randint(0,len(month)-1)]+'-'
    b=random.randint(0,len(day)-1)
    delivery_start=a+day[b]
    delivery_start=delivery_start+" "+time_h[i1]+time_m[i2]+time_s[i3]
    f1.write("insert into Processing values(%d,%d,\'%s\');\n" 
        %(id,em,delivery_start))
    # fc.write("\'C%d\',\'%s\',\'%s\',\'male\',\'%s\',\'+7(7%d7)%d%d%d%d%d%d%d\',%d\n" 
    #     %(id,name,sname,c,a1,a2,a3,a4,a5,a6,a7,a8,salary))
    id+=1
f1.close()
