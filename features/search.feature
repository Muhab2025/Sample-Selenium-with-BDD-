Feature: Search Function

    Background: common steps
        Given I am on the Application Homepage

    @implemented @search
    Scenario: Search for a valid product
        When I enter a valid product say "HP" into search box field
        And I click on Search button
        Then Valid products should be displayed on search results page

    @smoke @implemented @search
    Scenario: Search for an invalid product
        When I enter an invalid product say "HONDA" into search box field
        And I click on Search button
        Then Appropriate message should be displayed on search results page

    @smoke @implemented @search
    Scenario: Search without entering any product
        When I do not enter any product into search box field
        And I click on Search button
        Then Appropriate message should be displayed on search results page