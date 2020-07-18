def word_count(s):
    # Your code here
    my_collection ={}
    # info for maketrans
    # https://www.programiz.com/python-programming/methods/string/maketrans

    lower_s = s.translate(str.maketrans('str', 'str', '":;,.-+=/\\|[]{}()*^&')).lower().split()
    for i in lower_s: 
        if i in my_collection:
            my_collection[i] += 1
        else:
            my_collection[i] = 1
    return my_collection

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello    hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))