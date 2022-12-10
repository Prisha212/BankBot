# BankBot
A virtual assistant powered by RASA 3.0 which provides information on different banks in USA for international student.

Instructions to run:

1)Create virtual environment using python3 -m venv ./venv
2)Activate the environment using source ./venv/bin/activate
3)Download all the dependencies as mentioned in requirement.txt
4)Clone this repository in your local machine using gh repo clone Prisha212/BankBot
5)Train the model using rasa train
6)Activate the action server in another terminal using rasa run actions
7)Now run the bot in terminal using rasa shell


Conversational Flow

Story 1:

intent: greet
hey

hello

hi

hello there

good morning

good evening

moin

hey there

let's go

hey dude

goodmorning

goodevening

good afternoon

#Intent is present in nlu.yml file
 intent: international
  examples:
    -Are you international student
    -Are you from india  
    -Are you not an US citizen.
    
       
- intent: bank_ac
  examples: 
    -I want to open my bank account
    -In which bank I can open my account.
    -Bank?
     
     

- intent: int_student
  examples:
   -I am international student.
   -international

- intent: dom_student
  examples:
   -I am domestic student.
   -domestic   




- intent: int_interest
  examples: 
   -I want to open account in US bank
   -US bank    



     
- intent: int_age_above  
  examples: 
   -above
   -I am above 25

- intent: int_age_below
  examples:
    -below
    -I am below 25

- intent: int_open
  examples:
    -What documents require
    -Documents
    -Steps to open bank account

- intent: int_branch
  examples:
   -Nearest branch
   -Branch

   

- intent: int_services
  examples:
   -What services bank provide
   -Services


WEATHER API is integrated

- intent: weather
  examples:
    -what is the t weather
    -i want to know the weather of today
    -tell me the weather forecast
    -hows the weather today?

- intent : city
  examples:
    -San Jose
    -San Francisco
    -hayward
    -Fremont
    -New York
    -Chicago
    -Dallas
    
    
    
    Other stories are present in stories.yml file





