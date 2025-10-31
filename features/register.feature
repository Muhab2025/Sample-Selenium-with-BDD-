Feature: Register Functionality

    Background: common steps
        Given I navigate to register page

    @smoke @register
    Scenario: Register with mandatory fields 
        When I enter below data in all mandatory fields
            |first_name     |last_name      |telephone    |password     |
            |my_first_name  |my_last_name   |1234567890   |123456       | 
        And I click on Continue button
        Then I should be redirected to Account Success Page

    @smoke @register
    Scenario: Register with all fields 
        When I enter below data in all fields
            |first_name     |last_name      |telephone    |password     |
            |my_first_name  |my_last_name   |1234567890   |123456       | 
        And I click on Continue button
        Then I should be redirected to Account Success Page

    @smoke @register
    Scenario: Register with duplicate email address 
        When I enter an existing email address
            |first_name     |last_name      |e-mail                |telephone    |password     |
            |my_first_name  |my_last_name   |mohabda19@yahoo.com   |1234567890   |123456       |  
        And I click on Continue button
        Then Appropriate warning message should be displayed

    @smoke @register
    Scenario: Register without enetring any data in the fields 
        When I do not enter any data in the fields
        And I click on Continue button
        Then Appropriate warning messages should be displayed