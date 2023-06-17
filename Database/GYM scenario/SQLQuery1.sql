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




INSERT INTO Gyms (Gyms_id, Gyms_name, Gyms_location, Gyms_contact_number)
VALUES 
    ('G001', 'Fitness First', 'New York', 1234567890),
    ('G002', 'Gold''s Gym', 'Los Angeles', 9876543210),
    ('G003', '24 Hour Fitness', 'Chicago', 5555555555),
    ('G004', 'Anytime Fitness', 'London', 1111111111),
    ('G005', 'Planet Fitness', 'Sydney', 9999999999),
    ('G006', 'Snap Fitness', 'Toronto', 7777777777),
    ('G007', 'The Gym Group', 'Paris', 2222222222),
    ('G008', 'GoodLife Fitness', 'Vancouver', 8888888888),
    ('G009', 'PureGym', 'Berlin', 4444444444),
    ('G010', 'Equinox', 'Tokyo', 6666666666);



INSERT INTO Trainer (Trainer_id, Trainer_name, Trainer_gender, Trainer_mobile_number, Trainer_specialization, Trainer_gym_id)
VALUES 
    ('T001', 'John Doe', 'M', 1234567890, 'Strength Training', 'G001'),
    ('T002', 'Jane Smith', 'F', 9876543210, 'Yoga', 'G002'),
    ('T003', 'Mike Johnson', 'M', 5555555555, 'Cardio', 'G003'),
    ('T004', 'Emily Davis', 'F', 1111111111, 'Pilates', 'G004'),
    ('T005', 'David Lee', 'M', 9999999999, 'CrossFit', 'G005'),
    ('T006', 'Sarah Wilson', 'F', 7777777777, 'Zumba', 'G006'),
    ('T007', 'Daniel Brown', 'M', 2222222222, 'Kickboxing', 'G007'),
    ('T008', 'Jessica Adams', 'F', 8888888888, 'Functional Training', 'G008'),
    ('T009', 'Michael Taylor', 'M', 4444444444, 'Bodybuilding', 'G009'),
    ('T010', 'Sophia Anderson', 'F', 6666666666, 'Pilates', 'G010');

INSERT INTO Members (Members_id, Member_name, Member_date_of_birth, Member_email, Member_mobile_number, Member_gender, Member_Address, Member_gym_id)
VALUES 
    ('M011', 'Robert Johnson', '1990-05-15', 'robert@example.com', 1234567890, 'M', 'Laketown', 'G001'),
    ('M012', 'Jennifer Davis', '1985-10-20', 'jennifer@example.com', 9876543210, 'F', 'Elm St', 'G001'),
    ('M013', 'William Smith', '1992-03-25', 'william@example.com', 5555555555, 'M', 'Oak St', 'G002'),
    ('M014', 'Emma Brown', '1988-07-05', 'emma@example.com', 1111111111, 'F', 'PineSt', 'G002'),
    ('M015', 'James Wilson', '1987-12-10', 'james@example.com', 9999999999, 'M', 'MapleSt', 'G003'),
    ('M016', 'Sophia Adams', '1995-09-18', 'sophia@example.com', 7777777777, 'F', 'WalnutSt', 'G003'),
    ('M017', 'David Taylor', '1984-06-28', 'david@example.com', 2222222222, 'M', 'CedarSt', 'G004'),
    ('M018', 'Olivia Lee', '1998-02-02', 'olivia@example.com', 8888888888, 'F', 'BirchSt', 'G004'),
    ('M019', 'Ethan Wilson', '1991-11-11', 'ethan@example.com', 4444444444, 'M', 'OakSt', 'G005'),
    ('M020', 'Ava Johnson', '1989-08-08', 'ava@example.com', 6666666666, 'F', 'PineSt', 'G005');


INSERT INTO Equipment (Equipment_id, Equipment_name, Equipment_manufacturer, Equipment_age, Equipment_gym_id)
VALUES 
    ('E011', 'Treadmill', 'ABC Fitness', 2, 'G001'),
    ('E012', 'Dumbbells', 'XYZ Equipment', 1, 'G001'),
    ('E013', 'Stationary Bike', 'FitCorp', 3, 'G002'),
    ('E014', 'Leg Press Machine', 'GymTech', 5, 'G002'),
    ('E015', 'Elliptical Trainer', 'FitnessPro', 2, 'G003'),
    ('E016', 'Kettlebells', 'IronGrip', 1, 'G003'),
    ('E017', 'Bench Press', 'BodyBuilder', 4, 'G004'),
    ('E018', 'Resistance Bands', 'FlexFit', 2, 'G004'),
    ('E019', 'Rowing Machine', 'PowerFit', 3, 'G005'),
    ('E020', 'Yoga Mat', 'ZenFitness', 1, 'G005');


INSERT INTO Memberships (Membership_id, Membership_memberid, Membership_start_date, Membership_end_date, Membership_type)
VALUES 
    ('MS001', 'M011', '2023-01-01', '2023-06-30', 'Monthly'),
    ('MS002', 'M012', '2023-03-15', '2024-03-14', 'Annual'),
    ('MS003', 'M013', '2023-02-01', '2023-04-30', '3-Month'),
    ('MS004', 'M014', '2023-06-01', '2023-09-30', 'Seasonal'),
    ('MS005', 'M015', '2023-04-15', '2024-04-14', 'Annual'),
    ('MS006', 'M016', '2023-03-01', '2023-05-31', '3-Month'),
    ('MS007', 'M017', '2023-05-01', '2023-08-31', 'Seasonal'),
    ('MS008', 'M018', '2023-01-15', '2024-01-14', 'Annual'),
    ('MS009', 'M019', '2023-02-15', '2023-05-14', '3-Month'),
    ('MS010', 'M020', '2023-06-15', '2024-06-14', 'Annual');





