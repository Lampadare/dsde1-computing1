'''
keywords.py

Create functions that use keyword arguments
with default values.
'''

# Create a function called welcome_message():
# if no input argument is provided
# it returns the string 'Hello and welcome'
# if a keyword argument called user_name is provided
# it returns 'Hello, <user_name>, and welcome'
# if a keyword argument called place is provided
# it returns 'Hello and welcome to <place>'
# if both user_name and place are provided
# it returns 'Hello, <user_name>, and welcome to <place>

def welcome_message(user_name = '', place = ''):
    if user_name and place != '':
        return 'Hello, {}, and welcome to {}'.format(user_name, place)
    elif user_name != '':
        return 'Hello, {}, and welcome'.format(user_name)
    elif place != '':
        return 'Hello and welcome to {}'.format(place)
    elif user_name == '':
        return 'Hello and welcome'


# Create a function called list_average()
# without using any libraries to do the maths for you 
# (the point of this exercise is to practice interacting 
# with lists)
# the first argument is a list of numbers
# the second optional keyword arguemt is called avg_type
# if nothing for avg_type provided, return the mean of the list
# if avg_type=median', return themedian of the list 
# (return list of all modes if there is a tie between multiple values)
# if avg_type='mean', return the mean of the list
# if avg_type='median', return the median of this list

def list_average(ls, avg_type = 'mean'):
    if avg_type == 'mean' and len(ls) != 0:
        return sum(ls)/len(ls)
    else:
        return 0
    if avg_type == 'median':
        if len(ls) % 2 == 0:
            middle = len(ls)/2
            median = (ls[middle-1] + ls[middle])/ 2
            return median
        else:
            median = len(ls)/2
            return median
    if avg_type == 'mode':
        if ls == []:
            return []
        else:
            d = {}
            for x in ls:
                keys = d.keys()
                if x in keys:
                    d[x] += 1
                else:
                    d[x] = 1
            max_value = max(d.value())
            max_keys = [i for i, v in d.items() if v == max_value]
            return max_keys