import re


def phone_match_1():
    phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    mo = phone_num_regex.search('My number is 415-555-4242.')
    print(mo.group())

def phone_match_2():
    '''
    Grouping with Parentheses
    Say you want to separate the area code from the rest of the phone number.
    Adding parentheses will create groups in the regex: (\d\d\d)-(\d\d\d-\d\d\d\d).
    Then you can use the group() match object method to grab the matching text from just one group.
    The first set of parentheses in a regex string will be group 1.
    The second set will be group 2. By passing the integer 1 or 2 to the group()
    match object method, you can grab different parts of the matched text. Passing 0 or nothing to the group()
    method will return the entire matched text. Enter the following into the interactive shell:
    :return:
    '''
    phone_num_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
    mo = phone_num_regex.search('My number is 415-555-4242.')
    #below will print whole matched string
    print(mo.group())
    #below will print first group
    print(mo.group(1))
    #below will print second group
    print(mo.group(2))
    print(mo.groups())


def match_multiple_groups_with_pipe():
    hero_regex = re.compile(r'Batman|Tina Fey')
    mo1 = hero_regex.search('Batman and Tina Fey')
    mo2 = hero_regex.search('Tina Fey and Batman')
    print(mo1.group())
    print(mo2.group())


def optional_matching_with_question_mark():
    '''
    Sometimes there is a pattern that you want to match only optionally.
    That is, the regex should find a match regardless of whether that bit of text is there.
     The ? character flags the group that precedes it as an optional part of the pattern.
     For example, enter the following into the interactive shell:
    :return:
    '''
    batRegex = re.compile(r'Bat(wo)?man')
    mo1 = batRegex.search('The Adventures of Batman')
    mo2 = batRegex.search('The Adventures of Batwoman')
    print(mo1.group())
    print(mo2.group())


def zero_or_more_with_star():
    '''
    The * (called the star or asterisk) means
    “match zero or more”—the group that precedes the star can occur any number of times in the text.
    It can be completely absent or repeated over and over again.
    Let’s look at the Batman example again.
    :return:
    '''
    batRegex = re.compile(r'Bat(wo)*man')
    mo1 = batRegex.search('The Adventures of Batman')
    print(mo1.group())
    mo3 = batRegex.search('The Adventures of Batwowowowoman')
    print(mo3.group())


def one_or_more_with_plus():
    batRegex = re.compile(r'Bat(wo)+man')
    mo1 = batRegex.search('The Adventures of Batwoman')
    print(mo1.group())
    mo3 = batRegex.search('The Adventures of Batman')
    print(mo3 == None)


def specific_repetitions():
    '''
    Matching Specific Repetitions with Braces
    If you have a group that you want to repeat a specific number of times,
    follow the group in your regex with a number in braces.
    For example, the regex (Ha){3} will match the string 'HaHaHa', \
    but it will not match 'HaHa', since the latter has only two repeats of the (Ha) group.
    Instead of one number, you can specify a range by writing a minimum, a comma,
    and a maximum in between the braces. For example, the regex (Ha){3,5} will match 'HaHaHa', 'HaHaHaHa', and 'HaHaHaHaHa'.
    :return:
    '''
    haRegex = re.compile(r'(Ha){3}')
    mo1 = haRegex.search('HaHaHa')
    mo2 = haRegex.search('Ha')
    print(mo1.group())
    print(mo2 == None)

'''
Greedy and Non-greedy Matching
Since (Ha){3,5} can match three, four, or five instances of Ha in the string 'HaHaHaHaHa',
 you may wonder why the Match object’s call to group() in the previous brace example returns 'HaHaHaHaHa' 
 instead of the shorter possibilities. After all, 'HaHaHa' and 'HaHaHaHa' are also valid matches of
  the regular expression (Ha){3,5}.

Python’s regular expressions are greedy by default, which means that in ambiguous situations 
they will match the longest string possible. The non-greedy (also called lazy) version of the braces,
 which matches the shortest string possible, has the closing brace followed by a question mark.

Enter the following into the interactive shell, and notice the difference between the greedy and 
non-greedy forms of the braces searching the same string:

>>> greedyHaRegex = re.compile(r'(Ha){3,5}')
>>> mo1 = greedyHaRegex.search('HaHaHaHaHa')
>>> mo1.group()
'HaHaHaHaHa'

>>> nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
>>> mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
>>> mo2.group()
'HaHaHa'

Note that the question mark can have two meanings in regular expressions: declaring a non-greedy match or flagging an optional group. These meanings are entirely unrelated.
'''


def find_all():
    phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')  # has no groups
    print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))
    phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')  # has groups
    print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))


def char_class_example():
    xmasRegex = re.compile(r'\d+\s\w+')
    print(xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids,'))
    vowelRegex = re.compile(r'[aeiouAEIOU]')
    print(vowelRegex.findall())
    '''
    Note that inside the square brackets, the normal regular expression 
    symbols are not interpreted as such. This means you do not need to escape the ., *, ?, or ()
     characters with a preceding backslash. For example, the character class [0-5.]
      will match digits 0 to 5 and a period. You do not need to write it as [0-5\.].
    '''
    consonantRegex = re.compile(r'[^aeiouAEIOU]')
    print( consonantRegex.findall('RoboCop eats baby food. BABY FOOD.'))




if __name__ == '__main__':
    #phone_match_1()
    #phone_match_2()
    #match_multiple_groups_with_pipe()
    #optional_matching_with_question_mark()
    #zero_or_more_with_star()
    #one_or_more_with_plus()
    specific_repetitions()