create database lab7;
create table customers (
    id integer primary key,
    name varchar(255),
    birth_date date
);

create table accounts(
    account_id varchar(40) primary key ,
    customer_id integer references customers(id),
    currency varchar(3),
    balance float,
    "limit" float
);

create table transactions (
    id serial primary key ,
    date timestamp,
    src_account varchar(40) references accounts(account_id),
    dst_account varchar(40) references accounts(account_id),
    amount float,
    status varchar(20)
);

INSERT INTO customers VALUES (201, 'John', '2021-11-05');
INSERT INTO customers VALUES (202, 'Anny', '2021-11-02');
INSERT INTO customers VALUES (203, 'Rick', '2021-11-24');

INSERT INTO accounts VALUES ('NT10204', 201, 'KZT', 1000, null);
INSERT INTO accounts VALUES ('AB10203', 202, 'USD', 100, 0);
INSERT INTO accounts VALUES ('DK12000', 203, 'EUR', 500, 200);
INSERT INTO accounts VALUES ('NK90123', 201, 'USD', 400, 0);
INSERT INTO accounts VALUES ('RS88012', 203, 'KZT', 5000, -100);

INSERT INTO transactions VALUES (1, '2021-11-05 18:00:34.000000', 'NT10204', 'RS88012', 1000, 'commited');
INSERT INTO transactions VALUES (2, '2021-11-05 18:01:19.000000', 'NK90123', 'AB10203', 500, 'rollback');
INSERT INTO transactions VALUES (3, '2021-06-05 18:02:45.000000', 'RS88012', 'NT10204', 400, 'init');

-- Task2
-- 1
create role accountant;
grant select on accounts,transactions to accountant;
create role administrator createrole;
grant all privileges on accounts,transactions,customers to administrator;
create role support;
grant select,insert on  accounts,transactions,customers to support;
-- 2
create user user1;
create user user2;
create user user3;
grant accountant to user1;
grant administrator to user2;
grant support to user3;
-- 3
grant all privileges on accounts,transactions,customers to user2 with grant option;
-- 4
revoke insert on accounts,transactions,customers from user3;
-- Task3
-- 2
alter table transactions alter column amount set not null;
alter table transactions alter column status set not null;
-- Task5
-- 1
create unique index cust_curr_idx on accounts(customer_id,currency);
-- 2
create index curr_bal_idx on accounts(currency,balance);
-- Task6
begin;
insert into transactions values(4, '2021-11-13 17:13:46.000000', 'RS88012', 'NT10204', 500, 'init');
update accounts set balance=balance-500
    where accounts.account_id='RS88012'; -- 5000->4500
update accounts set balance=balance+500
    where accounts.account_id='NT10204'; -- 1000->1500
update transactions set status='commited' where id=4;
commit;



