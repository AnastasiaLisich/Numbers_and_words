# get_num = input('Please, enter a number: ')

dict_for_twenty = {
    '1':'один', 
    '2':'два', 
    '3':'три', 
    '4':'четыре', 
    '5':'пять', 
    '6':'шесть', 
    '7':'семь', 
    '8':'восемь', 
    '9':'девять', 
    '10':'десять',
    '11':'одиннадцать',
    '12':'двенадцать',
    '13':'тринадцать',
    '14':'четырнадцать',
    '15':'пятнадцать',
    '16':'шестнадцать',
    '17':'семнадцать',
    '18':'восемнадцать',
    '19':'девятнадцать',
    '20': 'двадцать',
    '30':'тридцать',
    '40':'сорок',
    '50':'пятьдесят',
    '60':'шестьдесят',
    '70':'семьдесят',
    '80':'восемьдесят',
    '90':'девяносто',
    '100':'сто',
    }


def parse_numbers(the_number):
    revers_str_from_num = reversed((str(the_number)))
    numbers = []

    if int(the_number) in (11, 12, 13, 14, 15, 16, 17, 18, 19):
        numbers.append(int(the_number))

    else:

        for index, value in enumerate(revers_str_from_num):
            if int(value) != 0:
                numbers.append(int(value) * 10 ** int(index)) 


    return numbers


def change_num_to_word(list_of_numbers):
    words = ''
    for number in list_of_numbers[::-1]:
        if number != 0:
            words += dict_for_twenty[str(number)] + ' '

    stripped_words = words.rstrip()
    print(stripped_words[-1] != ' ')

    return stripped_words 


for the_number in range(1, 101):
    print(the_number, change_num_to_word(parse_numbers(the_number)))