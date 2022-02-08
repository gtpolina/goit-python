'''the code shows all birthdays strting from the next day from today for 7 days ahead
for example:

input date of monday - you will get all birthdays from tuesday to next monday included
days-off transfered for the next monday

users:
is the test list of names and birthdays dicts

test prints are commented

'''

from datetime import datetime, timedelta
from collections import deque


users = [
    {
        "name": "Bill",
        "birthday": "1998-02-09"
    },
    {
        "name": "Poli",
        "birthday": "1988-02-10"
    },
    {
        "name": "Mary",
        "birthday": "1990-02-13"
    },
    {
        "name": "Jim",
        "birthday": "1985-02-12"
    },
    {
        "name": "Kate",
        "birthday": "1992-02-16"
    },
    {
        "name": "Ann",
        "birthday": "1992-02-13"
    }
]


def get_birthdays_per_week(func_users):

    # input of the date to count from and cutting the hours and minutes part
    today_date = input("Input todays' date in yyyy-mm-dd format: ")
    today_date = datetime.strptime(today_date, '%Y-%m-%d')

    # preparing weekday number keys and empty list values of birthday dict

    b_days_dict = {k: [] for k in range(7)}

    # adding names to proper weekday of birthday date, check sat and sun, to place it for next monday
    for person in func_users:

        person_date = datetime.strptime(
            person["birthday"], '%Y-%m-%d')
        # person_date for next week
        person_date = person_date.replace(year=today_date.year)

        interval = person_date - today_date
        if interval.days < 8 and interval.days > 0:
            key_bdays_dict = person_date.weekday()
            if key_bdays_dict == 5 or key_bdays_dict == 6:
                b_days_dict[0].append(person['name'])

            else:
                b_days_dict[key_bdays_dict].append(person['name'])
    # print(b_days_dict)

    

    # create and sort deque of keys for printing in order starting from today + one day

    d = deque([k for k in b_days_dict.keys()])
    # print(d)

    while d[0] != today_date.weekday()+1:
        d.appendleft(d.pop())
    # print(d)
    

    # clean empty values in birthday dict
    new_bday_dict = {}
    for key, value in b_days_dict.items():
        if b_days_dict[key] != []:
            new_bday_dict[key] = value
        else:
            d.remove(key)
    # print(new_bday_dict)
    # print(d)
    if not new_bday_dict:
        result_if_empty = print('No B-Days for the next week')
        return result_if_empty
    

    # convert numbers of the weekdays to strings and print result

    date_to_check = today_date + timedelta(days=1)
    for i in d:
        while date_to_check.weekday() != i:
            date_to_check += timedelta(days=1)
        weekday_str = date_to_check.strftime('%A')
        print(f"{weekday_str}: {', '.join(new_bday_dict.get(i))}")


get_birthdays_per_week(users)
