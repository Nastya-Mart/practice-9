calls = 0


def count_calls():
    global calls
    calls += 1
    print(f' {calls}')
def string_info(string):
    count_calls()
    if string:
        print(f' {string}')
        print(f' {string.upper()}')
        print(f' {string.lower()}')
    else:
        print('Строка пустая')
def is_contains(string, list_to_search):
    count_calls()
    if string in list_to_search:
        print(f'Строка "{string}" найдена в списке.')
    else:
        print(f'Строка "{string}" не найдена в списке.')
string_info("кот")
string_info("трон")
is_contains("машина", ["мойка", "шрам"])
is_contains("катер", ["стройка", "дом"])
print(f'Общее количество вызовов: {calls}')











