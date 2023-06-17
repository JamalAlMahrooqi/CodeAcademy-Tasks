Create database Gym

CREATE TABLE Gyms (
    Gyms_id VARCHAR(5) NOT NULL,
    Gyms_name VARCHAR(20) NOT NULL,
    Gyms_location VARCHAR(20),
    Gyms_contact_number BIGINT,
    CONSTRAINT gyms_id_pk PRIMARY KEY (Gyms_id),
    CONSTRAINT gyms_contact_number_check CHECK (Gyms_contact_number > 7000000)
);


CREATE TABLE Trainer (
    Trainer_id VARCHAR(5) NOT NULL,
    Trainer_name VARCHAR(20) NOT NULL,
    Trainer_gender VARCHAR(1) NOT NULL CHECK (Trainer_gender IN ('M', 'F')),
    Trainer_mobile_number BIGINT NOT NULL UNIQUE CHECK (Trainer_mobile_number > 7000000),
    Trainer_specialization VARCHAR(20),
    Trainer_gym_id VARCHAR(5) NOT NULL UNIQUE,
    CONSTRAINT Trainer_id_pk PRIMARY KEY (Trainer_id),
    CONSTRAINT Trainer_gym_id_fk FOREIGN KEY (Trainer_gym_id) REFERENCES Gyms(Gyms_id)
);

CREATE TABLE Members (
    Members_id VARCHAR(5) NOT NULL,
    Member_name VARCHAR(20) NOT NULL,
    Member_date_of_birth DATE NOT NULL,
    Member_email VARCHAR(20),
    Member_mobile_number BIGINT NOT NULL UNIQUE CHECK (Member_mobile_number > 7000000),
    Member_gender VARCHAR(1) NOT NULL CHECK (Member_gender IN ('M', 'F')),
    Member_Address VARCHAR(10),
    Member_gym_id VARCHAR(5) NOT NULL,
    CONSTRAINT Members_id_pk PRIMARY KEY (Members_id),
    CONSTRAINT Member_gym_id_fk FOREIGN KEY (Member_gym_id) REFERENCES Gyms(Gyms_id)
);

CREATE TABLE Equipment (
    Equipment_id VARCHAR(5) NOT NULL,
    Equipment_name VARCHAR(20),
    Equipment_manufacturer VARCHAR(20),
    Equipment_age INT NOT NULL,
    Equipment_gym_id VARCHAR(5) NOT NULL,
    CONSTRAINT Equipment_id_pk PRIMARY KEY (Equipment_id),
    CONSTRAINT Equipment_gym_id_fk FOREIGN KEY (Equipment_gym_id) REFERENCES Gyms(Gyms_id)
);

CREATE TABLE Memberships (
    Membership_id VARCHAR(5) NOT NULL,
    Membership_memberid VARCHAR(5) NOT NULL UNIQUE,
    Membership_start_date DATE NOT NULL,
    Membership_end_date DATE NOT NULL,
    Membership_type VARCHAR(10) NOT NULL,
    CONSTRAINT Membership_id_pk PRIMARY KEY (Membership_id),
    CONSTRAINT Membership_memberid_fk FOREIGN KEY (Membership_memberid) REFERENCES Members(Members_id)
);



