Feature: Cannot create two courses with the same name

    Scenario: two teachers both try to teach a math course
      Given <Alice> is teaching a <Math> course
      When  <Bob> attempts to also teach a <Math> course
      Then  an error is thrown
