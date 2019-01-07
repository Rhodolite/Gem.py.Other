Feature: Numbers can be used to uniquely identifer courses, students, and teachers

    Scenario: Unique person numbers
      Given a unique set of students and teachers
        | type    | name    | number |
        | Teacher | Alice   | 1      |
        | Teacher | Bob     | 2      |
        | Student | Charlie | 3      |
        | Student | David   | 4      |
      When other students or teachers attempt to use the same number
        | type    | name    | number |
        | Teacher | Eve     | 1      |
        | Student | Fred    | 2      |
        | Teacher | Gail    | 3      |
        | Student | Harry   | 4      |
      Then <4> errors are thrown

    Scenario: Invalid person type
      Given a set of people that includes a <Cook> instead of all students and teachers
        | type      | name    | number |
        | Student   | Alice   | 1      |
        | Teacher   | Bob     | 2      |
        | Cook      | Charlie | 3      |
        | Janitor   | David   | 4      |
      Then an error is thrown

    Scenario: A course can share the same unique number with a student or teacher
      Given a unique set of students and teachers
        | type    | name      | number |
        | Teacher | Alice     | 1      |
        | Student | Bob       | 2      |
        | Student | Charlie   | 3      |
        | Student | David     | 4      |
        | Teacher | Eve       | 5      |
      Then a unique set of courses can be created, using the same numbers assigned to the students or teacher
        | type    | name      | number | parent  |
        | Course  | Math      | 1      | Alice   |
        | Course  | Geography | 2      | Alice   |
        | Course  | Jogging   | 3      | Eve     |
        | Course  | Jumping   | 4      | Eve     |
        | Course  | Swimming  | 5      | Eve     |
