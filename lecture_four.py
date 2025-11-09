# Dictionary and Set

# A dictionary is a collection of key-value pairs, where each key is unique and maps to a value.
liste = {
"kay": "value",
"subject": "python",
}

#Dictionary methods;
#.keys -> returns all the keys in the dictionary;
print(liste.keys())

#.values -> returns all the values in the dictionary;
print(liste.values())

#typecasting to list
print(list(liste.keys()))

#total number of keys
print(len(liste.keys()))

#.items -> returns all the key-value pairs in the dictionary as tuples;
print(liste.items())

le = [1,2,3,4,5,6,7,8,9,10]
print(sum(le))

#.update -> updates the dictionary with new key-value pairs or modifies existing ones;
liste.update({"new_key": "new_value"})
print(liste)


#SET -> A set is an unordered collection of unique items. Sets are defined using curly braces {} or the set() constructor.
collection = {1,2,3,4,5,5,5,6,7,8,9, 8, 2,2,2,2}
print(type(collection))
print(collection)

mySet =set()#empty set

#set methos
#.add -> adds an element to the set;
#.remove -> removes an element from the set;
#.clear -> removes all elements from the set;
#.union -> returns a new set that is the union of two sets;
#.pop -> removes and returns an arbitrary element from the set;
#.intersection -> returns a new set that is the intersection of two sets;
#for an immutable set, we use frozenset()