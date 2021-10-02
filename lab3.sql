create database university;
-- run queries in lab3_dml.sql and lab3_ddl.sql files
-- TASK 1
-- a
select * from course where credits>3;
-- b
select * from classroom where building='Watson' or building='Packard';
-- c
select * from course where dept_name='Comp. Sci.';
-- d
select course.course_id,course.title,course.dept_name,course.credits from course,section
    where course.course_id=section.course_id and section.semester='Fall';
-- e
select * from student where tot_cred between 45 and 90;
-- f
select * from student where name like '%a' or name like '%o' or name like '%y' or name like '%i' or name like '%e' or name like '%u';
-- g
select course.course_id,course.title,course.dept_name,course.credits from prereq,course
    where course.course_id=prereq.course_id and prereq.prereq_id='CS-101';
-- TASK 2
-- a
select department.dept_name ,avg(instructor.salary) as avg_salary from department,instructor
    where department.dept_name=instructor.dept_name
    group by department.dept_name
    order by avg(instructor.salary) asc;
-- b
select department.building,count(course.course_id) as max_course from department,course
    where course.dept_name=department.dept_name
    group by department.building
    order by max_course desc limit 1;
-- c
select department.dept_name,count(course.course_id) as course from department,course
    where course.dept_name=department.dept_name
    group by department.dept_name
    order by course asc limit 1;
-- d
select res.id,res.name
    from(select student.id,student.name,count(course.dept_name) as cnt from student,takes,course
    where takes.id=student.id and takes.course_id=course.course_id and course.dept_name='Comp. Sci.'
    group by student.id) as res
    where cnt>3;
-- e
select * from instructor
    where dept_name in ('Biology','Music','Philosophy');
-- f
(select instructor.id,instructor.name,instructor.dept_name,instructor.salary from teaches,instructor
    where teaches.id=instructor.id and teaches.year=2018) except
(select instructor.id,instructor.name,instructor.dept_name,instructor.salary from teaches,instructor
    where teaches.id=instructor.id and teaches.year=2017);
-- TASK 3
-- a
select student.id,student.name,student.dept_name,student.tot_cred from takes,course,student
    where takes.course_id=course.course_id and course.dept_name='Comp. Sci.' and takes.grade in ('A','A-') and takes.id=student.id
    order by student.name;
-- b
select distinct instructor.name,instructor.id, student.name,student.id,takes.grade from takes,instructor,teaches,student,advisor
    where takes.grade not in ('A','A-','B','B+') and advisor.i_id=instructor.id and takes.id=advisor.s_id and advisor.s_id=student.id;
-- c
(select student.dept_name from student,takes
    where student.id=takes.id and takes.grade not in ('C','C+','C-','F')) except
(select student.dept_name from student,takes
    where student.id=takes.id and takes.grade in ('C','C+','C-','F'));
-- d
select * from teaches;
(select instructor.id,instructor.name from teaches,takes,instructor
    where teaches.course_id=takes.course_id and takes.grade not in ('A','A-') and instructor.id=teaches.id) except
(select instructor.id,instructor.name from teaches,takes,instructor
    where teaches.course_id=takes.course_id and takes.grade in ('A','A-') and instructor.id=teaches.id);
-- e
select course.course_id,course.title,time_slot.day,time_slot.end_hr,time_slot.end_min from section,time_slot,course
    where time_slot.time_slot_id=section.time_slot_id and time_slot.end_hr<13 and course.course_id=section.course_id;



