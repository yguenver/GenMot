# Import pour la génération aléatoire
import random as random



class Generateur(object):
    """ Générateur de mot plausible implémentant un dictionnaire de dictionnaire
    """

    def __init__(self,profondeur):
        self.nbAppear = dict() # Initialise un dictionnaire vide
        self.N = profondeur # Initialise une profondeur
    
    def ajout(self, arbre, caracteres):
        """ Incrémente le nombre d'occurence d'une lettre, le créé si non présent
        """
        if len(caracteres)==1 : # On vérifie qu'on est à la bonne profondeur
            if caracteres[0] in arbre : # On vérifie la présence du  caractère
                arbre[caracteres[0]] += 1 # On l'incrémente s'il existe
            else :
                arbre[caracteres[0]] = 1 # On créé l'entrée sinon
        else :
            if caracteres[0] in arbre : # On vérifie la présence du caractère 
                self.ajout(arbre[caracteres[0]], caracteres[1:])
            else :
                arbre[caracteres[0]] = dict() # On créé le sous dictionnaire avec l'entrée
                self.ajout(arbre[caracteres[0]], caracteres[1:])
        
    def lireMot(self, mot):
        """ Lit un mot et dénombre les occurrences de ses couples de lettre
        """
        for i in range(len(mot)-(self.N-1)): # On parcourt le mot
            caracteres = []
            for y in range(self.N):
                caracteres.append(mot[i+y])
            self.ajout(self.nbAppear, caracteres) # On incrémente le nombre d'occurrence de la lettre
    
    def _estLettre(self, c):
        """ Détermine si un caractère donné est une lettre
        """
        return ("a" <= c <= "z") or ("à" <= c <= "ü")

    def __trouveMot(self,texte,i):
        """ Trouve le premier mot dans une chaîne donnée à partir d'un indice donné.
            Renvoi le mot et l'indice de fin
        """
        mot = " "*(self.N-1) # On démarre par le caractère de début de mot
        while self._estLettre(texte[i].lower()) and i < len(texte): # On parcourt tant qu'on a une lettre
            mot+=texte[i].lower() # On ajoute la lettre au mot
            i+=1
        return mot+" ", i+1 # On ajoute une espace comme caractère de fin de mot

    def lireTexte(self,fichier):
        """ Lit un fichier texte dont le nom est donné en paramètre pour nourrir le dictionnaire
        """
        texte = open("./ProjetPython/"+fichier, "r", encoding="utf8").read()
        i = 0
        while i < len(texte):
            mot, i = self.__trouveMot(texte,i) # On récupère les mots
            if mot != " "*self.N : # On nourri le dictionnaire si le mot n'est pas vide
                self.lireMot(mot)
    
    
    def __trouveLettre(self, caracteres):
        """ Fait la somme des occurrences des lettres possibles suivant une liste de lettres donnée 
            et fait un tirage uniforme sur cette somme
        """
        somme = 0
        arbre = self.nbAppear
        for c in caracteres :
            arbre = arbre[c]
        
        for occurrence in arbre.values(): # Pour toutes les occurrences dans le dictionnaire d'une lettre
            somme += occurrence # On l'ajoute à la somme
        
        return random.randint(0,somme) # On renvoi une valeur aléatoire entre 0 et la somme
        
    def caractereSuivant(self, caracteres):
        """ Prend une liste de caractère et tire au sort le caractère suivant
        """
        alea = self.__trouveLettre(caracteres) # On fait un tirage aléatoire
        i = 0
        arbre = self.nbAppear
        for c in caracteres :
            arbre = arbre[c]
            
        occurences = list(arbre.values())
        while alea > occurences[i]: # Si le tirage est plus grand que le nombre d'occurence d'une lettre
            alea-= occurences[i] # On soustrait au tirage le nombre d'occurences de cette lettre
            i+=1
        return list(arbre.keys())[i] # On renvoi la lettre tiré
    
    def genereMot(self, premiereLettre=' '):
        """ Génère un mot commançant par une lettre donnée. Trouve la première lettre suivant le caractère de début de mot si non spécifié
        """
        mot = ' '*(self.N-2) + premiereLettre
        if len(mot)==(self.N-1) :
            mot+=self.caractereSuivant(mot[0-(self.N-1):])
        while(mot[-1]!=' ') : # Tant que la dernière lettre n'est pas le caractère de fin de mot ou que le mot est vide
            mot+=self.caractereSuivant(mot[0-(self.N-1):]) # On ajoute la lettre suivante en fonction de la dernière lettre actuelle
        return mot[(self.N-1):-1] if mot[self.N-2]==' ' else mot[(self.N-2):-1] # Renvoi la mot, sans espace si première lettre non spécifiée
