*** Settings ****
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser

*** Test Cases ***
Register With Valid Username And Password
    Go To Main Page And Click Register
    Set Username  lars
    Set Password  lars123123
    Set Confirmation Password  lars123123
    Click Button  Register
    Page Should Contain  Welcome

Register With Too Short Username And Valid Password
    Go To Main Page And Click Register
    Set Username  a 
    Set Password  lars123123
    Set Confirmation Password  lars123123
    Click Button  Register
    Page Should Contain  Username must be 3 or more char

Register With Valid Username And Too Short Password
    Go To Main Page And Click Register
    Set Username  anders
    Set Password  aa 
    Set Confirmation Password  aa
    Click Button  Register
    Page Should Contain  Password must be 8 or more char


Register With Nonmatching Password And Password Confirmation
    Go To Main Page And Click Register
    Set Username  bosse
    Set Password  bosse123123
    Set Confirmation Password  bosse00000000
    Click Button  Register
    Page Should Contain  Password must match each other

*** Keywords ***
Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Text  password  ${password}

Set Confirmation Password
    [Arguments]  ${password}
    Input Text  password_confirmation  ${password}

Go To Main Page And Click Register
    Go To Main Page
    Click Link  Register new user