# Created by josephkeane at 4/23/25
Feature: Secondary Deals Page
  # Enter feature description here

  Scenario: User can open the Secondary deals page and go through the pagination
    Given Open the main page
    When Log in to the page
    And Click on the Secondary option at the left side menu
    Then Verify the Secondary page opens
    When Advance to final page
    And Retreat to first page

#  @mobile
#Scenario: User can open the Secondary deals page and go through the pagination
#    Given Open the main page
#    When Log in to the page
#    When Click on the Secondary option at the left side menu
#    Then Verify the Secondary page opens
#    When Advance to final page
#    When Retreat to first page