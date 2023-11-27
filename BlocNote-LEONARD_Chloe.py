#Bloc-notes en POO
    
class Note:
    def __init__(self, titre, contenu):
        self.titre = titre
        self.contenu = contenu


class Note_Importante(Note):
    def __init__(self, titre, contenu, importance):
        super().__init__(titre, contenu)
        self.importance = True

class Blocnotes:
    def __init__(self):
        self.notes = []

    def creation_note(self, titre, contenu):
        if "IMPORTANT" in contenu :            
            note = Note_Importante(titre, contenu, True)
        else :
            note = Note(titre, contenu)
        self.notes.append(note)
            
    def modifier_note(self, titre, nouv_contenu):
        for note in self.notes:
            if note.titre == titre:
                note.contenu = nouv_contenu
                break

    def rechercher_note(self):
        titre = input("Entrez le titre de la note que vous cherchez : ")
        for note in self.notes:
            if note.titre == titre:
                print("Titre : ", note.titre)
                print("Contenu : ", note.contenu)
                print(" ")
                break
        print("Note introuvable ! ")

    def sauvegarde_quitter(self):
        print("sauvegarde en cours")
        fichier = open("sauvegarde.txt", "w")
        for note in self.notes:    
            if "IMPORTANT" in note.contenu :
                fichier.write("\033[31m" + f'{note.titre} \n'+ "\033[0m" +  f'{note.contenu} \n') #ecrit le titre en rouge si la note est importante 
            else :
                fichier.write("%s\n%s\n" % (note.titre, note.contenu))
        fichier.close()
        print("sauvegarde terminé")
        
    def voir_notes(self):
        #note vide
        if not self.notes:
            print("Aucune note n'est disponible!")
            return
        print("Voici les notes enregistrés")
        for note in self.notes:
            print(f"Titre: {note.titre}")
            print(f"Contenu: {note.contenu}")
            print(" ")            

    def supprimer_note(self, titre):
        for note in self.notes:
            if note.titre == titre:
                self.notes.remove(note)
                break

test = Blocnotes()     
print("\t1- Créer une nouvelle note.")
print("\t2- Modifier une note existante.")
print("\t3- Rechercher une note.")
print("\t4- Sauvegarder.")
print("\t5- Afficher toutes les notes.")
print("\t6- Supprimer une note.")
print("\t7- Quitter.")
choix = int(input("Choisir l'option souhaitée :"))

while choix != 7:
    if choix == 1:
        new_titre = input("Entrer le titre de votre note : ")
        new_contenu = input("Entrer le contenu de votre note : ")
        test.creation_note(new_titre, new_contenu)
    elif choix == 2:
        old_titre = input("Entrez le titre de la note que vous voulez modifier : ")
        new_titre = input("Modifiez le titre : ")
        new_contenu = input("Modifiez le contenu : ")
        note = Note(old_titre, new_contenu)
        test.modifier_note(note)
    elif choix == 3:
        recherche = input("Recherchez une note par son titre : ")
        resultat = test.rechercher_note(recherche)
        if resultat is None:
            print("La note est introuvable")
        else:
            print(resultat)
    elif choix == 4:
        test.sauvegarde_quitter()
        break
    elif choix == 5:
        test.voir_notes()
    elif choix == 6:
        sup_titre = input("Supprimez une note par son titre : ")
        test.supprimer_note(sup_titre)

    print("\t1- Créer une nouvelle note.")
    print("\t2- Modifier une note existante.")
    print("\t3- Rechercher une note.")
    print("\t4- Sauvegarder.")
    print("\t5- Afficher toutes les notes.")
    print("\t6- Supprimer une note.")
    print("\t7- Quitter.")
    choix = int(input("Choisir l'option souhaitée :"))

"""
test = Blocnotes()
test.creation_note("Salutations", "Bonjour le monde!")
test.voir_notes()
test.creation_note("NOTE 2", "note2")
test.modifier_note("Salutations", "Salut à tous!")
test.voir_notes()
test.rechercher_note()
test.voir_notes()
test.sauvegarde_quitter()
#test.supprimer_note("Salutations")
test.voir_notes() 
"""

from abc import *

class BlocNoteComptage(ABC):
    @abstractmethod
    def calculer_somme(self):
        pass

class Chiffre(BlocNoteComptage):
    def __init__(self, chiffre):
        self.chiffre = chiffre

    def __str__(self):
        return str(self.chiffre)

    def calculer_somme(self):
        return self.chiffre

class BlocNoteAvecChiffres(BlocNoteComptage):
    def __init__(self, chiffres):
        self.chiffres = chiffres

    def __str__(self):
        resultat = ""
        for i in range(len(self.chiffres)):
            resultat += str(self.chiffres[i]) + "\n"
        return resultat

    def calculer_somme(self):
        somme = 0
        for chiffre in self.chiffres:
            somme += chiffre.calculer_somme()
        return somme
    
