*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input Register Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  nalle  nalle123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  nalle123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  ka  nalle123
    Output Should Contain  Username too short

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  kalle1  nalle123
    Output Should Contain  Username must only contain letters a-z

Register With Valid Username And Too Short Password
    Input Credentials  kalle  na
    Output Should Contain  Password too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kalle  nallenalle
    Output Should Contain  Password must contain at least one number

*** Keywords ***
Create User And Input Register Command
    Create User  kalle  kalle123
    Input Register Command