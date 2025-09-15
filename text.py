# def add(x, y):
#     return(x + y)

# def substract()

# ddtrr = 'hello world'
# r = ddtrr[1:4:1]
# print(r)

data = {
    'hii': 'hlo',
    'by': 'ok have a nice day😊'
}

def chatbot():
    print('wlcm')
    while True:
        user_input = input('enter your msg: ')
        if user_input in data:
            print('chatbot: ', data[user_input])
        elif user_input == 'quit'.lower():
            break
        else:
            print('not in my dict coming soon')
chatbot()