--=======================================================================
-- DDL script used for Assignment 1 
-- of CONL705 - Database systems 
--=======================================================================

--=======================================================================
-- 1.0 - Drop all relevant tables, sequences and Indexes
--=======================================================================

DROP TABLE Equipment_Register   CASCADE CONSTRAINTS;
DROP TABLE Hardware_Register    CASCADE CONSTRAINTS;
DROP TABLE Software_Register    CASCADE CONSTRAINTS;
DROP TABLE Helpdesk_Operator    CASCADE CONSTRAINTS;
DROP TABLE Helpdesk_Specialist  CASCADE CONSTRAINTS;
DROP TABLE Call_Log             CASCADE CONSTRAINTS;
DROP TABLE Personnel_Register   CASCADE CONSTRAINTS;
DROP TABLE Problem_Register     CASCADE CONSTRAINTS;
DROP TABLE Problem_Type         CASCADE CONSTRAINTS;
DROP TABLE Subject_Area         CASCADE CONSTRAINTS;

DROP SEQUENCE personnelseq;    
DROP SEQUENCE hardwareseq;   
DROP SEQUENCE softwareseq;  
DROP SEQUENCE equipmentseq; 
DROP SEQUENCE operatorseq;
DROP SEQUENCE specialistseq;
DROP SEQUENCE callseq;
DROP SEQUENCE problemseq;
DROP SEQUENCE probtypeseq;
DROP SEQUENCE subjectseq;

DROP INDEX personnel_name_i;
DROP INDEX personnel_dept_i;
DROP INDEX call_personnel_i;
DROP INDEX problem_call_i;
DROP INDEX problem_status_i;

--=======================================================================
--=======================================================================
-- 2.0 - Create Sequences for all primary keys
--=======================================================================
CREATE SEQUENCE personnelseq    START WITH 1001     INCREMENT BY 1 MAXVALUE 2000;
CREATE SEQUENCE hardwareseq     START WITH 5001     INCREMENT BY 1 MAXVALUE 6000;
CREATE SEQUENCE softwareseq     START WITH 6001     INCREMENT BY 1 MAXVALUE 7000;
CREATE SEQUENCE equipmentseq    START WITH 8001     INCREMENT BY 1 MAXVALUE 9999;
CREATE SEQUENCE operatorseq     START WITH 101      INCREMENT BY 1 MAXVALUE 199 ;
CREATE SEQUENCE specialistseq   START WITH 901      INCREMENT BY 1 MAXVALUE 999;
CREATE SEQUENCE callseq         START WITH 200001   INCREMENT BY 1 MAXVALUE 500000;
CREATE SEQUENCE problemseq      START WITH 400001   INCREMENT BY 1 MAXVALUE 750000;
CREATE SEQUENCE probtypeseq     START WITH 35001    INCREMENT BY 1 MAXVALUE 36000;
CREATE SEQUENCE subjectseq      START WITH 65001    INCREMENT BY 1 MAXVALUE 66000;


--=======================================================================
-- 2.0 - Creates relevant tables
--=======================================================================
CREATE TABLE Personnel_Register 
(
    personnel_ID   NUMBER(4)       PRIMARY KEY,
    First_Name     VARCHAR2(30)    NOT NULL,
    Last_Name      VARCHAR2(30)    NOT NULL,
    Contact_No     CHAR(11)        NOT NULL UNIQUE,
    Email_Address  VARCHAR2(50)    NOT NULL UNIQUE,
    Job_Title      VARCHAR2(50)    NOT NULL,
    Department     VARCHAR2(50)    NOT NULL
);


CREATE TABLE Hardware_Register
(
   Hardware_ID              NUMBER  (4)     PRIMARY KEY,
   Hardware_Name            VARCHAR2(50)    NOT NULL,
   Hardware_Make            VARCHAR2(50)    NOT NULL,
   Hardware_Specification   VARCHAR2(200)   NOT NULL,
   Under_Warranty           VARCHAR2(3)     NOT NULL
);


CREATE TABLE Software_Register
(
   Software_ID              NUMBER  (4)     PRIMARY KEY,
   Software_Name            VARCHAR2(50)    NOT NULL UNIQUE,
   Software_Make            VARCHAR2(50)    NOT NULL,
   Software_Specification   VARCHAR2(200)   NOT NULL,
   License_Valid            VARCHAR2(3)
);


