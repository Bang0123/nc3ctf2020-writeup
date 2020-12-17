extracted = "WFuYiQES5N6Zy\\rnMkFkzU7xQ5cgfsCuK|oCm{D3xDwDWfZLmTQFV5O64OOQ[y:9sixTDys"

converted = ""
for x in extracted:
    converted += chr(ord(x) - 2)
print(converted)

