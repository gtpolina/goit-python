import re


phone_book = {}


def hello_func(input_text):
    answer_f = 'How can i help you?'
    return answer_f


def add_func(input_text):
    if input_text[0] in list(phone_book):
        answer_f = 'Contact exists, use "change" command in order to change number? or use another name'
    else:
        phone_book[input_text[0]] = input_text[1]
    answer_f = 'Contact added to phonebook'
    return answer_f


def change_func(input_text):
    if input_text[0] not in list(phone_book):
        answer_f = 'No contact to change, choose "add" to add a contact to phonebook'
    else:
        phone_book[input_text[0]] = input_text[1]
    answer_f = 'Contact is changed'
    return answer_f


def phone_func(input_text):
    if input_text[1] in list(phone_book):
        answer_f = f'   {input_text[1]}   {phone_book[input_text[1]]}'


def show_all_func(input_text):
    if not phone_book:
        answer_f = 'Phone book is empty, chose "add" to add contact'
    else:
        for key, value in map(lambda i: (i[0], i[1]), phone_book.items()):
            answer_f = f'   {key}   {value}\n'
    return answer_f


def other_option():
    answer_f = 'No such command'
    return answer_f


COMMANDS = {
    'hello': hello_func,
    'add': add_func,
    'change': change_func,
    'phone': phone_func,
    'show all': show_all_func,
    'close': None,
    'exit': None,
    'good bye': None,
    '.': None

}


def inputs(mod):
    return COMMANDS.get(mod, 'other_option')


bye_commands = ("good bye", "close", "exit", ".")

no_args_commands = ('hello', 'show all', 'good bye', 'exit', 'close', '.')


def input_error(func):
    def inner():
        frase = func()
        result = None

        try:
            command_to_bot = list(
                filter(lambda i: not frase.find(i), COMMANDS.keys()))[0]
        except IndexError:
            result = 'Command does not exist, try again'
            return result
        else:
            if command_to_bot in no_args_commands and frase not in no_args_commands:
                result = 'Nno spaces/arguments for this command, please, try again'
                return result
            elif command_to_bot not in no_args_commands and not frase.startswith(command_to_bot + ' '):
                result = 'Command syntax is incorrect, input command word with arguments using spaces in between'
                return result

        if command_to_bot in ('add', 'change'):
            try:
                try_variable = frase.split()[1]
            except IndexError:
                result = 'Input name and phone after "add" command'
            else:
                if len(frase.split()) == 2:
                    result = 'This data in not enough, try again with name and number devided by space'
                elif len(frase.split()) > 4 and re.fullmatch(r'\+?\d+', frase.split()[-1]) != None:
                    result = 'Try one or two words in name'
                elif len(frase.split()) <= 4 and re.fullmatch(r'\+?\d+', frase.split()[-1]) == None:
                    result = 'Phone number supposed to contain digits'

                elif len(frase.split()) == 3:
                    frase = [frase.split()[1]] + [frase.split()[2]]
                elif len(frase.split()) == 4:
                    frase = [frase.split()[1] + ' ' + frase.split()[2]] + \
                        [frase.split()[3]]

        if command_to_bot == 'phone':
            try:
                try_variable = frase.split()[1]
            except:
                result = 'Input name to find in phone_book'
            else:
                frase = frase.removeprefix(command_to_bot + ' ')
                if frase not in list(phone_book):
                    result = 'No phone number with this name'

        if result:
            return result
        else:
            return command_to_bot, frase
    return inner


@input_error
def main_input():
    user_input = input('Input command: ').casefold()
    return user_input


def main():
    while True:

        res = main_input()

        if res[0] in bye_commands:
            print('Good bye!')
            break

        else:
            requests = inputs(res[0])
            try:
                requests(res[1])
            except TypeError:
                print(res)
                continue
            else:
                print(requests(res[1]))


if __name__ == '__main__':
    main()
