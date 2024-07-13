Feature: Login functionality

  Scenario Outline: User logs in with different credentials
    Given I am on the login page
    When I enter <username> and <password>
    And I click on the login button
    Then I should see <message>

    Examples:
      | username      | password        | message                        |
      | valid_user    | valid_password  | Homepage                       |
      | invalid_user  | invalid_password| Invalid username or password.  |
      | locked_user   | locked_password | Your account is locked.        |
