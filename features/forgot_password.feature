Feature: Forgot password functionality

  Scenario: User requests a password reset
    Given I am on the login page
    When I click on the forgot password link
    And I enter my email address
    And I click on the submit button
    Then I should see "A password reset link has been sent to your email."
