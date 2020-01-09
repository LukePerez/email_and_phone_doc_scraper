#! python3
# created with help from Al Sweigart's book "Automate The Boring Stuff With Python"
import re, pyperclip

# Create a regex obj for phone numbers
phoneRegex = re.compile(r'''
# 415-555-0000, 555-555-5555, (555) 555-5555, 555-5555, 555-5555 ext 12345, ext. 12345, x12345
(
((\d\d\d)|(\(\d\d\d\)))?        # area code (optional)

(\s|-)        # first seperator

\d\d\d        # first 3 digits

-             #seperator

\d\d\d\d             # Last 4 digits

(((ext(\.)?\s)|x)    # extension word-part (optional)
(\d{2,5}))?          # extension number-part (optional)
)''', re.VERBOSE)



# regex for email
emailRegex = re.compile(r'''

[a-zA-Z0-9_.+\-]+        # name part
@        # @ symbol
[a-zA-Z0-9_.+]+        # domain name


''', re.VERBOSE)
# Get text off of clipboard
text = pyperclip.paste()

# Extract email/phone from text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)
print(extractedPhone)
print(extractedEmail)
allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])



# Copy extracted email/phone to clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)
print(results)
