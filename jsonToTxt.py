import json
from os.path import exists

def main():
    print("jsonToTxt.py called successfully")
    # Check if JSON file exists
    if not exists('myJson.json'):
        print("File not found")
        return
    with open('myJson.json', 'r+') as f:
        myJson = json.load(f)
        if len(myJson) == 0:
            print("No JSON file found")
            f.close()
            return
    f.close()

    # Write JSON info to 'tasks.txt'
    with open('tasks.txt', 'w') as f:
        for i in myJson:
            f.write('\n')
            f.write(i['title']+' ')
            f.write('\n')
            for j in i['items']:
                f.write('- '+ j['name'] + ': ')
                f.write(j['desc'] + ' ')
                f.write('\n')
    f.close()

    print("jsonToTxt.py has finished generating tasks.txt from myJson.json")

if __name__ == '__main__':
    main()