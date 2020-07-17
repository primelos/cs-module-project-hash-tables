# my_arr = [ 'hi', 'car', 'goat', 'yell', 'hat']


# my_arr[4]

# def my_hash(s):
#     return len(s)

# # print(my_hash('hat'))



# my_alphabet = {'a':0, 'b':1,}
# def my_hash2(s):
#     total = 0
#     for char in s:
#         total += my_alphabet[char]
#     return total

# print('2', my_hash2(my_alphabet))


def my_hash3(s):
    s_utf8 = s.encode()
    total = 0

    for c in s_utf8:
        # print(c)
        total += c
    return total

hello_index = my_hash3('hello') # 532
print('1',hello_index)  # prints 532

my_arr = [None] * 5
# print('len', len(my_arr))
hello_index = hello_index % len(my_arr)   # = 532 % 5 equals 2 means position2 in my_arr
# print('2',hello_index)
my_arr[hello_index] = 'hello'
print(my_arr)

# new add
world_index = my_hash3('sfo') # 552
print(world_index)

world_index = world_index % len(my_arr) #552 % 5 equals 3
print(world_index)
my_arr[world_index] = 'sfo'

print(my_arr)
print(my_arr[world_index])


# insert in to our hash map
key = 'key'
key_index = my_hash3(key) % len(my_arr)

my_arr[key_index] = 'value'

# print('1', my_arr)
# access the value

key_index = my_hash3(key) % len(my_arr)
print(my_arr[key_index])

# #### steps to put
#  say you have a hash function and you have a array and key-value to put in the array
# hash the word  and get some number back from the hash function 
# modulo this number with array length to find the index
# use index to insert word

# ##### steps to get 
# hash the key/word, get some number back from hash function
# modulo with array length to find index
# lookup value at the index , return it 

# ##### dynamic programming 

#  hash function ideal speeds
# in a hash table: fast  we want to look stuff up fast
# to hash passwords and store hashes instead of plaintext passwords : relatively SLOW
