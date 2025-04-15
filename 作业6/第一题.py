# Given dictionary
dict_demo = {"k1": "v1", "k2": "v2", "k3": "v3"}

print("Keys:")
for key in dict_demo.keys():
    print(key)

print("\nValues:")
for value in dict_demo.values():
    print(value)

print("\nKey-Value Pairs:")
for key, value in dict_demo.items():
    print(f"{key}: {value}")
dict_demo["k4"] = "v4"
dict_demo["k5"] = "v6"
print("\nDictionary after adding new key-value pairs:", dict_demo)
dict_demo["k5"] = "v5"
print("\nDictionary after modifying 'k5':", dict_demo)
dict_demo.clear()
print("\nDictionary after clearing all key-value pairs:", dict_demo)