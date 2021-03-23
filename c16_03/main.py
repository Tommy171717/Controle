note1 = ('eleve1', 'math', 13)
note2 = ('eleve1', 'physique', 15)
note3 = ('eleve1', 'math', 13)
note4 = ('eleve1', 'eco', 12)
note5 = ('eleve1', 'eco', 13)
note6 = ('eleve1', 'math', 12)
note7 = ('eleve2', 'math', 13)
note8 = ('eleve2', 'math', 14)

notes = [note1, note2, note3, note4, note5, note6,note7,note8]
notes_eleves1 = [note1, note2, note3, note4, note5, note6]

moyenne_eleve1 = (notes[0][2]+notes[1][2]+notes[2][2]+notes[3][2]+notes[4][2]+notes[5][2])/6
print("la moyenne de l'élève 1 = ",moyenne_eleve1)

print(moyenne_eleve1)

#4ab
moyenne_eleve1math = (notes[0][2]+notes[2][2]+notes[5][2])/3
print(moyenne_eleve1math)

#4ac
def moyenne_tuple(notes,eleve,matiere):
  s=0
  i = 0
  for x in notes:
    if x[0] == eleve and x[1]== matiere:
      s= s+x[2]
      i = i +1
  moy = s / i 
  return moy

print(moyenne_tuple(notes,'eleve1','math'))

#Que se passe-t-il si on fait une faute de frappe dans la saisie d'une matière ?
# Le shell ne trouve pas la matière et signale une erreur de syntaxe

#Que se passe-t-il si quelqu'un rentre une chaine de caractère au lieu d'une nombre '14' au lieu de 14 ?
#Le shell renvoie une erreur pour dire que la chaine de caractère n'est pas définie

#Que se passe-t-il si on veut ajouter des coefficient aux notes et aux matières ?
#Ca ne marchera pas car on a pas rentré de paramètre pour les coefficients dans la fonction moyenne_tuples

#Que se passe-t-il si on a un triplet qui n'est pas du tout une note ?
# Il va afficher une erreur car ce n'est pas possible de faire une moyenne avec une chose qui n'est pas une note

#Qst 5 
class Note:
  instances = []  
  def __init__(self, eleve, matiere, valeur): #La méthode pour créer un objet
    self.eleve = eleve
    self.matiere = matiere
    self.valeur = valeur

    Note.instances.append(self)

  def __str__(self):
    return f"{self.__class__.__name__}('{self.eleve}','{self.matiere}','{self.valeur}')"


  @classmethod #attention !
  def vider(cls):
    cls.instances = []

  @classmethod #attention !
  def moyenne(cls):
    return(sum(n.valeur for n in cls.instances)/len(cls.instances))






if __name__ == '__main__':
    note1 = ('eleve1', 'math', 13)
    note2 = ('eleve1', 'physique', 15)
    note3 = ('eleve1', 'math', 13)
    note4 = ('eleve1', 'eco', 12)
    note5 = ('eleve1', 'eco', 13)
    note6 = ('eleve1', 'math', 12)
    note7 = ('eleve2', 'math', 13)
    note8 = ('eleve2', 'math', 14)


    notes = [note1, note2, note3, note4, note5, note6,note7,note8]

    notes_elv1 = [note for note in notes if note[0] == 'eleve1']

    print(notes_elv1)

    print(sum(note[2] for note in notes_elv1)/len(notes_elv1))

    notes_elv1_math = [n for n in notes_elv1 if n[1] == 'math']

    print(sum(n[2] for n in notes_elv1_math)/len(notes_elv1_math))


    print(moyenne_tuple(notes, 'eleve1', 'math'))


    onote = Note('eleve1', 'maths', 13)





    onotes = [Note(eleve, matiere,  valeur) for eleve, matiere, valeur in notes]




    onotes = [Note(*note) for note in notes]



    Note.vider()



    onotes = [Note(*note) for note in notes]

    print(Note.moyenne())