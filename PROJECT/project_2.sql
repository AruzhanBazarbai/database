create database project_delivery_company;
create table Package(
    package_id integer primary key,
    customer_id integer references Customer(customer_id),
    weight numeric(10,5) not null,
    price numeric(10,3) check(price>0),
    from_city text not null,
    from_street_name text not null,
    from_home_num integer not null,
    to_city text not null,
    to_street_name text not null,
    to_home_num integer not null,
    delivery_start date not null, --время оформления заказа
    delivery_end date not null --планированное время доставки
);
create table Normal(
    package_id integer references Package(package_id),
    type_of_package text not null, --flat envelope, small box, larger boxes, etc.
    price numeric check(price>0)
);
create table International_shipment(
    package_id integer references Package(package_id),
    declaration_id integer unique not null,
    contents text not null,
    price numeric(10,3) check(price>0)

);
create table Hazardous_material(
    package_id integer references Package(package_id),
    UN_id integer unique not null ,
    transport_id integer not null,
    level text not null,
    price numeric(10,3) check(price>0)
);
create table Processing(
    package_id integer references Package(package_id),
    employee_id integer references Employee(employee_id),
    primary key (package_id,employee_id),
    processing_time date not null
);
create table Customer(
    customer_id integer primary key,
    first_name text not null,
    last_name text not null,
    city text not null,
    street_name text not null,
    home_num integer not null,
    date_of_birth date,
    num_orders integer not null,
    status text
);
create table Account(
    account_id integer,
    customer_id integer references Customer(customer_id),
    primary key (account_id,customer_id)
);
create table Prepaid_shipment(
    account_id integer,
    customer_id integer,
    foreign key(account_id,customer_id) references Account(account_id,customer_id),
    package_id integer references Package(package_id),
    receipt_num text not null
);
create table Infrequent_customer(
    account_id integer,
    customer_id integer,
    foreign key(account_id,customer_id) references Account(account_id,customer_id),
    package_id integer references Package(package_id),
    credit_card_number text not null
);
create table Contract_shipment(
    account_id integer,
    customer_id integer,
    foreign key(account_id,customer_id) references Account(account_id,customer_id),
    package_id integer references Package(package_id),
    bill_every_month numeric not null ,
    account_num text not null ,
    months integer not null

);
create table Employee(
    employee_id integer primary key,
    first_name text not null,
    last_name text not null,
    city text not null,
    street_name text not null,
    home_num integer not null,
    salary integer not null ,
    date_of_birth date,
    shift_at_work text not null

);
create table Tracking(
    tracking_id integer ,
    del_transport_id integer references Transport(transport_id),
    del_employee_id integer references Employee(employee_id),
    package_id integer references Package(package_id),
    primary key (tracking_id,package_id),
    status text not null , --created,processed,submitted for delivery,delivered,received,crashed,in the warehouse
    location_country text,
    location_city text,
    location_street_name text,
    date date not null --если статус доставлен/получен, то здесь будет время доставки
);
create table Transport(
    transport_id integer primary key,
    num_of_trips integer not null,
    type text not null, --plane,truck,ship
    cost_of_transport integer
);
-----creating indexes
create index idx_address_custom on customer(city,street_name);
create index idx_name_custom on customer(first_name,last_name);
create index idx_package_date on package(delivery_start,delivery_end);
create index idx_track_tr on tracking(del_transport_id);