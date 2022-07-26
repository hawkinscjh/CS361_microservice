# CS361_microservice

Partner Communication Contract:

Requests:

Request data by calling jsonToTxt.py after exporting json data to local file named 'myJson.json'

Json format should be in the format of the example shown below.

[ { "items": [ { "desc": "Honey Crisp", "name": "apple" }, { "desc": "Boneless Skinless thighs", "name": "Chicken" } ], "title": "Grocery" }, { "items": [ { "desc": "Thursday at 9am", "name": "Doctor" }, { "desc": "Monday 10am", "name": "Dentist" } ], "title": "Appointments" } ]

Receive:

Receive data by reading local 'tasks.txt' file created by jsonToTxt.py. Text file created will be in the format shown below.

Grocery

apple: Honey Crisp
Chicken: Boneless Skinless thighs
Appointments

Doctor: Thursday at 9am
Dentist: Monday 10am
UML Diagram:

![image](https://user-images.githubusercontent.com/59400213/181065943-cc278642-250c-4736-8d41-3389afc85fa8.png)
