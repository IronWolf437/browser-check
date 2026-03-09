import subprocess
import time

unallow_text = []  # but here your unallow word

def browser_check(command, unallow_text):
    lines = command.strip().split('\n')
    parts = []
    clear = []

    for line in lines:
        part = line.strip().split('\t')
        parts.append(part)

    for i in range(len(parts)):
        for word in unallow_text:
            if (word.lower() in parts[i][1].lower()) or (word.lower() in parts[i][2].lower()):
                tab_id = parts[i][0]
                clear.append(tab_id)
                break
    
    for i in clear:
        subprocess.run(['brotab', 'close', i])


while True:
    command = subprocess.check_output(['brotab', 'list']).decode('utf-8')
    browser_check(command, unallow_text)
    time.sleep(5)
