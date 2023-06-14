create database Gym

CREATE TABLE Gyms (
    Gyms_id VARCHAR(5) NOT NULL,
    Gyms_name VARCHAR(20) NOT NULL,
    Gyms_location VARCHAR(20),
    Gyms_contact_number INT,
    CONSTRAINT gyms_id_pk PRIMARY KEY (Gyms_id),
    CONSTRAINT gyms_contact_number_check CHECK (Gyms_contact_number > 7000000)
);

create table Trainer(
Trainer_id varchar(5) NOT NULL,
Trainer_name varchar(20) Not Null,
Trainer_gender varchar(1) Not null check (Trainer_gender in ('M','F')),
Trainer_mobile_number int Not null UNIQUE check (Trainer_mobile_number>7000000),
Trainer_specialization varchar(20),
Trainer_gym_id varchar(5) not null unique ,
constraint Trainer_id_pk primary key (Trainer_id),
constraint trainer_gym_id_fk foreign key (Trainer_gym_id) references Gyms(Gyms_id),
);

create table Members(
Members_id varchar(5) NOT NULL,
Member_name varchar (20) not null,
Member_date_of_birth date not null,
Member_email varchar(20),
Member_mobile_number int Not null UNIQUE check (Member_mobile_number>7000000),
Member_gender varchar(1) Not null check (Member_gender in ('M','F')),
Member_Address varchar (10),
Member_gym_id varchar(5) not null,
constraint Members_id_pk primary key (Members_id),
constraint Member_gym_id_fk foreign key (Member_gym_id) references Gyms(Gyms_id),
);

create table Equipment(
Equipment_id varchar(5) NOT NULL,
Equipment_name varchar(20),
Equipment_manufacturer varchar(20),
Equipment_age int not null,
Equipment_gym_id varchar(5) not null,
constraint Equipment_id_pk primary key (Equipment_id),
constraint Equipment_gym_id_fk foreign key (Equipment_gym_id) references Gyms(Gyms_id),
);


create table Memberships(
Membership_id varchar(5) NOT NULL,
Membership_memberid varchar(5) unique not null,
Membership_start_date date not null,
Membership_end_date date not null,
Membership_type varchar (10) not null,
constraint Membership_id_pk primary key (Membership_id),
constraint Membership_memberid_fk foreign key (Membership_memberid) references Members(Members_id),
);
	