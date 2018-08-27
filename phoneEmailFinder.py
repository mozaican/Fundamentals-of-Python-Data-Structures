"""
Program that extracts phone numbers and email addresses from 
a text and copy them in the clipboard for further manipulation.
"""

import re, pyperclip

# create the regex for phone numbers
phoneRegex = re.complie(r'''
# 415-777-0000, 777-0000, (415) 777-0000
(
    ((\d\d\d) | (\(\d\d\d\)))?   # area code (optional)
    (\s | -)                     # first separator
    \d\d\d                       # first 3 digits
    -                            # separator
    \d\d\d\d                     # last 4 digits
)
''', re.VERBOSE)

# create a regex for the email addresses
emailRegex = re.compile(r'''
    [a-zA-Z0-9_.+]+            # name part
    @                          # @ symbol
    [a-zA-Z0-9_.+]+            # domain name part
''', re.VERBOSE)

# get the text off the clipboard 
text = pyperclip.paste()

# extract the email/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

# copy the extracted email/phone to the clipboard
results = "\n".join(allPhoneNumbers) + "\n" + "\n".join(extractedEmail)
pyperclip.copy(results)