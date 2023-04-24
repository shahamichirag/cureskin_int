# Created by shaha at 4/21/2023
Feature: Search functionality test cases

  Scenario: User can search product based on given categories
    Given open main page
    When click on shop by category on main page
    And click on the product category "body"
    Then verify result for "body" category is shown