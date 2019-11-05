## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## interactive_story_1
* greet
    - utter_greet
* user_info
    - utter_my_message
* mood_unhappy
    - utter_did_that_help
* affirm
    - utter_greet
* goodbye
    - utter_goodbye
* user_info
    - utter_iamabot

## interactive_story_1
* user_info
    - utter_my_message
* bot_challenge
    - utter_iamabot

## interactive_story_1
* user_info
    - utter_my_message
* bot_challenge
    - utter_iamabot

## interactive_story_1
* car_info
    - utter_my_car
* bot_challenge
    - utter_greet

## interactive_story_1
* car_info
    - utter_my_car
* bot_challenge
    - utter_happy
* car_info
    - utter_my_car
* bot_challenge
    - utter_greet

## interactive_story_1
* car_info
    - utter_my_car
* car_info
    - utter_my_car
* bot_functions
    - utter_happy
* car_info
    - utter_my_car

## interactive_story_1
* car_info
    - utter_my_car
* bot_functions
    - utter_happy

## interactive_story_1
* car_info
    - utter_my_car
* bot_functions
    - utter_happy
* car_info
    - utter_my_car
* bot_functions
    - utter_happy
* car_info
    - utter_my_car
* bot_functions
    - utter_happy
