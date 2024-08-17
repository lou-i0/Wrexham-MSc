/*
--q1
SELECT 
    A.FIRST_NAME
    ,A.LAST_NAME
    ,B.CITY
    ,B.STATE
    ,B.ZIP
FROM 
    INSTRUCTOR A
INNER JOIN 
    ZIPCODE B 
    ON A.ZIP = B.ZIP
    
ORDER BY B.ZIP DESC ;



--q2
SELECT
    a.student_id,
    a.first_name,
    a.last_name
    ,b.section_id   
    ,b.enroll_date
    ,b.final_grade
FROM
    student a 
INNER JOIN 
    ENROLLMENT b
    ON  a.STUDENT_ID = b.STUDENT_ID
    
ORDER BY a.last_name, b.section_id ASC;
    
--q3
SELECT 
    a.description   
    ,a.cost
    ,b.section_no
    ,b.start_date_time
FROM
    COURSE a
LEFT JOIN
    SECTION b
    ON a.course_no = b.course_no
WHERE
    b.location = 'L211'
    
  
--q4
SELECT
    a.instructor_id, 
    a.first_name,
    a.last_name
    ,b.section_no
    ,b.start_date_time
    ,b.location
    
FROM
    instructor a
INNER JOIN 
    section b
    ON a.INSTRUCTOR_ID = b.INSTRUCTOR_ID
    
ORDER BY a.last_name, b.start_date_time, b.section_no;

*/
--q5
SELECT 
    a.section_id,
    a.section_no,
    a.location,
    a.capacity
    ,b.final_grade

FROM
    section a
INNER JOIN 
   ENROLLMENT b
   ON a.SECTION_ID = b.section_id
WHERE
    b.final_grade between 40 and 80
;