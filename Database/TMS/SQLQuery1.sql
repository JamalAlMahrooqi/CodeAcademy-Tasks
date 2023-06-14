Create table COLLEGE(
Cl_Code varchar(3),
Cl_Name varchar(40) CONSTRAINT cl_name_not_null NOT NULL,
Cl_Dean varchar(30),
CONSTRAINT college_pk PRIMARY KEY (Cl_Code),
);

insert into COLLEGE values('SCI','Science ','Prof. Salma')
insert into COLLEGE values('COM','Economy ','Prof. Fahim')
insert into COLLEGE values('EDU','Education ','Dr. Hamad')
insert into COLLEGE values('ART','Arts ','Dr. Abdullah')
select * from COLLEGE;

CREATE TABLE DEPARTMENT (
    Dp_Code varchar(4),
    Dp_Name varchar(40) NOT NULL,
    Dp_HoD varchar(30),
    Dp_Col varchar(3),
    CONSTRAINT department_pk PRIMARY KEY (Dp_Code),
    CONSTRAINT Dp_col_fk FOREIGN KEY (Dp_Col) REFERENCES COLLEGE(Cl_Code)
);
insert into DEPARTMENT values('INFS','Information system','Dr. Kamla','COM')
insert into DEPARTMENT values('FINA','Finance','Dr. Salim','COM')
insert into DEPARTMENT values('COMP','Compute Science','Dr. Zohoor','SCI')
insert into DEPARTMENT values('BIOL','Biology','Dr. Othman','SCI')
insert into DEPARTMENT values('HIST','History','Dr. Said','EDU')
select * from department

Create table BOOK(
	BK_ID int,
	BK_Title varchar(60) Constraint bk_title not null,
	Bk_Edition int,
	Bk_#ofPages int constraint bk_pages check (Bk_#ofPages>0),
	Bk_TotalCopies int,
	Bk_RemCopies int,
	CONSTRAINT book_pk PRIMARY KEY (BK_ID),
);	

create table BOOKTOPIC(
Tp_BkID int,
Tp_Desc varchar(30),
constraint tp_bkid_fk foreign key (Tp_BkID) references BOOK(BK_ID),
);


create table BORROWER(
Br_ID varchar(6),
Br_Name varchar(30),
Br_Dept varchar(4),
Br_Mobile int,
Br_City varchar(20),
Br_House# varchar(4),
Br_Type varchar (1),
constraint borrower_pk primary key(Br_ID),
);

create table EMPLOYEE(
Em_ID int,
Em_Office# varchar (6),
Em_Ext# int constraint em_ext_limit check (Em_Ext#>1000),
Constraint employee_pk primary key(Em_ID),
);

create table STUDENT(
St_ID int,
St_Major varchar (60),
St_Cohort int constraint st_cohort_nn NOT NULL,
constraint student_pk primary key (St_ID),
);

CREATE TABLE COURSE (
    Cr_Code varchar(8),
    Cr_Title varchar(24) NOT NULL,
    Cr_CH int,
    Cr_#ofSec int,
    Cr_Dept varchar(4),
    CONSTRAINT course_pk PRIMARY KEY (Cr_Code),
    CONSTRAINT cr_dpt_fk FOREIGN KEY (Cr_Dept) REFERENCES DEPARTMENT(Dp_Code)
);


CREATE TABLE CBLINK (
    Li_CrCode varchar(8),
    Li_BkID int,
    Li_usage varchar(1) CHECK (Li_usage IN ('T', 'R')),
    CONSTRAINT cblink_fk FOREIGN KEY (Li_CrCode) REFERENCES COURSE(Cr_Code),
    CONSTRAINT cblink_fk2 FOREIGN KEY (Li_BkID) REFERENCES BOOK(BK_ID)
);


create table REGISTRATION(
Re_BrID varchar(6),
Re_CrCode varchar(8),
Re_Semester varchar(6) constraint re_semester_nn NOT NULL,
constraint re_brid_fk foreign key (Re_BrID) references BORROWER(Br_ID),
constraint re_crcode_fk foreign key (Re_CrCode) references COURSE(Cr_Code),
);

CREATE TABLE ISSUING (
    is_BrID varchar(6),
    is_BkID int,
    is_DateTaken date NOT NULL,
    is_DateReturn date,
    CONSTRAINT is_datetaken_nn CHECK (is_DateTaken IS NOT NULL),
    CONSTRAINT is_datereturn_not_greaterthan_datetaken CHECK (is_DateReturn > is_DateTaken),
    CONSTRAINT is_brid FOREIGN KEY (is_BrID) REFERENCES BORROWER(Br_ID),
    CONSTRAINT is_bkid FOREIGN KEY (is_BkID) REFERENCES BOOK(BK_ID)
);



