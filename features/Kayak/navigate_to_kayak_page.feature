@regression_tests
Feature: Validate element created dropdown column

  Scenario: Navigate to the Kayak home page and validate principal elements
    Given I navigate to the kayak main page
    Then I should be in the "home" page
    And The page "should" contain the next elements
      | name                 | type   |
      | name_tag             | input  |
      | name_dropdown_column | input  |
#      | search_tag             | input  |
      | cancel               | button |
#      | create_column_disabled | button |

  Scenario: Validate URL of Home page
    Given I navigate to the kayak main page
    Then I should be in the "home" page
    And The url page should be equal to the next "https://www.kayak.com.co/" url

  Scenario Outline: Navigate between countries and validate the URL
    Given I navigate to the kayak main page
    Then I should be in the "home" page
    When I navigate to the "<url>" URL
    Then The url page should be equal to the next "<url>" url

    Examples:
      | url                       |
      | https://www.kayak.com.my/ |
      | https://www.kayak.com.pr/ |
      | https://www.kayak.com.br/ |

  @menuOptions
  Scenario Outline: Navigate each of the right menu options and validate the URL
    Given I navigate to the kayak main page
    When I navigate each of the right menu "<option>"
    Then The url page should be equal to the next "<url>" url

    Examples:
      | option             | url                                                   |
      | Vuelos             | https://www.kayak.com.co/flights                      |
      | Alojamientos       | https://www.kayak.com.co/stays                        |
      | Carros             | https://www.kayak.com.co/cars                         |
      | Paquetes           | https://www.kayak.com.co/citybreaks                   |
      | Explore            | https://www.kayak.com.co/explore/                     |
      | Blog               | https://www.kayak.com.co/news/                        |
      | Vuelos directos    | https://www.kayak.com.co/direct                       |
      | El mejor momento   | https://www.kayak.com.co/el-mejor-momento-para-viajar |
      | KAYAK for Business | https://www.kayak.com.co/business                     |
      | Trips              | https://www.kayak.com.co/trips                        |