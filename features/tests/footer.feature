# Created by shaha at 4/26/2023
Feature: Shop page footer fuctionality test cases

  Scenario: verify the Email field located at the shop page footer
    Given open main page
    When go to the email field located at the footer of the shop page
    And enter a valid email email@g.mail and hit the submit button
    And verify successful subscription
    And enter an invalid email emailgmail.com and hit the submit button
    Then verify unsuccessful attempt of subscription