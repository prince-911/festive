create database festive_ride;

use festive_ride;

create table admin(username varchar(30) primary key,firstname varchar(20) not null,
middlename varchar(20),lastname varchar(20),email varchar(40) not null,number varchar(20) not null
,password varchar(40) not null);
