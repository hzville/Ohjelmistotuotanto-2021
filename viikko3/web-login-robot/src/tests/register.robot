*** Settings ****
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser

*** Variables ***
${SUCCESSFUL USERNAME}  lars
${SUCCESSFUL PASSWORD}  lars123123
${FAIL USERNAME}  a
${FAIL PASSWORD}  lars123123

*** Test Cases ***
Register With Valid Username And Password
    Go To Main Page And Click Register
    Set Username  ${SUCCESSFUL USERNAME}
    Set Password  ${SUCCESSFUL PASSWORD}
    Set Confirmation Password  ${SUCCESSFUL PASSWORD}
    Click Button  Register
    Page Should Contain  Welcome

Register With Too Short Username And Valid Password
    Go To Main Page And Click Register
    Set Username  ${FAIL USERNAME}
    Set Password  ${FAIL PASSWORD}
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

Login After Successful Registration
    Go To Main Page And Click Login
    Set Username  ${SUCCESSFUL USERNAME}
    Set Password  ${SUCCESSFUL PASSWORD}
    Click Button  Login
    Page Should Contain  Ohtu Application main page

Login After Failed Registration
    Go To Main Page And Click Login
    Set Username  ${FAIL USERNAME}
    Set Password  ${FAIL PASSWORD}
    Click Button  Login
    Page Should Contain  Invalid username or password

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

Go To Main Page And Click Login
    Go To Main Page
    Click Link  Login