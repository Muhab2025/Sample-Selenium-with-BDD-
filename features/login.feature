
Feature: Login Feature

    Background: common steps
        Given I navigate to Login page

    @login
    Scenario Outline: Login with valid credentials
        When I enter a valid username as "<email>" and a valid password as "<password>" into the fields
        And I click on Login button
        Then I should get logged in my account page
        Examples:
            |email                           |password    |
            |mohabda19@yahoo.com             |123456      | 
            |my_first_username@gmail.com	 |1234567890  |
            |my_second_username@gmail.com	 |2345678901  |
            |my_third_username@gmail.com	 |3456789012  |


    @login
    Scenario: Login with an invalid username and valid password 
        When I enter an invalid username and a valid password as "123456" into the fields
        And I click on Login button
        Then I should get an appropriate warning message

    @login
    Scenario: Login with a valid username and an invalid password
        When I enter a valid username as "mohabda19@yahoo.com" and an invalid password as "1234567890" into the fields
        And I click on Login button
        Then I should get an appropriate warning message

    @login
    Scenario: Login with an invalid credentials
        When I enter an invalid username and an invalid password as "123" into the fields
        And I click on Login button
        Then I should get an appropriate warning message

    @login
    Scenario: Login without entering any credentials
        When I do not enter any credentials into the fields
        And I click on Login button
        Then I should get an appropriate warning message

