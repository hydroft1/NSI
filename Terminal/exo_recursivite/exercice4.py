def bin_s(tab, e):
    if len(tab) == 1: return tab[0] == e
    #
    indice_milieu = len(tab) // 2
    milieu = tab[indice_milieu]
    if milieu == e: return True
    if milieu < e:
        nv_tab = tab[indice_milieu:]
    else:
        nv_tab = tab[0:indice_milieu]
    return bin_s(nv_tab, e)
        

if __name__ == '__main__':
    import doctest
    doctest.testmod()