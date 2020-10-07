def word_count(s):
    # Your code here
    cache = {}
    ignore = '":;,.-+=/\\|[]{}()*^&'
    lower = s.lower()

    for i in lower:
        if i in ignore:
            lower = lower.replace(i, '')
    words = lower.split()
    for j in words:
        if j not in cache:
            cache[j] = 1
        else:
            cache[j] += 1
    return cache


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
