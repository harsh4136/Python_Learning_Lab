x = "harsh"                     # string
print(x)
print(type(x))

x = 25                          # int
print(x)
print(type(x))

x = 25.5                        # float 
print(x)
print(type(x))

x = 25j                         # complex
print(x)
print(type(x))

x = ["BMW","Lamborghini", "Ferrari"]        # list 
print(x)
print(type(x))

x = ("BMW","Lamborghini", "Ferrari")        # Tuple
print(x)
print(type(x))

x = range(6)                       # range 
print(x)
print(type(x))

x = {"name" : "Harsh", "age" : 17}       # dict        like key-value pair.
# print(x[name])   -> ouput : Harsh       this is the method from which you can print the value from any key
print(x)
print(type(x))

x = {"Harsh", "Patel", "age : 17"}      # set          , remember there's an differnce between syntax of set and list, tuple.
print(x)
print(type(x))

x = frozenset({"Harsh", "Patel", "age : 17"})
print(x)
print(type(x))

x = True                        # boolean    , which only contains value 0 and 1.
print(x)
print(type(x))

x = b"Harsh"                    # bytes
print(x)
print(type(x))

x = bytearray(5)                # bytearray
print(x)
print(type(x))

x = memoryview(bytes(5))        # memoryview
print(x)
print(type(x))

x = None                         # none       this is included in none datatype.
print(x)
print(type(x))