"""
本篇用来记录sql语言
首先本语言不区分大小写，关键字建议大写
可以单行，可以多行，分号结尾
一·DDL语言
1.创建数据库
create database chen default character set utf8mb4;
此句中create database...default character set...为创建数据库关键字
chen为将要创建的数据库的名称，utf8为将要使用的字符编码
2.选择数据库
use chen
此句同上use为选择数据库的关键字，chen为刚创建的数据库
3.删除数据库
drop database chen;
此句中drop database为删除数据库关键字，chen为要删除的数据库的名称
4.创建表
create table 表名(列名 类型，列名 类型，列名 类型）
某些类型需要加上后面的长度限制例如
create table employees(id int,name varchar(10),salary(8,2))
表示创建了一个叫employees的表，这个表有三个列，分别是id，他的类型是整
数，可以限制长度，也可以不限制长度，name列限制长度10，薪水列类型为浮点数类
型，后面的长度限制标识为总长为8，小数点位数为2
5.删除表格
同删除数据库一样使用drop关键字
drop table employees;

"""