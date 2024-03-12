def print_menu():
    print('Сервис поиска авиабилетов')
    print('\n')
    print('1 - ввод рейса')
    print('2 - вывод всех рейсов')
    print('3 - поиск рейса по номеру')
    print('0 - завершение работы')
    print('\n')


# prints out all existing flights
def print_all_flights(flights, sep):
    # display message if there are no logged flights
    if not flights:
        print('Информация о рейсах отсутствует')
        return

    print('Информация о рейсе: ')
    flights_strlen = check_symbol_count(flights)
    counter = 0
    for sym in flights:
        if sym == sep and counter < flights_strlen - 1:
            print('\n')
            print('Информация о рейсе: ')
            counter += 1
            continue
        elif sym == sep:
            print('\n')
            continue
        print(sym, end='')
        counter += 1


# function to search a flight by flight number
def search_flight_num(flight_to_find, all_flights, sep):
    # display message is there are no flights logged
    if not all_flights:
        print('Информация о рейсах отсутствует')
        return
    # display message if the flight the user is looking for is not among the logged flights
    if flight_to_find not in all_flights:
        print('Информация о данном рейсе отсутствует')
        return

    flight = ''
    for sym in all_flights:
        if sym == sep and check_flight_num(flight, flight_to_find):
            print(flight)
            break
        elif sym == sep:
            flight = ''
            continue
        flight += sym


# function to check if a flight information contains flight number a user is looking for
def check_flight_num(flight, flight_to_find):
    if flight_to_find in flight:
        return True
    return False


# function to count and return amount of symbols in a string
def check_symbol_count(input_str):
    str_len = 0
    for _ in input_str:
        str_len += 1
    return str_len


# function to check if input string number is positive
def is_positive(input_str):
    if '-' in input_str:
        return False
    else:
        return True


# function to convert alphabetic letters to uppercase
def sym_to_upper(input_str):
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_str = ''
    for s in input_str:
        if s not in alphabet or alphabet.index(s) >= 26:
            new_str += s
        else:
            new_str += alphabet[alphabet.index(s) + 26]
    return new_str


def prompt_flight_num():
    flight_num = input('XXXX - номер рейса: ')
    while check_symbol_count(flight_num) != 4:
        print('Номер рейса должен содержать 4 символа.')
        flight_num = input('XXXX - номер рейса: ')
    return sym_to_upper(flight_num)


def prompt_date():
    date = input('ДД/ММ/ГГГГ - дата рейса: ')
    while check_symbol_count(date) != 10:
        print('Дата рейса должна содержать 10 символов. ')
        date = input('ДД/ММ/ГГГГ - дата рейса: ')
    return date


def prompt_time():
    time = input('ЧЧ:ММ - время вылета: ')
    while check_symbol_count(time) != 5:
        print('Время вылета должно содержать 5 символов.')
        time = input('ЧЧ:ММ - время вылета: ')
    return time


def prompt_duration():
    duration = input('ХХ.ХХ - длительность перелета: ')
    while not is_positive(duration):
        print('Длительность перелета не может быть отрицательной')
        duration = input('ХХ.ХХ - длительность перелета: ')

    while '.' not in duration or check_symbol_count(duration) != 5:
        print('время перелета должна содержать двузначное дробное число')
        duration = input('ХХ.ХХ - длительность перелета: ')
    return duration


def prompt_dep_airport():
    departure_airport = input('ХХХ - аэропорт вылета: ')
    while check_symbol_count(departure_airport) != 3:
        print('Аэропорт вылета должен содержать 3 символа')
        departure_airport = input('ХХХ - аэропорт вылета: ')
    return sym_to_upper(departure_airport)


def prompt_arr_airport():
    arrival_airport = input('ХХХ - аэропорт назначения: ')
    while check_symbol_count(arrival_airport) != 3:
        print('Аэропорт вылета должен содержать 3 символа')
        arrival_airport = input('ХХХ - аэропорт вылета: ')
    return sym_to_upper(arrival_airport)


def prompt_ticket_price():
    ticket_price = input('.ХХ - стоимость билета (> 0): ')
    while not is_positive(ticket_price):
        print('Цена не может быть отрицательной')
        ticket_price = input('.ХХ - стоимость билета (> 0): ')
    return ticket_price


def add_new_flight():
    # prompt and check flight number
    print('Введите данные рейса: ')
    flight_num = prompt_flight_num()

    # add and check date
    date = prompt_date()

    # add and check time
    time = prompt_time()

    # add and check flight duration
    duration = prompt_duration()

    # add and check departure airport
    departure_airport = prompt_dep_airport()

    # add and check arrival airport
    arrival_airport = prompt_arr_airport()

    # add and check ticket price
    ticket_price = prompt_ticket_price()

    flight_info = flight_num + ' ' + date + ' ' + time + ' ' + duration + ' ' + \
                  departure_airport + ' ' + arrival_airport + ' ' + ticket_price + ' '
    print('Информация о рейсе ' + flight_info + ' добавлена')
    return flight_info


# function to add new flight to all flights string
def combine_flight(flight_info, all_flights, sep):
    if not all_flights:
        return flight_info + sep
    return all_flights + flight_info + sep


def main():
    all_flights = None
    separator = '%'
    while True:
        print_menu()
        user_choice = int(input('Введите номер пункта меню: '))
        if user_choice == 1:
            new_flight = add_new_flight()
            all_flights = combine_flight(new_flight, all_flights, separator)
        elif user_choice == 2:
            print_all_flights(all_flights, separator)
        elif user_choice == 3:
            flight_num = sym_to_upper(input('Введите номер рейса в формате ХХХХ: '))
            search_flight_num(flight_num, all_flights, separator)
        elif user_choice == 0:
            exit()


if __name__ == '__main__':
    main()
