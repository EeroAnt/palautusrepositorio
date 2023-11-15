*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Reset App And Go To Register Page

***Test Cases***

Register With Valid Username And Password
    Set Username  kalleksi
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ka
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Register Should Fail With Message  Username must be at least 3 characters long

Register With Valid Username And Invalid Password
# salasana ei sisällä halutunlaisia merkkejä
    Set Username  kalleksiko
    Set Password  kallekalle
    Set Password Confirmation  kallekalle
    Submit Credentials
    Register Should Fail With Message  Password must not contain only letters

Register With Nonmatching Password And Password Confirmation
    Set Username  kalleksikohan
    Set Password  kalle123
    Set Password Confirmation  kalle321
    Submit Credentials
    Register Should Fail With Message  Password and password confirmation do not match

Login After Successful Registration
    Set Username  kalleksikohankaan
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Register Should Succeed
    Go To Login Page
    Set Username  kalleksikohankaan
    Set Password  kalle123
    Submit Login Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  ka
    Set Password  kalle123
    Set Password Confirmation  kalle122
    Submit Credentials
    Register Should Fail With Message  Username must be at least 3 characters long
    Go To Login Page
    Set Username  ka
    Set Password  kalle123
    Submit Login Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Submit Credentials
    Click Button  Register

Submit Login Credentials
    Click Button  Login

Register Should Succeed
    Click Link  Continue to main page
    Main Page Should Be Open

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Reset App And Go To Register Page
    Reset Application
    Go To Register Page