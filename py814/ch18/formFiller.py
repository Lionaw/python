# Automatically fills in the form.

import pyautogui,time

formData = [{'name': 'Alice', 'fear': 'eavesdroppers', 'source': 'wand', 'robocop': 4, 'comments': 'Tell Bob I said hi.'},
            {'name': 'Bob', 'fear': 'bees', 'source': 'amulet', 'robocop': 4, 'comments': 'n/a'},
            {'name': 'Carol', 'fear': 'puppets', 'source': 'crystal ball', 'robocop': 1, 'comments': 'Please take the puppets out of the break room.'},
            {'name': 'Alex Murphy', 'fear': 'ED-209', 'source': 'money', 'robocop': 5, 'comments': 'Protect the innocent. Serve the public trust. Uphold the law.'},
            ]
pyautogui.PAUSE = 0.5
print('Ensure that the browser window is active and the form is loaded!')
# Set these to the orrect coordinates for your computer.
nameField = (,)
submitButton = (,)
submitButtonColor = (,)
submitAnotherLink = (,)

for person in formData:
# TODO:Give the user a chance to kill the script.
    print('>>> 5 SECOND PAUSE TO LET USER PRESS CTRL-C <<<')
    time.sleep(5)
# TODO:Wait until the form page has loaded.
    while not pyautogui.pixelMatchesColor(submitButton[0],submitButton[1],submitButtonColor):
        time.sleep(5)
        print('Entering %s info...' % (person['name']))
        pyautogui.click(nameField[0],namefield[1])
# TODO:Fill out the Name Field.
        pyautogui.typewrite(person['name'] + '\t')
# TODO:Fill out the Greatest Fear(s) field.
        pyautogui.typewrite(person['fear'] + '\t')
# TODO:Fill out the Source if Wizard Powers field.
        if person['source'] == 'wand':
            pyautogui.typewrite(['down','\t'])
        elif person['source'] == 'amulet':
            pyautogui.typewrite(['down','down','\t'])
        elif person['source'] == 'crystal ball':
            pyautogui.typewrite(['down','down','down','\t'])
        elif person['source'] == 'money':
            pyautogui.typewrite(['down','down','down','down','\t'])
# TODO:File out the Robocop field.
        if person['source'] == 1:
            pyautogui.typewrite(['','\t'])
        elif person['source'] == 2:
            pyautogui.typewrite(['right','\t'])
        elif person['source'] == 3:
            pyautogui.typewrite(['right','right','\t'])
        elif person['source'] == 4:
            pyautogui.typewrite(['right','right','right','\t'])
        elif person['source'] == 5:
            pyautogui.typewrite(['right','right','right','right',,'\t'])
# TODO:File out the Additional Comments field.
        pyautogui.typewrite(person['comments'] + '\t')
# TODO:Click Submit.
        pyautogui.press('enter')
# TODO:Wait until form page has loaded.
        print('Click Submit.')
        time.sleep(5)
# TODO:Click the Submit another response link.
        pyautogui.click(submitAnotherLink[0],subminAnotherLink[1])