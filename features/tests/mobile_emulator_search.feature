# Created by shaha at 5/4/2023
Feature: Search functionality test cases for mobile emulator

  Scenario: User can search product based on given categories from given mobile capabilities
    Given Click the main menu
    When click on shop icon on main menu shown on the mobile screen
    When click on the product body category on mobile screen
    Then verify result for body category is shown on mobile screen