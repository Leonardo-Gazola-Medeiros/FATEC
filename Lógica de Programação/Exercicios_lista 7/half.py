# H. first_half
# seja uma string s
# retorna a primeira metade da string
# first_half('WooHoo') -> 'Woo'
# first_half('HelloThere') -> 'Hello'
# first_half('abcdef') -> 'abc'

def first_half(s):
    
    if (len(s)%2) != 0:
        return (s[0:((len(s)//2)+1)])
    else:
        return (s[0:((len(s[0:((len(s)//2))])))])