CREATE TABLE Equipment_Register
(
    Equipment_ID       NUMBER(4)    PRIMARY KEY,
    Computer_Serial_No CHAR(7)      NOT NULL UNIQUE, 
    Hardware_ID_1        NUMBER(4)    REFERENCES Hardware_Register (Hardware_ID) ON DELETE CASCADE,
    Hardware_ID_2        NUMBER(4)    REFERENCES Hardware_Register (Hardware_ID) ON DELETE CASCADE,
    Hardware_ID_3        NUMBER(4)    REFERENCES Hardware_Register (Hardware_ID) ON DELETE CASCADE,
    Software_ID_1        NUMBER(4)    REFERENCES Software_Register (Software_ID) ON DELETE SET NULL,
    Software_ID_2        NUMBER(4)    REFERENCES Software_Register (Software_ID) ON DELETE SET NULL,
    Software_ID_3        NUMBER(4)    REFERENCES Software_Register (Software_ID) ON DELETE SET NULL,
    Personnel_ID        NUMBER(4)    REFERENCES Personnel_Register(Personnel_ID)ON DELETE SET NULL
    --placeholder for primary composite key creation
);


CREATE TABLE Helpdesk_Operator
(
    Operator_ID     NUMBER(3) PRIMARY KEY,
    Personnel_ID    REFERENCES Personnel_Register (personnel_ID) ON DELETE SET NULL
);

CREATE TABLE Helpdesk_Specialist
(
    Specialist_ID           NUMBER(3) PRIMARY KEY,
    Personnel_ID            NUMBER(4) REFERENCES Personnel_Register(Personnel_ID) ON DELETE CASCADE
);

CREATE TABLE Call_Log
(
    Call_ID             NUMBER(6)       PRIMARY KEY,
    Operator_ID         NUMBER(3)       REFERENCES  Helpdesk_Operator(Operator_ID),
    Personnel_ID        NUMBER(4)       REFERENCES  Personnel_Register(Personnel_ID),
    Call_Started        DATE            DEFAULT     (SYSDATE),
    Call_Ended          DATE,     
    Computer_Serial_No  CHAR(7)         NOT NULL,
    Reason_For_Call     VARCHAR2(50)    NOT NULL,
    Call_Notes          VARCHAR2(100)           
);

CREATE TABLE Problem_Register
(
    Problem_ID              NUMBER(6)       PRIMARY KEY,
    Call_ID                 NUMBER(6)       REFERENCES          Call_Log (Call_ID),
    Specialist_ID           NUMBER(3)       REFERENCES          Helpdesk_Specialist(Specialist_ID),
    Problem_Description     VARCHAR2(100),
    Problem_Created_Date    DATE            DEFAULT(SYSDATE),
    Problem_Ended_Date      DATE,
    Problem_Status          VARCHAR2(10)    NOT NULL,
    Resolutions_Notes       VARCHAR2(100)
);

CREATE TABLE Problem_Type
(
    ProblemType_ID          NUMBER(5)        PRIMARY KEY,
    ProblemType_Desc        VARCHAR2(100),   
    Equipment_Type          VARCHAR2(30)     NOT NULL,
    Parent_ProblemType_ID   NUMBER(5)        REFERENCES Problem_Type(ProblemType_ID)
);

CREATE TABLE Subject_Area
(
    Subject_Area_ID NUMBER(5) PRIMARY KEY,
    Subject_Name VARCHAR2(30) NOT NULL UNIQUE,
    Subject_Description VARCHAR2(100),
    ProblemType_1 NUMBER(5) REFERENCES  Problem_Type(ProblemType_ID),
    ProblemType_2 NUMBER(5) REFERENCES  Problem_Type(ProblemType_ID),
    ProblemType_3 NUMBER(5) REFERENCES  Problem_Type(ProblemType_ID)
);
--=======================================================================
--=======================================================================
-- 3.0 Alter tables to add relevant columns, now that the tables have been created togther 
--=======================================================================
ALTER TABLE Helpdesk_Specialist ADD Subject_Area_1 NUMBER(5) REFERENCES Subject_Area(Subject_Area_ID);
ALTER TABLE Helpdesk_Specialist ADD Subject_Area_2 NUMBER(5) REFERENCES Subject_Area(Subject_Area_ID);
ALTER TABLE Helpdesk_Specialist ADD Subject_Area_3 NUMBER(5) REFERENCES Subject_Area(Subject_Area_ID);


ALTER TABLE Call_Log ADD Problem_ID NUMBER(6) REFERENCES Problem_Register(Problem_ID);


ALTER TABLE Problem_Register ADD ProblemType_ID NUMBER(5) REFERENCES Problem_Type(ProblemType_ID);


ALTER TABLE Problem_Type ADD Subject_Area_ID  NUMBER(5) REFERENCES Subject_Area(Subject_Area_ID);





