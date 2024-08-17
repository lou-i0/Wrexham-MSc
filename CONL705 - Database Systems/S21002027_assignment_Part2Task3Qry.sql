--Select Queries  
--==========================================================================
--1.	List the details of equipment and associated software.  
--==========================================================================
SELECT
    eqp.equipment_id
    ,eqp.computer_serial_no
    ,eqp.software_id_1
    ,sft_1.software_name AS Software_ID_1_Name
    ,eqp.software_id_2
    ,sft_2.software_name AS Software_ID_2_Name
    ,eqp.software_id_3
    ,sft_3.software_name AS Software_ID_3_Name   
FROM 
    equipment_register eqp
LEFT JOIN
    software_register sft_1
    ON eqp.software_id_1 = sft_1.software_id
LEFT JOIN
    software_register sft_2
    ON eqp.software_id_2 = sft_2.software_id
LEFT JOIN
    software_register sft_3
    ON eqp.software_id_3 = sft_3.software_id;
    

--==========================================================================
--2. Produce a list of experts (support staff) for a given problem area 
--==========================================================================
SELECT 
    spe.specialist_id
    ,sub.subject_area_id
    ,sub.subject_name
    ,sub.subject_description
    ,sub.problemtype_1
    ,sub.problemtype_2
    ,sub.problemtype_3
FROM 
    helpdesk_specialist spe
LEFT JOIN
    subject_area sub
    ON spe.subject_area_1 = sub.subject_area_id
WHERE 
    sub.subject_area_id = 65002;
--==========================================================================
--3. Produce a list of all unresolved problems with the assigned Specialist 
--==========================================================================
SELECT 
    * 
FROM 
    problem_register
WHERE
    specialist_id = 903
AND 
    problem_status IN ('Open','On-hold');
--==========================================================================
--4. Produce a list of problems reported by a member of staff, the details of 
--the support staff who attended the problem and the solution provided by 
--the support staff  
--==========================================================================
SELECT 
    call.call_id
    ,call.personnel_id
    ,call.reason_for_call
    ,call.call_notes
    ,call.operator_id
    ,pro.problem_id
    ,pro.specialist_id
    ,pro.problem_status
    ,pro.resolutions_notes
    
FROM
    call_log call
LEFT JOIN
    problem_register pro
    ON call.problem_id = pro.problem_id
WHERE 
    call.personnel_id = 1044
AND 
    pro.problem_status = 'Closed';

--==========================================================================
--5. Find (display) the average time taken fix fault for a given problem area.
--==========================================================================
SELECT
    pro.problem_id
    ,AVG(pro.problem_ended_date - pro.problem_created_date) AS average_time_to_fix_days
FROM 
    problem_register pro
WHERE 
    pro.problemtype_id = 35014
GROUP BY
    pro.problem_id;
--==========================================================================
--6. Display a list of the most common problems and order them in according 
--to the frequency of their occurrence.  
--==========================================================================
SELECT
   pro.problemtype_id
   ,COUNT(*) as Frequency
   ,pty.problemtype_desc
FROM
    problem_register pro
LEFT JOIN
    problem_type pty 
    ON pro.problemtype_id = pty.problemtype_id
GROUP BY
    pro.problemtype_id
    ,pty.problemtype_desc
ORDER BY 
    COUNT(*) DESC;

--==========================================================================
--7. Display the equipment with the most reported problems showing problem details  
--==========================================================================
WITH  most_personnel_calls AS 
(
    SELECT 
        COUNT(*) AS call_frequency
        ,personnel_ID 
    FROM
        call_log 
    WHERE
        problem_id IS NOT NULL 
    GROUP BY 
        personnel_id
    ORDER BY 
        COUNT(*) DESC
    FETCH FIRST 1 ROWS ONLY
)
SELECT 
    mpc.personnel_id
    ,call.call_id
    ,call.operator_id
    ,call.call_started
    ,call.call_ended
    ,call.reason_for_call
    ,call.call_notes
    ,pro.problem_id
    ,pro.specialist_id
    ,pro.problem_description
    ,pro.problem_created_date
    ,pro.problem_ended_Date
    ,pro.problem_status
    ,pro.resolutions_notes
    ,pro.problemtype_ID
    ,eqp.equipment_id
    ,eqp.computer_serial_no
    ,eqp.hardware_id_1
    ,eqp.hardware_id_2
    ,eqp.hardware_id_3
    ,eqp.software_id_1
    ,eqp.software_id_2
    ,eqp.software_id_3
    
FROM
    most_personnel_calls mpc
LEFT JOIN 
    call_log call 
    ON mpc.personnel_id = call.personnel_id
LEFT JOIN
    problem_register pro
    ON call.problem_id = pro.problem_id
LEFT JOIN 
    equipment_register eqp
    ON mpc.personnel_id = eqp.personnel_id;
    
--==========================================================================
--8. Produce a list of problems that have been solved by helpdesk operator 
--==========================================================================
SELECT 
    call.call_id
    ,call.personnel_ID
    ,call.computer_serial_no
    ,call.reason_for_call
    ,call.call_notes
    ,pro.problem_id
    ,pro.problem_description
    ,call.operator_id
    ,pro.specialist_id
FROM 
    call_log call
LEFT JOIN
    problem_register pro
    ON call.problem_id = pro.problem_id
WHERE 
    call.problem_id IS NOT NULL
AND 
    pro.specialist_id IS NULL;

--==========================================================================
--9. Add a new Specialist to the database 
--==========================================================================
INSERT INTO Personnel_Register VALUES(personnelseq.NEXTVAL,'Terrence','Anderson','07892225879','terrance.anderson@premierproducts.co.uk','Helpdesk Specialist','IT Operations');
INSERT INTO Helpdesk_Specialist VALUES (specialistseq.NEXTVAL,personnelseq.CURRVAL,65003,65001,65002);

--==========================================================================
--10. Assign a specialist for a given problem (it must be an unresolved, 
--unassigned and should find a matching Specialist) 
--==========================================================================   
UPDATE 
    problem_register 
SET
    specialist_id = 905
WHERE 
    problem_id = 400006;


--==========================================================================
--11. Update the Call-log with appropriate details when the problem has been 
--resolved.
--==========================================================================
UPDATE 
    call_log
SET 
    reason_for_call = 'Personnel recently started, issue with equipment'
    ,call_notes = 'personnel just started company. Struggling to install new software onto laptop based on notes provided.'
WHERE 
    call_id  = 200094
AND 
    problem_id = 400006;
    
UPDATE 
    problem_register
SET
   problem_status = 'Closed'
   ,resolutions_notes = 'Spoke with personnel. Documentation incorrect; now updated and managed to self install software.'
WHERE 
    call_id  = 200094
AND 
    problem_id = 400006;
    

--==========================================================================
--12. An item of Equipment which, has previously had a fault reported, has 
--now become redundant so Delete it from the database.  
--==========================================================================
DELETE FROM hardware_register WHERE hardware_id = 5004;
