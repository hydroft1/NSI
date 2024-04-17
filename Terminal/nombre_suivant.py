def nombre_suivant(s):
    """
    >>> nombre_suivant('1211')
    '111221'
    >>> nombre_suivant('311')
    '1321'
    >>> nombre_suivant('87754')
    '18271514'
    >>> nombre_suivant('1123765444125')
    '21121317161534111215'
    
    """
    resultat = ''
    chiffre = s[0]
    compte = 1
    
    for i in range(1, len(s)):
        if s[i] == chiffre:
            compte += 1
        else:
            resultat += str(compte) + chiffre
            chiffre = s[i]
            compte = 1
    
    resultat += str(compte) + chiffre
    
    return resultat


if __name__ == '__main__':
    import doctest
    doctest.testmod()