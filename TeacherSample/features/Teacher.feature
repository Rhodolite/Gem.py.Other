Feature: A complete Semester

    Scenario: Alice's Math class
      Given a unique set of choices, courses, quizes, students and teachers
        | type    | name    | number | parent    | correct | text                       |
        | Teacher | Alice   | 1      | .         | .       | .                          |
        | Student | Bob     | 2      | .         | .       | .                          |
        | Student | Charlie | 3      | .         | .       | .                          |
        | Student | David   | 4      | .         | .       | .                          |
        | Teacher | Eve     | 5      | .         | .       | .                          |
        | Course  | Math    | 1      | Alice     | .       | .                          |
        | Quiz    | Simple  | 1.1    | Math      | .       | .                          |
        | Question| .       | 1.1.1  | .         | .       | What is 1+1?               |
        | Choice  | .       | 1.1.1A | .         | No      | One                        |
        | Choice  | .       | 1.1.1B | .         | Yes     | Two                        |
        | Choice  | .       | 1.1.1C | .         | No      | Three                      |
        | Question| .       | 1.1.2  | .         | .       | What is 2-2?               |
        | Choice  | .       | 1.1.2A | .         | Yes     | Zero                       |
        | Choice  | .       | 1.1.2B | .         | No      | One                        |
        | Choice  | .       | 1.1.2C | .         | No      | Two                        |
        | Question| .       | 1.1.3  | .         | .       | What is 3 multiplied by 3? |
        | Choice  | .       | 1.1.3A | .         | No      | Zero                       |
        | Choice  | .       | 1.1.3B | .         | No      | Three                      |
        | Choice  | .       | 1.1.3C | .         | No      | Six                        |
        | Choice  | .       | 1.1.3D | .         | Yes     | Nine                       |
        | Question| .       | 1.1.4  | .         | .       | What is 4 modulus 4?       |
        | Choice  | .       | 1.1.4A | .         | Yes     | Zero                       |
        | Choice  | .       | 1.1.4B | .         | No      | One                        |
        | Choice  | .       | 1.1.4C | .         | No      | Four                       |
    When students join courses
        | student | course |
        | Bob     | Math   |
        | Charlie | Math   |
        | David   | Math   |
    And  students learn facts
        | student | correct | question_text | choice_text |
        | Bob     | Yes     | What is 1+1?  | Two         |
    And  students learn more facts
        | student | correct | question_text              | choice_text |
        | Bob     | No      | What is 3 multiplied by 3? | Six         |
        | Bob     | Yes     | What is 2-2?               | Zero        |
    And  teachers gives quizzes
        | teacher | course | name   | number |
        | Alice   | Math   | Simple | 1.1    |
    And  students answer questions
        | student |
        | Bob     |
    Then students get their quiz grades
        | student | course | name   | number | grade |
        | Bob     | Math   | Simple | 1.1    | 50    |
    When teachers create more quizzes
        | type    | name    | number | parent    | correct | text                        |
        | Quiz    | Final   | 1.2    | Math      | .       | .                           |
        | Question| .       | 1.2.1  | .         | .       | What is 4 modulus 4?        |
        | Choice  | .       | 1.2.1A | .         | Yes     | Zero                        |
        | Choice  | .       | 1.2.1B | .         | No      | Four                        |
        | Question| .       | 1.2.2  | .         | .       | What is 5 to the 5th power? |
        | Choice  | .       | 1.2.2A | .         | No      | Five                        |
        | Choice  | .       | 1.2.2B | .         | No      | 25                          |
        | Choice  | .       | 1.2.2C | .         | No      | 125                         |
        | Choice  | .       | 1.2.2D | .         | No      | 625                         |
        | Choice  | .       | 1.2.2E | .         | Yes     | 3125                        |
        | Choice  | .       | 1.2.2F | .         | No      | 15625                       |
    And  teachers gives more quizzes
        | teacher | course | name   | number |
        | Alice   | Math   | Final  | 1.2    |
    And  students learn more facts, including facts on PREVIOUS tests
        | student | correct | question_text               | choice_text |
        | Bob     | Yes     | What is 4 modulus 4?        | Zero        |
        | Bob     | Yes     | What is 5 to the 5th power? | 3125        |
    And  students answer questions
        | student |
        | Bob     |
    Then students get their quiz grades, including IMPROVED grades on previous quizzes
        | student | course | name   | number | grade |
        | Bob     | Math   | Simple | 1.1    | 75    |
        | Bob     | Math   | Final  | 1.2    | 100   |
    And  students get their course grades
        | student | course | grade |
        | Bob     | Math   | 88    |
    When teachers create more courses and quizzes
        | type    | name      | number | parent    | correct | text                                      |
        | Course  | Geography | 2      | Alice     | .       | .                                         |
        | Quiz    | Simple    | 2.1    | Geography | .       | .                                         |
        | Question| .         | 2.1.1  | .         | .       | How many states are in the United States? |
        | Choice  | .         | 2.1.1A | .         | No      | 13                                        |
        | Choice  | .         | 2.1.1B | .         | Yes     | 50                                        |
        | Choice  | .         | 2.1.1C | .         | No      | 51                                        |
        | Quiz    | Final     | 2.2    | Geography | .       | .                                         |
        | Question| .         | 2.2.1  | .         | .       | What is the capital of New York?          |
        | Choice  | .         | 2.2.1A | .         | Yes     | New York                                  |
        | Choice  | .         | 2.2.1B | .         | No      | Madison                                   |
        | Question| .         | 2.2.2  | .         | .       | What is the capital of the United States? |
        | Choice  | .         | 2.2.2A | .         | No      | New York                                  |
        | Choice  | .         | 2.2.2B | .         | No      | Olympia                                   |
        | Choice  | .         | 2.2.2C | .         | Yes     | Washington, D.C.                          |
        | Question| .         | 2.2.3  | .         | .       | What is the capital of Washington?        |
        | Choice  | .         | 2.2.3A | .         | No      | Madison                                   |
        | Choice  | .         | 2.2.3B | .         | No      | New York                                  |
        | Choice  | .         | 2.2.3C | .         | Yes     | Olympia                                   |
        | Choice  | .         | 2.2.3D | .         | No      | Washington, D.C.                          |
        | Course  | Jogging   | 3      | Eve       | .       | .                                         |
        | Course  | Jumping   | 4      | Eve       | .       | .                                         |
        | Quiz    | Empty     | 4.1    | Jumping   | .       | .                                         |
        | Course  | Swimming  | 5      | Eve       | .       | .                                         |
        | Quiz    | Easy      | 5.1    | Swimming  | .       | .                                         |
        | Question| .         | 5.1.1  | .         | .       | Do we use chlorine in our swimming pool?  |
        | Choice  | .         | 5.1.1A | .         | Yes     | Yes                                       |
        | Choice  | .         | 5.1.1B | .         | No      | No                                        |
    And  students join courses
        | student | course    |
        | Bob     | Geography |
        | Bob     | Jogging   |
        | Bob     | Jumping   |
        | Bob     | Swimming  |
        | Charlie | Geography |
    And  students learn facts
        | student | correct | question_text                             | choice_text      |
        | Bob     | No      | How many states are in the United States? | 51               |
        | Bob     | Yes     | What is the capital of New York?          | New York         |
        | Bob     | Yes     | What is the capital of the United States? | Washington, D.C. |
        | Bob     | Yes     | What is the capital of Washington?        | Olympia          |
        | Bob     | Yes     | Do we use chlorine in our swimming pool?  | Yes              |
    And  teachers gives quizzes
        | teacher | course    | name   | number |
        | Alice   | Geography | Simple | 2.1    |
        | Alice   | Geography | Final  | 2.2    |
        | Eve     | Jumping   | Empty  | 4.1    |
        | Eve     | Swimming  | Easy   | 5.1    |
    And  students answer questions
        | student |
        | Bob     |
    Then students get their quiz grades
        | student | course    | name   | number | grade |
        | Bob     | Math      | Simple | 1.1    | 75    |
        | Bob     | Math      | Final  | 1.2    | 100   |
        | Bob     | Geography | Simple | 2.1    | 0     |
        | Bob     | Geography | Final  | 2.2    | 100   |
        | Bob     | Jumping   | Empty  | 4.1    | 100   |
        | Bob     | Swimming  | Easy   | 5.1    | 100   |
    And  students get their course grades
        | student | course    | grade |
        | Bob     | Geography | 50    |
        | Bob     | Math      | 88    |
        | Bob     | Jogging   | 100   |
        | Bob     | Jumping   | 100   |
        | Bob     | Swimming  | 100   |
    And  students get their semester grades, for a particular teacher
        | student | teacher   | grade |
        | Bob     | Alice     | 69    |
        | Bob     | Eve       | 100   |
    When other students learn facts
        | student | correct | question_text                             | choice_text |
        | Charlie | Yes     | What is 1+1?                              | Two         |
        | Charlie | Yes     | What is 2-2?                              | Zero        |
        | Charlie | Yes     | What is 3 multiplied by 3?                | Nine        |
        | Charlie | Yes     | What is 4 modulus 4?                      | Zero        |
        | Charlie | Yes     | What is 5 to the 5th power?               | 3125        |
        | David   | Yes     | What is 1+1?                              | Two         |
        | David   | Yes     | What is 2-2?                              | Zero        |
        | David   | Yes     | What is 3 multiplied by 3?                | Nine        |
        | David   | Yes     | What is 4 modulus 4?                      | Zero        |
        | David   | Yes     | What is 5 to the 5th power?               | 3125        |
        | Charlie | No      | How many states are in the United States? | 51          |
        | Charlie | Yes     | What is the capital of New York?          | New York    |
        | David   | Yes     | What is the capital of New York?          | New York    |
    And  students answer questions
        | student |
        | Charlie |
        | David   |
    Then students get their quiz grades
        | student | course    | name   | number | grade |
        | Bob     | Math      | Simple | 1.1    | 75    |
        | Bob     | Math      | Final  | 1.2    | 100   |
        | Bob     | Geography | Simple | 2.1    | 0     |
        | Bob     | Geography | Final  | 2.2    | 100   |
        | Charlie | Math      | Simple | 1.1    | 100   |
        | Charlie | Math      | Final  | 1.2    | 100   |
        | David   | Math      | Simple | 1.1    | 100   |
        | David   | Math      | Final  | 1.2    | 100   |
        | Charlie | Geography | Simple | 2.1    | 0     |
        | Charlie | Geography | Final  | 2.2    | 33    |
    And  students get their course grades
        | student | course    | grade |
        | Bob     | Geography | 50    |
        | Bob     | Math      | 88    |
        | Bob     | Jogging   | 100   |
        | Bob     | Jumping   | 100   |
        | Bob     | Swimming  | 100   |
        | Charlie | Math      | 100   |
        | Charlie | Geography | 17    |
        | David   | Math      | 100   |
    And  students get their semester grades, for a particular teacher
        | student | teacher   | grade |
        | Bob     | Alice     | 69    |
        | Bob     | Eve       | 100   |
        | Charlie | Alice     | 59    |
        | David   | Alice     | 100   |
