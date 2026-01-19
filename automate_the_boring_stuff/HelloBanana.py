#this program asks you about yourself

print ('Hello World')

print ('What is your name?') #ask them
myName = input()
print ('Its good times ' + myName)
print ('The length of your name is:')
print (len(myName))

print ('What is your age?') # ask for age
myAge = input()
print ('You will be ' + str(int(myAge) + 1) + ' in a year.')