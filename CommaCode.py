def comma(listValue):
    string = ', '.join(listValue[:-1]) + ', and ' + listValue[-1]
    print(string)

spam = ['apples', 'bananas', 'tofu', 'cats']
comma(spam)


