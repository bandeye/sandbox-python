#api.feature
Feature: API tests

    Scenario: User should get a random Chuck norris Joke.
        Given The API endpoint is "https://api.chucknorris.io/jokes/random"
        When A GET request is made
        Then The response status code should be 200
        And The response should contain "value"