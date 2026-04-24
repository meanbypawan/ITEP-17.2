d = {"a": 1, "b": 2, "c": 3,"d":4}
# o/p {1: "a", 2: "b", 3:"c", 4:"d"}

result = {value:key for key,value in d.items()}
print(result)