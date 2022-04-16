#!/usr/bin/env python
# coding: utf-8

# In[1]:


def increment(n):
    return n + 1


# In[2]:


six = increment(increment(increment(3)))

print(six)


# In[3]:


six = increment(increment(increment(3)))
six = increment(increment(4))
six = increment(5)
six = 6


# In[4]:


def increment(n):
    return n + 1
    print('You will never see this')
    return n + 1

increment(3)


# In[6]:


def add(a, b):
    result = a + b
    return result

x = 3
seven = add(x, 4)


# In[7]:


seven


# In[8]:


def shout(message):
    print(message.upper() + '!!!')

return_value = shout('hey there')
print(return_value)


# In[9]:


def sayhello():
    print('Hey there!')

sayhello()


# In[10]:


def sayhello(name='World', greeting='Hello'):
    return '{}, {}!'.format(greeting, name)


# In[11]:


sayhello()


# In[13]:


sayhello('code')


# In[14]:


sayhello(greeting='Salutations', name='Codeup')


# In[15]:


sayhello()


# In[16]:


args = ['Codeup', 'Salutations']

sayhello(*args)


# In[17]:


kwargs = {'greeting': 'Salutations', 'name': 'Codeup'}

sayhello(**kwargs)


# In[18]:


a_global_variable = 42

def somefunction():
    print('Inside the function: %s' % a_global_variable)

somefunction()
print('Outside the function: %s' % a_global_variable)


# In[19]:


n = 123

def somefunction():
    n = 10
    n = n - 3
    print('Inside the function, n == %s' % n)

print('Outside the function, n == %s' % n)
somefunction()
print('Outside the function, n == %s' % n)


# In[1]:


def is_two(n):
    if n == 2 or n == 'Two':
        return True
    else:
        return False


# In[2]:


is_two(2)


# In[3]:


is_two(6)


# In[4]:


is_two('Two')


# In[5]:


def is_vowel(n):
    if n.lower() in 'aeiou':
        return True
    if n.upper() in 'AEIOU':
        return True
    else:
        return False
    


# In[6]:


is_vowel('iou')


# In[7]:


def is_consonant(n):
    if n.lower() in 'aeiou':
        return False
    if n.upper() in 'AEIOU':
        return False
    else:
        return True


# In[8]:


is_consonant('a')


# In[9]:


is_consonant('b')


# In[69]:


def word(message):
        if 'aeiou' in message :
            return message.lower()
        else:
            return message.capitalize()
    


# In[70]:


word('aord')


# In[92]:


def word(phrase):
    answer = ''
    for letter in phrase:
        if letter in "aeiouAEIOU":
            answer = answer + letter.lower()
        else:
            answer = answer + letter.capitalize()
        return answer 


# In[93]:


word('boop')


# In[1]:


def is_vowel(somestring):
    if type(somestring) == str:
        result = somestring.lower() in ['a', 'e', 'i', 'o', 'u']
        return result
    else:
        return False


# In[11]:


is_vowel ('a')


# In[12]:


is_vowel ('A')


# In[13]:


is_vowel ('b')


# In[18]:


def is_consonant(somestring):
    if type(somestring) == str:
        only_letters = somestring.isalpha()
        return only_letters and not is_vowel(somestring)
    return False


# In[19]:


is_consonant ('3')


# In[20]:


is_consonant ('a')


# In[21]:


is_consonant ('z')


# In[23]:


def word(string):
    if type(string) != str:
        return False
    first_letter = string[0]
    if is_consonant(first_letter):
        string = string.capitalize()
        return string


# In[24]:


word('fat')


# In[25]:


word('donkey')


# In[48]:





# In[6]:





# In[7]:


def calculate_tip(bill, tip_percentage=0.2):
    if type(tip_percentage) != float:
        return False
    if tip_percentage < 0 or tip_percentage > 1:
        return 'the tip percentage must be between 0 and 1'
    return tip_percentage * bill


# In[8]:


calculate_tip (20)


# In[9]:


calculate_tip(25)


# In[4]:


def apply_discount(price, discount_percentage):
    price = 100
    discount_percentage = .2
    discount = price * discount_percentage
    return price - discount
# needed to keep variables open


# In[32]:


def apply_discount(price, discount_percentage):
    discount = price * discount_percentage
    return price - discount


# In[33]:


apply_discount(100, .2)


# In[ ]:





# In[35]:


def handle_commas(somestring):
    if type(somestring) != str:
        return 'input must be a string'
    somestring = somestring.replace(',', '')
    if somestring.isdigit():
        return float(somestring)
    else:
        return 'input must be a string that is a number'


# In[36]:


handle_commas('hello,,world')


# In[37]:


handle_commas('50,00000')


# In[42]:


def get_letter_grade(grade):
    if type(grade) == int or type(grade) == float:
        if grade >= 100:
            return "A, Great job"
        elif grade >= 80:
            return "B, Almost there"
        elif grade >= 70:
            return "C, Try Harder"
        elif grade >= 60:
            return "D, You suck"
        else:
            return "F, Redo"
    else:
        return "Input must be a number"


# In[44]:


get_letter_grade(60)


# In[60]:


def remove_vowels(somestring):
   # if type(somestring) != str:
    for letter in somestring:
        if is_consonant(letter):
            output += letter
        return output


# In[49]:


def remove_vowels(somestring):
    if type(somestring) != str: # i see the importiance of this varification
        return False
    output = ''
    for letter in somestring:
        if is_consonant(letter):
            output += letter
    return output


# In[51]:


remove_vowels('aaaaaaaaaeeeeeeeiiiiooooouuu ,wow!!!!!')


# In[2]:


def normalize_name(string):
    output = ''
    string = string.lower()
    for character in string:
        if character.isidentifier() or character == ' ':
            output += character
    output = output.strip()
    output = output.replace('_', ' ') 
    return output


# In[3]:


normalize_name ('______BiGGySmalls@#$_____')


# In[70]:


def cumulative_sum(x):
    output = []
    for i, num in enumerate(x):
        sum_so_far = sum(x[:i + 1])
        output.append(sum_so_far)
    return output


# In[75]:


somenums = [1, 2, 3]


# In[76]:


def cumulative_sum(somenums):
    output = []
    for i, num in enumerate(somenums):
        sum_so_far = sum(somenums[:i + 1])
        output.append(sum_so_far)
    return output


# In[77]:


somenums


# In[85]:


cumulative_sum ([1 , 4, 8 ])


# In[ ]:


def cumulative_sum(somenums):
    output = []
    for i in range(len(somenums)):
        sum_so_far = sum(somenums[:i + 1])
        output.append(sum_so_far)
    return output


# In[ ]:


# range(len) = enumerate // so i guess distince variance vs length of string numbered. play with enumerate JOEY!!!#

