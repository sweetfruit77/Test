use test;
create database if not exists member;
commit;

drop table if exists users;
create table if not exists users(
userid varchar(20) primary key,
userpw varchar(20) NOT NULL,membermember
username varchar(20) NOT NULL,
userage int,
useremail varchar(20),
useradd varchar(50),
usergender varchar(10),
usertel varchar(20));

insert into users values(
'hong',
'1234',
'홍길동',
23,
'kkd479@naver.com',
'부산시북구 만덕동',
'male',
'010-1234-1234');

select * from users;
