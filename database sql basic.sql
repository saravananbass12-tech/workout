create database saro;
use saro;
create table saravanan(name varchar(70),age int,id int,course varchar(40));
insert into saravanan value("saro",20,55,"Ai")
select * from saravanan;
insert into saravanan value("vishal",20,55,"bca")
insert into saravanan value("gokul",21,58,"bca")
insert into saravanan value("nithish",20,59,"bca")
insert into saravanan value("pattu",29,70,"bca")
insert into saravanan value("viknesh",19,80,"bca")
select * from saravanan;
SET SQL_SAFE_UPDATES = 0;
update  saravanan set course="MCA" where  name="saro";
select * from saravanan;
update saravanan set course="BCA" where id=70;
alter table saravanan add column phone int;
alter table saravanan drop column phone;
select*from saravanan;

