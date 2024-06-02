# EXERCIE 1
def correspond(mot, mot_a_trous):
    """
    >>> correspond('INFORMATIQUE', 'INFO*MA*IQUE')
    True
    >>> correspond('AUTOMATIQUE', 'INFO*MA*IQUE')
    False
    >>> correspond('STOP', 'S*')
    False
    >>> correspond('AUTO', '*UT*')
    True
    """
    if len(mot) != len(mot_a_trous):
        return False
    for i in range(len(mot)):
        if mot_a_trous[i] != '*' and mot_a_trous[i] != mot[i]:
            return False
    return True
        
# EXERCICE 2
def est_cyclique(plan):
    '''Prend en paramÃ¨tre un dictionnaire `plan` correspondant Ã  
    un plan d'envoi de messages (ici entre les personnes A, B, C,
    D, E, F).
    Renvoie True si le plan d'envoi de messages est cyclique et 
    False sinon.
    >>> est_cyclique({'A':'E','F':'A','C':'D','E':'B','B':'F','D':'C'})
    False
    >>> est_cyclique({'A':'E','F':'C','C':'D','E':'B','B':'F','D':'A'})
    True
    >>> est_cyclique({'A':'B','F':'C','C':'D','E':'A','B':'F','D':'E'})
    True
    >>> est_cyclique({'A':'B','F':'A','C':'D','E':'C','B':'F','D':'E'})
    False
    '''
    expediteur = 'A'
    destinataire = plan[expediteur] 
    nb_destinataires = 1

    while destinataire != expediteur:
        destinataire = plan[destinataire] 
        nb_destinataires += 1 

    return nb_destinataires == len(plan) 
        
if __name__ == '__main__':
    import doctest
    doctest.testmod()