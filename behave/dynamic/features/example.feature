Feature: TEST WWW HTTP Endpoint

  In the following tests I want to ensure that when connecting to the www http endpoint:
  1) TBC
  2) TBC

  Background: APP WWW HTTP Endpoint Tests

  @dynamic
  Scenario Outline: APP <Envs> WWW HTTP Endpoint - Accepted Request with TBC
    Given TBC "<Envs>"
    And TBC "TEST"
    When TBC
    Then TBC

    Examples: Envs
      | Envs |
      |   .  |

  @dynamic
  Scenario Outline: APP <Envs> WWW HTTP Endpoint - Blocked Request without TBC
    Given TBC "<Envs>"
    And TBC
    When TBC
    Then TBC

    Examples: Envs
      | Envs |
      |   .  |
