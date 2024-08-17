-- Question One 
--====================================================
SELECT
    FIRST_NAME
    ,LAST_NAME
    ,STREET_ADDRESS
FROM
    STUDENT;
    

-- Question Two 
--====================================================
SELECT COST FROM COURSE;
SELECT DISTINCT COST FROM COURSE;
-- DISTINCT is used within a SQL Statement to only show for unique/ non-duplicated records 


-- Question Three
--====================================================
 SELECT DESCRIPTION, COST FROM COURSE;
 SELECT DISTINCT DESCRIPTION, COST FROM COURSE;
 -- in this case,  the whole record returned in the query needs to be unique and although the cost is duplicated the description is not 
 -- thereofre the records 1 and 2  for example , whilst may have the same value in COST, do not hold the same value in DESCRIPTION, and therefore will be shown together.
 
 
 -- Question Four
--====================================================
SELECT DISTINCT
    GRADE_TYPE_CODE
FROM 
    GRADE;
    
    
 -- Question Five
--====================================================
-- 3 Instructors live at the zip code of 10015
SELECT 
    FIRST_NAME
    ,LAST_NAME
    ,ZIP
FROM
    INSTRUCTOR
WHERE
    ZIP = '10015';
    
    
 -- Question Six
--====================================================
SELECT 
    FIRST_NAME
    ,LAST_NAME
    ,STREET_ADDRESS
    ,ZIP
    ,PHONE
    ,EMPLOYER
FROM 
    STUDENT
WHERE
    ZIP = '07024'
    OR 
    employer = 'Amer.Legal Systems'
    
    
-- Question Seven 
--====================================================
SELECT 
    LAST_NAME
FROM
    STUDENT
WHERE
    ZIP IN ('10048','11102','11209')
    
    
-- Question Eight  - 2 Intructors
--====================================================
SELECT 
    FIRST_NAME
    ,LAST_NAME
FROM 
    INSTRUCTOR
WHERE 
    ZIP = '10015'
    AND 
        (FIRST_NAME LIKE '%R%'
            OR
        FIRST_NAME LIKE '%r%')
--2 Intructors


-- Question Nine 
--====================================================
SELECT 
    last_name
 FROM
    instructor
WHERE 
    created_date = modified_by;
    
--1) created_date is a Date Data Type
--2) Trying to applying a filter to a column, by using another column name, which will be an aeeror in itself
--3) ignoring the above two errors, if this was a string, it would need to be surroudnied in quotation marks in order to search within the columns values like 'modified_by'



-- Question Ten
--====================================================
SELECT course_no, cost
FROM course
WHERE cost BETWEEN 1500 AND 1000;
-- no results are returned as erroneous way to search between a range, should be lower then higher values 
SELECT course_no, cost
FROM course
WHERE cost BETWEEN 1000 AND 1500;
-- difference is that the second query produces results, as the rnage to search for has been entered correc


-- Question Eleven
--====================================================
SELECT 
    *
FROM 
    COURSE
WHERE 
    PREREQUISITE IS NULL;
    
    

-- Question Twelve
--====================================================
SELECT 
    *
FROM 
    COURSE
WHERE 
    PREREQUISITE IS NOT NULL
    AND
    COST < 1100;
    
    
-- Question Thirteen
--====================================================
SELECT 
    CITY
    ,ZIP
FROM 
    ZIPCODE
ORDER BY STATE DESC ;


-- Question Fourteen
--====================================================
SELECT 
    SALUTATION
    ,FIRST_NAME
    ,LAST_NAME
FROM 
    STUDENT
WHERE
    LAST_NAME = 'Grant'
ORDER BY SALUTATION DESC;


-- Question Fifteen - 206
--====================================================
SELECT student_id, last_name
FROM student
ORDER BY last_name;


-- Question Sixteen
--====================================================
SELECT 
    COURSE_NO
    ,DESCRIPTION
    ,COST
    ,CASE
        WHEN COST  1095 ThEN COST * 1.1
    ELSE COST
    END AS COST_INC_INCREASE 
        
FROM 
    COURSE;
    
-- a) 3 records will be affecged
-- b) new value will be 1204.5
    
    