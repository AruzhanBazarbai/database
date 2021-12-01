import random
# 2021-11-30 07:42:26.971059 +00:00
# 2008-10-23
f1=open("haz.txt","w")
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
type_of_package=['flat envelope','small box','large box']
cost_of_package=[100,200,300]
id=42
contents=['content1','content2','content3','content4','content5','content6']
level=['1','2','3','4','5','6']
price_c=[100,200,300,400,500,600]
for i in range(10):
    a=random.randint(0,5)
    un_id=random.randint(1000,10000)
    f1.write("insert into Hazardous_material values(%d,%d,%d,\'%s\',%d);\n" %(id,un_id,un_id,level[a],price_c[a]))
    # fc.write("\'C%d\',\'%s\',\'%s\',\'male\',\'%s\',\'+7(7%d7)%d%d%d%d%d%d%d\',%d\n" 
    #     %(id,name,sname,c,a1,a2,a3,a4,a5,a6,a7,a8,salary))
    id+=2
# for i in range(20):
#     a=random.randint(0,5)
#     dec_id=random.randint(1000,10000)
#     f1.write("insert into International_shipment values(%d,%d,\'%s\',%d);\n" %(id,dec_id,contents[a],price_c[a]))
#     # fc.write("\'C%d\',\'%s\',\'%s\',\'male\',\'%s\',\'+7(7%d7)%d%d%d%d%d%d%d\',%d\n" 
#     #     %(id,name,sname,c,a1,a2,a3,a4,a5,a6,a7,a8,salary))
#     id+=2
f1.close()
