CREATE TABLE waiter(
waiter_id smallint not null,
name text,
salary integer,
PRIMARY KEY (waiter_id)
);

CREATE TABLE customer( 
customer_id smallint not null,
name text,
address text,
phone_num text,
PRIMARY KEY (customer_id)
);

CREATE TABLE manager( 
manager_id smallint not null,
name text,
salary integer,
PRIMARY KEY (manager_id)
);

CREATE TABLE chef( 
chef_id smallint not null,
name text,
salary integer,
PRIMARY KEY (chef_id)
);

CREATE TABLE dish( 
dish_id smallint not null,
name text,
description text,
price real,
PRIMARY KEY (dish_id)
);

CREATE TABLE supplier( 
supplier_id smallint not null,
name text,
city text,
phone_num text,
PRIMARY KEY (supplier_id)
);

CREATE TABLE ingredient( 
ingredient_id smallint not null,
name text,
Inventory smallint,
PRIMARY KEY (ingredient_id)
);

