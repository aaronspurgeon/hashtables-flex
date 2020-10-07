def no_dups(s):
    # Your code here
    if len(s) == 0:
        return ''
    cache = {}
    s = [s]
    array = ([i for item in s for i in item.split()])
    my_list = []

    for i in array:
        if i not in cache:
            cache[i] = 1
            my_list.append(i)
    new_string = ' '.join(my_list)
    return new_string


print(no_dups('hello'))


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
