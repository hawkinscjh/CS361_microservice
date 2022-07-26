import json
import subprocess

x = [
    {
        "title": "Grocery",
        "items": [
            {
                "name": "apple",
                "desc": "Honey Crisp"
            },
            {
                "name": "Chicken",
                "desc": "Boneless Skinless thighs"
            }
        ]
    },
    {
        "title": "Appointments",
        "items": [
            {
                "name": "Doctor",
                "desc": "Thursday at 9am"
            },
            {
                "name": "Dentist",
                "desc": "Monday 10am"
            }
        ]
    }
]

print("Sending json data to external myJson.json file")
with open("myJson.json", "w") as f:
	json.dump(x, f, indent = 4, sort_keys=True)
f.close()

print("Calling jsonToTxt.py subprocess")
subprocess.run("python3 jsonToTxt.py", shell=True)

print("Adding data from newly generated tasks.txt file to tasks")
with open("tasks.txt", "r") as f:
    tasks = f.read()
f.close()

print("Print data from tasks.txt\n")
print(tasks)