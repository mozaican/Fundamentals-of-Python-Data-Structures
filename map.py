"""
Small program that finds a Google Map address by
entering it in the 'Run' dialog box on Windows. 
"""

import webbrowser, sys, pyperclip

# check if command line arguments were passed
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

# https://www.google.com/maps/places/<address>
webbrowser.open('https://www.google.com/maps/places/' + address) 