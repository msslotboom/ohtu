*** Settings ***
Resource  resource.robot
Test Setup  Input New Command and Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kalleee  kalle123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123 
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  a  kalle123
    Output Should Contain  Username should be at least 3 characters long

Register With Valid Username And Too Short Password
    Input Credentials  kalleee  abc1234
    Output Should Contain  Password should be at least 8 characters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kalleeee  password
    Output Should Contain  Password should contain at least one symbol or number

*** Keywords ***
Input New Command And Create User
    Create User  kalle  kalle123
    Input New Command