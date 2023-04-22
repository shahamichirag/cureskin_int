# Created by shaha at 4/21/2023
Feature: Search functionality test cases

  Scenario: User can search product based on given categories
    Given open main page
    When click on "shop by category"
    And click on "Body"
    Then verify "Body" header is shown