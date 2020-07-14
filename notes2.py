def djb2(key):
    hash = 5381

    for char in key:
        hash = ((hash << 5) + hash) + ord(char)
        # hash =((hash * 33) + hash) + ord(char)
    return hash


my_hash_table = [None] * 8


class HashTableItem:
    def __init__(self, key, value, next=None):
        self.key = key
        self.value = value
        self.next = next


def my_hash3(s):
    s_utf8 = s.encode()
    total = 0

    for c in s_utf8:
        # print(c)
        total += c
    return total


def put(key, value):
    hashed_key = my_hash3(key)
    index = hashed_key % len(my_hash_table)
    if my_hash_table[index] != None:
        print('OOps Collision')
    my_hash_table[index] = HashTableItem(key, value)


def get(key):
    hashed_key = my_hash3(key)
    index = hashed_key % len(my_hash_table)
    table_item = my_hash_table[index]
    return table_item.value


def delete(key):
    hashed_key = my_hash3(key)
    index = hashed_key % len(my_hash_table)
    my_hash_table[index] = None


put('hello', 'hello word')
put('world', "we didn't start the fire")
print(my_hash_table)

put('olleh', "fire")


print(get('hello'))

# delete('hello')
print(my_hash_table)


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def find(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return current
            current = current.next
        return None

    def insert_at_tail(self, value):
        node = ListNode(value)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node

    def delete(self, value):
        current = self.head

        if current is None:
            return None

        if current.value == value:
            self.head = current.next
            return current
        else:
            prev = current
            current = current.next

            while current is not None:
                if current.value == value:
                    prev.next = current.next
                    return current
                else:
                    prev = current
                    current = current.next
            return None

    def iterate_nodes(self):
        total = 0
        node = self.head
        while node is not None:
            total += 1
            node = node.next
        return total

    def print_all(self):
        node = self.head
        while node is not None:
            node = node.next
        return node


list = LinkedList()
list.insert_at_tail('A')
list.insert_at_tail('B')
list.insert_at_tail('C')
list.insert_at_tail('D')
list.insert_at_tail('E')
list.insert_at_tail('F')
list.insert_at_tail('G')


# print('find', list.find('C').value)
# print(list.iterate_nodes())
print('print', list.print_all())
# list.delete('C')
# print('find', list.find('C'))
print('list.head.value', list.head.value)
print(list.head.next.value)

node = list.head
while node.next:
    print(node.value)
    node = node.next
    if node.next is None:
        print(node.value)
       
        