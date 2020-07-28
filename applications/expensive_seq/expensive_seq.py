# Your code here
# my dict key can be many immutable type including tuple  <-------- decoded hint <------------

# def expensive_seq(x, y, z):
#     # Your code here
#     if x <= 0:
#         return y + z
#     if x > 0:
#         return expensive_seq(x-1,y+1,z) + expensive_seq(x-2,y+2,z*2) + expensive_seq(x-3,y+3,z*3)

cache = {}
def expensive_seq(x, y, z):
    # Your code here
    key = (x, y, z)
    if x <= 0:
        return y + z

    if x > 0 and key not in cache:
        cache[key] = expensive_seq(x-1,y+1,z) + expensive_seq(x-2,y+2,z*2) + expensive_seq(x-3,y+3,z*3)
    
    return cache[key]
 
    
#  d
def rot13(phrase):
     abc = 'abcdefghijklmnopqrstuvwxyz'
     out_phrase = ''

     for i in phrase:
          out_phrase += abc[(abc.find(i)+13) % 26]
     return out_phrase

phrase = ' Va Clguba, n qvpg xrl pna or nal vzzhgnoyr glcr... vapyhqvat nghcyr.'

print(rot13(phrase))

if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
