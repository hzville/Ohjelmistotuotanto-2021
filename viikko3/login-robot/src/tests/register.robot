*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input New Command
    Input Credentials  lars  lars123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input New Command
    Input Credentials  olle  kalle123
    Output Should Contain  User with username olle already exists

Register With Too Short Username And Valid Password
    Input New Command
    Input Credentials  o  kalle123
    Output Should Contain  Username must be 3 or more char

Register With Valid Username And Too Short Password
    Input New Command
    Input Credentials  lars  lars1
    Output Should Contain  Password must be 8 or more char

Register With Valid Username And Long Enough Password Containing Only Letters
    Input New Command
    Input Credentials  lars  passwordpassword
    Output Should Contain  Password must contain other than a-z char

*** Keywords ***
Input New Command And Create User
    Input New Command
    Input Credentials  olle  kalle123

