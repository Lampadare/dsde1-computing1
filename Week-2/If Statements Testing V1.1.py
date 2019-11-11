# If statements testing
import time
print('Enter your goddam name')
name = input()
if name[0] == 'M' :
    print('SHIIIEEEET M GAAAANG MY BOIIIIII')
elif name[0] == 'm' :
    print('SHIIIEEEET M GAAAANG MY BOIIIIII')
else:
    print("YOU ARE  L A M E  CUZ YOUR  N A M E  DIDN'T START WITH M")

time.sleep(2)
print('Enter your fucking age')
age = int(input())
if age > 95 :
    print('You old motherfucker...')
elif age > 55 :
    print("Youth doesn't last forever")
elif age > 35 :
    print('You boutta find out what real oldness is like')
elif age > 20 :
    print('Do your best now cuz you are at your peak my boi')
elif age > 15 :
    print('You immature piece of shiet')
elif age > 8 :
    print('I bet you are a virgin')
else :
    print('Ababa Booboo Guilly PooPoo')
time.sleep(2)

spam = 0
if age > 30 :
    while spam < age :
        print('Why are you so old yet so immature')
        time.sleep(0.2)
        spam = (spam+1)
else :
     while spam < age :
         print('Why are you so young yet look like a granny')
         time.sleep(0.2)
         spam = (spam+1)

print('This was printed ',age,' times, you know, like your age...')