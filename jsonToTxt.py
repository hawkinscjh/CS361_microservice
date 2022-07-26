import json

print("jsonToTxt.py called successfully")
with open('myJson.json', 'r+') as f:
    x = json.load(f)
f.close()

# Write JSON info into 'tasks.txt'
with open('tasks.txt', 'w') as f:
    for i in x:
        f.write('\n')
        f.write(i['title']+' ')
        f.write('\n')
        for j in i['items']:
            f.write('- '+ j['name'] + ': ')
            f.write(j['desc'] + ' ')
            f.write('\n')
f.close()

print("jsonToTxt.py has finished generating a tasks.txt from myJson.json")