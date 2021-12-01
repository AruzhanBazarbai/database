-- a. Assume truck 1721 is destroyed in a crash. Find all customers who had a package on that
-- truck at the time of the crash. Find all recipients who had a package on that truck at the time
-- of the crash. Find the last successful delivery by that  truck prior to the crash
with crash_date(value) as
    (select tracking.date from tracking,package,customer
    where tracking.del_transport_id=1721 and tracking.status='crash' and package.package_id=tracking.package_id
        and customer.customer_id=package.customer_id limit 1)
select tracking_id,del_transport_id,package_id,status,date from tracking,crash_date
    where del_transport_id=1721 and status='delivered' and tracking.date<crash_date.value
    order by date desc limit 1;

-- b.Find the customer who has shipped the most packages in the past year.
select customer_id,count(package_id) as cnt
    from package where extract(year from package.delivery_start)=extract(year from now())-1
    group by customer_id
    order by cnt  desc limit 1;

-- c.Find the customer who has spent the most money on shipping in the past year
select customer_id,sum(price) as sum
    from package where extract(year from package.delivery_start)=extract(year from now())-1
    group by customer_id
    order by sum  desc limit 1;

-- d.Find the street with the most customers
select count(customer_id) as cnt_customers,city,street_name from customer
    group by city,street_name
    order by cnt_customers desc limit 1;

-- e.Find those packages that were not delivered within the promised time
select package.package_id,package.delivery_end as planning_delivery_end,tracking.date as delivered_date from tracking,package
    where tracking.package_id=package.package_id and tracking.status='delivered' and tracking.date>package.delivery_end;
-- select count(distinct package_id) from tracking; --17

-- f.Generate the bill for each customer for the past month. Consider creating several types of bills.
    -- f-1. Простой счет: клиент, адрес и сумма задолженности.--7
    select customer.first_name  as name,customer.last_name as surname,customer.city as city,customer.street_name as street,
           customer.home_num as home, sum(package.price) as amount
    from package,customer
        where  extract(month from package.delivery_start)=extract(month from now())-1 and package.customer_id=customer.customer_id
    group by package.customer_id,customer.first_name, package.customer_id, customer.last_name,customer.home_num,package.customer_id,customer.city,
             customer.street_name;
    -- f-2.Счет с перечислением сборов по видам услуг.
    select package.customer_id as id,customer.first_name as name,customer.last_name as surname, sum(package.price) as gen_amount,
           package.price-coalesce(normal.price,0.0)-coalesce(hm.price,0.0)-coalesce(international_shipment.price,0.0) as price_weight,
           count(package.package_id) as cnt,normal.price as normal_price,
           hm.price as hm_price,international_shipment.price as inter_price
        from package inner join customer on package.customer_id = customer.customer_id
            left join hazardous_material hm on package.package_id = hm.package_id
            left join normal on package.package_id = normal.package_id
            left join international_shipment on package.package_id = international_shipment.package_id
        where extract(month from package.delivery_start)=extract(month from now())-1
        group by id,name,surname, normal_price,hm_price,inter_price,price_weight;
    -- f-3.Детализируйте выставление счетов с перечислением каждой отдельной отправки и сборов за нее.
    select package.customer_id as id,customer.first_name as name,customer.last_name as surname,package.package_id as p_id, package.price as amount,
           package.price-coalesce(normal.price,0.0)-coalesce(hm.price,0.0)-coalesce(international_shipment.price,0.0) as price_weight,
            normal.price as n_price,hm.price as hm_price,international_shipment.price as inter_price
        from package inner join customer on package.customer_id = customer.customer_id
            left join hazardous_material hm on package.package_id = hm.package_id
            left join normal on package.package_id = normal.package_id
            left join international_shipment on package.package_id = international_shipment.package_id
        where extract(month from package.delivery_start)=extract(month from now())-1;