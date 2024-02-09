Feature: TEST WWW HTTP Endpoint

  In the following test I want to ensure that when connecting to the defined http endpoint:
  * We receive an HTTP response code 200

  Background: HTTP Endpoint Tests

  Scenario: HTTP Endpoint - Test For 200 Response Code
    Given the HTTP endpoint has been defined
    When we connect to the HTTP endpoint
    Then we get the response code "200"
