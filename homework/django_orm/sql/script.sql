create table country
(
    country_id   serial
        primary key,
    country_name varchar(100) not null,
    abbreviation varchar(20)  not null
);

alter table country
    owner to restaurant;

create table city
(
    city_id   serial
        primary key,
    city_name varchar(100) not null,
    country   integer
                           references country
                               on update cascade on delete set null
);

alter table city
    owner to restaurant;

create table restaurant
(
    restaurant_id serial
        primary key,
    name          varchar(100) not null,
    address       varchar(150) not null,
    city          integer
                               references city
                                   on update cascade on delete set null
);

alter table restaurant
    owner to restaurant;

create table employee
(
    employee_id serial
        primary key,
    first_name  varchar(100) not null,
    last_name   varchar(100) not null,
    position    varchar(100) not null,
    restaurant  integer
                             references restaurant
                                 on update cascade on delete set null
);

alter table employee
    owner to restaurant;

create table season
(
    season_id serial
        primary key,
    season    varchar(10) not null
);

alter table season
    owner to restaurant;

create table menu
(
    menu_id    serial
        primary key,
    name       varchar(100) not null,
    for_season integer
                            references season
                                on update cascade on delete set null,
    restaurant integer
                            references restaurant
                                on update cascade on delete set null
);

alter table menu
    owner to restaurant;

create table dish
(
    dish_id    serial
        primary key,
    name       varchar(100) not null,
    components varchar(350) not null,
    recipe     text         not null,
    menu       integer
                            references menu
                                on update cascade on delete set null
);

alter table dish
    owner to restaurant;


