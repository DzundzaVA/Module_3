calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(x):
    global calls
    x = (len(x), x.upper(), x.lower())
    count_calls()
    return x
def is_contains(k,l):
    for i in range(len(l)):
        l.append(l[i].lower())
    if k.lower() in l:
        is_contains_ = True
    else:
        is_contains_ = False
    count_calls()
    return is_contains_

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)