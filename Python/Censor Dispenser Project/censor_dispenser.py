import re

# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:

email_one = \
    open("email_one.txt", 'r').read()
email_two = \
    open("email_two.txt", 'r').read()
email_three = \
    open("email_three.txt", 'r').read()
email_four = \
    open("email_four.txt", 'r').read()


def ireplace(self, old, new, count=0):
    ''' Behaves like S.replace(), but does so in a case-insensitive fashion. '''

    pattern = re.compile(re.escape(old), re.I)
    return re.sub(pattern, new, self, count)


# Censor first email
email_one = ireplace(email_one, 'learning algorithms',
                     'XXXXXXXX XXXXXXXXXX')

# Censor second email
proprietary_terms = [
    'she',
    'personality matrix',
    'sense of self',
    'self-preservation',
    'learning algorithm',
    'her',
    'herself',
    ]
for word in proprietary_terms:
    email_two = ireplace(email_two, word, 'X' * len(word))

# Censor third email
negative_words = [
    'concerned',
    'behind',
    'danger',
    'dangerous',
    'alarming',
    'alarmed',
    'out of control',
    'help',
    'unhappy',
    'bad',
    'upset',
    'awful',
    'broken',
    'damage',
    'damaging',
    'dismal',
    'distressed',
    'distressed',
    'concerning',
    'horrible',
    'horribly',
    'questionable',
    ]
occurances = 0
for word in negative_words:
    if word in email_three:
        occurances += 1
    if occurances > 2:
        email_three = ireplace(email_three, word, 'X' * len(word))
for word in proprietary_terms:
    email_three = ireplace(email_three, word, 'X' * len(word))

# Censor fourth email
censor = proprietary_terms + negative_words
for word in censor:
    email_four = ireplace(email_four, word, 'X' * len(word))
