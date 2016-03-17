# civ_script
CIV V download/submission script for GMR

WINDOWS
1. Install python on your computer from here: https://www.python.org/downloads/
2. When installing, make sure to check the box that says “Add python to environment variable” (so you can access it from command prompt)
3. Go to this link: https://bootstrap.pypa.io/get-pip.py, and save that file (i.e. right click on the page and hit “save” to your desktop. Should have the name get-pip.py
4. Open command prompt, navigate to your desktop (probably the command “cd Desktop” and then type “python get-pip.py”
5. Then type “pip install requests”

MAC
1. Go to terminal, type “sudo easy_install pip” and then enter your password
2. Type “sudo pip install requests”

You need to open "civMultiplayer.py" in a text editor and change the global variable AUTH_KEY to your authentication key found here: # Available here: http://multiplayerrobot.com/Download