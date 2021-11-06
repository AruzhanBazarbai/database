-- TASK 1
-- a
select * from dealer, client;
-- b
select sell.dealer_id,client.name as client_name,client.city,client.priority as grade,sell.id as sell_number,sell.date,sell.amount
    from sell inner join client on sell.client_id=client.id;
-- c
select dealer.id as dealer_id, dealer.name as dealer_name,client.id as client_id, client.name as client_name, client.city
    from dealer inner join client on dealer.id = client.dealer_id and dealer.location=client.city;
-- d
select sell.id as sell_id,sell.amount,client.name as client_name,client.city
    from sell inner join client on sell.client_id = client.id
    where sell.amount>=100 and sell.amount<=500;
-- e
select * from dealer left join client on client.dealer_id=dealer.id;
-- f
select c.name as client_name,c.city,dealer.name as dealer_name,dealer.charge from dealer inner join client c on dealer.id = c.dealer_id;
-- g
select c.name,c.city,d.name,d.charge from client c inner join dealer d on d.id = c.dealer_id where d.charge>0.12;
-- h
select c.name,c.city,s.id as sell_id,s.date as sell_date,s.amount,d.name,d.charge
    from client c left join sell s on c.id = s.client_id left join dealer d on s.dealer_id = d.id;
-- i
select c.name,c.priority,d.name,s.id as sell_id,s.amount as sell_amount
    from client c inner join dealer d on c.dealer_id=d.id left join sell s on c.id=s.client_id
    where s.amount>2000 and c.priority is not null or s.amount is null;

-- TASK 2
-- a
create view cnt_date as
    select s.date,count(distinct s.client_id),avg(s.amount),sum(s.amount)
        from client c inner join sell s on c.id = s.client_id
        group by s.date;
select * from cnt_date;
-- b
create view order_sum as
    select date,sum(amount) from sell
    group by date
    order by sum(amount) desc;
select * from order_sum
    limit 5;
-- c
create view cnt as
    select dealer_id,count(id),sum(amount) as sum,avg(amount) from sell
        group by dealer_id;
select * from cnt;
-- d
create view cnt_loc1 as
    select d.location, sum(s.amount)*sum(d.charge)
        from dealer d inner join sell s on d.id=s.dealer_id
        group by d.location;
select * from cnt_loc1;
-- e
create view cnt_loc2 as
    select d.location,count(s.id),avg(s.amount),sum(s.amount)
        from sell s inner join dealer d on s.dealer_id=d.id
        group by d.location;
select * from cnt_loc2;
-- f
create view cnt_city as
    select c.city,count(s.id),avg(s.amount),sum(s.amount)
        from sell s inner join client c on s.client_id=c.id
        group by c.city;
select * from cnt_city;
-- g
create view f_loc as
    select d.location as loc,sum(s.amount) as loc_sum
        from sell s inner join dealer d on s.dealer_id=d.id
        group by d.location;
create view f_city as
    select c.city as city,sum(s.amount) city_sum
        from sell s inner join client c on c.id = s.client_id
        group by c.city;
select city,loc_sum,city_sum
    from f_loc inner join f_city on loc=city
    where loc_sum<city_sum;
