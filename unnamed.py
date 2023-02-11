word = '@'
address = input()
login = input()
if address.find(word) != -1 and login.find(word) == -1:
    print('OK')
elif address.find(word) == -1 and login.find(word) == -1:
    print ('Wrong address')
elif login.find(word) != -1 and address.find(word) != -1:
    print('Wrong login')
else:
    print('Wrong password and login')