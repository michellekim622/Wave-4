# Reverse Lookup

def reverseLookup(data, value):
    keys = []
    for key in data:
        if data[key] == value:
            keys.append(key)
    
    return keys

# Demonstrate
def main():
    ItEn = {"Ciao" : "Hello", "BuonGiorno" : "Hello", "uovo" : "egg", "fuoco" : "fire"}
    
    # multiple keys
    print("The Italian words for 'Hello' are: ", reverseLookup(ItEn, "Hello"))
    print("Expected: ['Ciao', 'BuonGiorno']")
    print()

    # one that returns one key
    print("The Italian word for 'fire' is: ", reverseLookup(ItEn, "fire"))
    print("Expected: ['fuoco']")
    print()

    # one that returns no keys
    print("The Italian word for 'dghtf' is: ", reverseLookup(ItEn, "dghtf"))
    print("Expected: []")

if __name__ == "__main__":
    main()
