# B. string_splosion
# string_splosion('Code') -> 'CCoCodCode'
# string_splosion('abc') -> 'aababc'
# string_splosion('ab') -> 'aab'

def string_splosion(s):
    
    exploded = []
    result = str()
    
    #appending the string to a list.
    for w in s:
        exploded.append(w)
        
    #creating a function to return the components of the list in the required order [0:n]+[0:n+1]+....[0:n+k]
    for k in range(len(exploded[:])):
        for n in range(k+1):
            result = result + exploded[n]

    return result
