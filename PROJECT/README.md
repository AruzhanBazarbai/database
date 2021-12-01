project is db for delivery company
-table Package contains information about package,customer,general amount of package(price for weight,service so on) weight of package,address from shipper and to receiver,and scheduled delivery time
-table International_shipment contains information about packages that needs to delivery to another countries. this requires a declaration id at customs, information about the content of the package, and contains price of this type of service
-table Normal is  for ordinary package(envelope,large box,small box)inside the country, and the price for this type of service
-table Hazardous_material UN_id, id of transport that delivery this package, because we need to delivary Hazardous materials safely, and dangerous level of package and price for this type of service 
-table Processing contains information about in what time employee of this company processed the package and sent to delivering 
-table Customer contains information about Customer
-table Account about account
-table Prepaid_shipment for type of account
-table Infrequent_customer type of account
-table Contract_shipment type of account
-table Tracking contains infromations about tracks,status("creates"-when delivery created,there is employee and transport id is null,because they didn't participate in this,"processed"-when employee is prosessing the package,there is only transport is null,"submitted for delivery"-when transport and driver is submitted a package and go on to journey,"delivered"-when package is delivered to right department,and reciver need to take from this department its package,"received"-when rciver took the package, and there is employee and transport id is null)
And there is information about location address and date
-table Transport contains information about transport
