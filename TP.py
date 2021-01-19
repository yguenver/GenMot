from Generateur import Generateur
# Import pour les tests de mesure temporelle
import time

N = 3
texte = "notredame"


g = Generateur(N)

débutLectureG1 = time.time()
g.lireTexte(texte+".txt")
finLectureG1 = time.time()

print(" Temps de construction G : ",
      '%.3f'%(finLectureG1 - débutLectureG1),'sec')

print(texte+":")
print("  N={0:35}".format(str(N)))
débutGeneration = time.time()
for i in range(10):
    mot = g.genereMot()
    print("  Mot aléatoire : {0:20}".format(mot))

finGeneration = time.time()
print(" Temps de génération : ",
      '%.4f'%(finGeneration - débutGeneration),"sec")
