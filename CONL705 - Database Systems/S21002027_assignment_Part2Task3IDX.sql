--============================================
--Create Indexes
--============================================
  
CREATE INDEX personnel_name_i
ON Personnel_Register(Last_Name,First_Name);

CREATE INDEX personnel_dept_i
ON Personnel_Register(Department,Job_Title);

CREATE INDEX call_personnel_i
ON Call_Log(Personnel_ID,Operator_ID);

CREATE INDEX problem_call_i
ON Problem_Register(Call_ID);

CREATE INDEX problem_status_i
ON Problem_Register(Problem_Status);


