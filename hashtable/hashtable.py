class HashTableEntry: # Like class Node:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.min_capacity = MIN_CAPACITY
        if capacity > self.min_capacity:
            self.capacity = capacity
        else:
            self.capacity = self.min_capacity
        self.bucket = [None] * self.capacity
        self.count = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return self.capacity

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.count / self.capacity
    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here

        # source : https://en.wikipedia.org/wiki/Fowler%E2%80%93Noll%E2%80%93Vo_hash_function#FNV-1_hash

        #     algorithm fnv-1 is
        #     hash := FNV_offset_basis do
        #     for each byte_of_data to be hashed
        #       hash := hash × FNV_prime
        #       hash := hash XOR byte_of_data
        #     return hash 

        #  XOR in python is ^ 
        # source: https://python-reference.readthedocs.io/en/latest/docs/operators/bitwise_XOR.html 

        FNV_offset_basis =  14695981039346656037
        FNV_prime = 1099511628211

        hash = FNV_offset_basis

        for i in key.encode():
            hash = hash * FNV_prime
            hash = hash ^ i
        return hash

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        
        str_key = str(key).encode() # Cast the key to a string and get bytes
         
        hash_value = 5381  # Start from an arbitrary large prime

        for i in key.encode():
            hash_value = (hash_value * 33) + i
        return hash_value

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % len(self.capacity)

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        if self.bucket[index] == None:
            self.bucket[index] = HashTableEntry(key, value)
            self.count += 1
        else:
            current = self.bucket[index]
            while current.next != None and current.key != key:
                current = current.next
            if current.key == key:
                current.value = value
            else:
                new_entry = HashTableEntry(key, value)
                new_entry.next  = self.bucket[index]
                self.bucket[index] = new_entry
                self.count +=1
        if self.get_load_factor() > .7:
            self.resize(self.capacity * 2)


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        if self.bucket[index].key == key:
            if self.bucket[index].next == None:
                self.bucket[index] = None 
                self.count -= 1
            else:
                new_head = self.bucket[index].next
                self.bucket[index].next = None
                self.bucket[index] = new_head
                self.count -= 1
        else:
            if self.bucket[index] == None:
                return None
            else:
                current = self.bucket[index]
                previous = None
                while current.next is not None and current.key != key:
                    previous = current
                    current = current.next
                if current.key == key:
                    previous.next = current.next
                    self.count -= 1
                    return current.value
                else:
                    return None
        if self.get_load_factor() < .2:
            if self.capacity/2 > 8:
                self.resize(self.capacity // 2)
            elif self.capacity > 8:
                self.resize(8)

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        if self.bucket[index] is not None and self.bucket[index].key == key:
            return self.bucket[index].value
        elif self.bucket[index]is None:
            return None
        else:
            current = self.bucket[index]
            while current.next != None and current.key != key:
                current = self.bucket[index].next
            if current == None:
                return None
            else: 
                return current.value

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        prev_table = self.bucket[:]
        self.capacity = new_capacity
        self.bucket = [None] * new_capacity
        for i in range(len(prev_table)):
            if prev_table[i] is not None:
                current = prev_table[i]
                self.put(current.key, current.value)


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")

# my_hash = HashTableEntry('key', 1)
# my_hash.get_num_slots()