#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 22:22:26 2022

@author: Perrine
"""

import chardet
import matplotlib.pyplot as plt

# Définis le nom du dossier qui contient les fichiers à normaliser
data_folder = '../DATA/'
# Liste des noms des trois textes à étudier
filenames = ["80jours_unitex_gramlab_v3_2.txt", "103-0_jv80_english_gutenberg_prj.txt", "jv80jours_ABU_unformated_iso88591.txt"]
# Liste du nom du lexique
lexique = ["dimaju-4.1.1_utf8.txt"]
# Les 3 phrases à annoter
phrases = ["On ne l'avait jamais vu ni à la Bourse, ni à la Banque, ni dans aucun des comptoirs de la Cité. ", "Ni les bassins ni les docks de Londres n'avaient jamais reçu un navire ayant pour armateur Phileas Fogg.", "En tout cas, il n'était prodigue de rien, mais non avare, car partout où il manquait un appoint pour une chose noble, utile ou généreuse, il l'apportait silencieusement et même anonymement. "]


# Pour chaque nom de fichier dans la liste "filenames"
for filename in filenames:
    # Ouvre le fichier en lecture
    with open(data_folder+filename, 'rb') as infile:
        # Détecte l'encodage du fichier
        encoding = chardet.detect(infile.read())['encoding']

    # Si l'encodage n'est pas utf-8, lisez le contenu du fichier dans l'encodage détecté et écrivez-le de nouveau dans utf-8
    if encoding != 'utf-8':
        content = ""
        # Ouvre le fichier en lecture dans l'encodage détecté
        with open(data_folder+filename, 'r', encoding=encoding) as infile:
            # Lis le contenu du fichier
            content = infile.read()
        # Ouvre le fichier en écriture en utf-8
        with open(data_folder+filename, 'w', encoding='utf-8') as outfile:
            # Écris le contenu dans le fichier en utf-8
            outfile.write(content)


# Ouvre le fichier 0 en lecture
with open(data_folder+filenames[0], 'r', encoding='utf-8') as infile:
    # Initialise les variables qui stockeront les données et les métadonnées
    data0 = []
    metadata0 = {}
    # Initialise une variable qui indique si les données ont été trouvées
    data_found0 = False
    # Pour chaque ligne du fichier, extraire les données et les métadonnées
    for line in infile:
        if line.startswith('Chapitre I'):
            data_found0 = True
        # Si les données ont été trouvées et que la ligne commence par " FIN", cela signifie que les données se sont terminées
        elif data_found0 and line.startswith('FIN'):
            # Initialise une variable qui indique que les données se sont terminées
            data_found0 = False
        # Si les données ont été trouvées, ajoute la ligne aux données
        elif data_found0:
            data0.append(line)
print('data :', filenames[0], data0)
print('metadata :', filenames[0], metadata0)

# Ouvre le fichier 1 en lecture
with open(data_folder+filenames[1], 'r', encoding='utf-8') as infile:
    # Initialise les variables qui stockeront les données et les métadonnées
    data1 = []
    metadata1 = {}
    # Initialise une variable qui indique si les données ont été trouvées
    data_found1 = False
    # Pour chaque ligne du fichier, extraire les données et les métadonnées
    for line in infile:
        # Si la ligne commence par "Title: ", extraire le titre et l'ajoute aux métadonnées
        if line.startswith('Title: '):
            metadata1['titre'] = line[7:].strip()
        # Si la ligne commence par "Author: ", extraire l'auteur et l'ajoute aux métadonnées
        elif line.startswith('Author: '):
            metadata1['auteur'] = line[8:].strip()
        # Si la ligne commence par "Translator: ", extraire le traducteur et l'ajoute aux métadonnées
        elif line.startswith('Translator: '):
            metadata1['traducteur'] = line[12:].strip()
        # Si la ligne commence par "Release Date: ", extraire la date de sortie et l'ajoute aux métadonnées
        elif line.startswith('Release Date: '):
            metadata1['date de realisation'] = line[14:].strip()
        # Si la ligne commence par "Language: ", extraire la langue et l'ajoute aux métadonnées
        elif line.startswith('Language: '):
            metadata1['langue'] = line[10:].strip()
        # Si la ligne commence par "*** START OF THE PROJECT GUTENBERG EBOOK", cela signifie que les données commencent
        elif line.startswith('*** START OF THE PROJECT GUTENBERG EBOOK'):
            # Initialise une variable qui indique si les données ont été trouvées
            data_found1 = True
        # Si les données ont été trouvées et que la ligne commence par "*** END OF THE PROJECT GUTENBERG EBOOK", cela signifie que les données se sont terminées
        elif data_found1 and line.startswith('*** END OF THE PROJECT GUTENBERG EBOOK'):
            # Initialise une variable qui indique que les données se sont terminées
            data_found1 = False
        # Si les données ont été trouvées, ajoutez la ligne aux données
        elif data_found1:
            data1.append(line)

# Affiche les données et les métadonnées extraites
print('data : ', filenames[1], data1)
print('metadata :', filenames[1], metadata1)



# Ouvre le fichier 2 en lecture
with open(data_folder+filenames[2], 'r', encoding='utf-8') as infile:
    # Initialise les variables qui stockeront les données et les métadonnées
    data2 = []
    metadata2 = {}
    # Initialise une variable qui indique si les données ont été trouvées
    data_found2 = False
    # Pour chaque ligne du fichier, extraire les données et les métadonnées
    for line in infile:
        if line.startswith('<AUTEUR'):
            metadata2['auteur'] = line[8:].strip().replace('>', '')
        # Si la ligne commence par "<IDENT_AUTEURS ", extraire l'identification de l'auteur et l'ajoute aux métadonnées
        elif line.startswith('<IDENT_AUTEURS '):
            metadata2['identification de l\'auteur'] = line[14:].strip().replace('>', '')
        # Si la ligne commence par "<TITRE ", extraire le titre et l'ajoute aux métadonnées
        elif line.startswith('<TITRE '):
            metadata2['titre'] = line[6:].strip().replace('>', '')
        # Si la ligne commence par "<IDENT ", extraire l'identification et l'ajoute aux métadonnées
        elif line.startswith('<IDENT '):
            metadata2['identification'] = line[6:].strip().replace('>', '')
        # Si la ligne commence par "<COPISTE ", extraire l'identification et l'ajoute aux métadonnées
        elif line.startswith('<COPISTE '):
            metadata2['copiste'] = line[9:].strip().replace('>', '')
        # Si la ligne commence par "<IDENT_COPISTES ", extraire l'identification et l'ajoute aux métadonnées
        elif line.startswith('<IDENT_COPISTES '):
            metadata2['identification du copiste'] = line[15:].strip().replace('>', '')
        # Si la ligne commence par "<ARCHIVE ", extraire l'identification et l'ajoute aux métadonnées
        elif line.startswith('<ARCHIVE '):
            metadata2['adresse de l\'archive'] = line[8:].strip().replace('>', '')
        # Si la ligne commence par "<VERSION ", extraire l'identification et l'ajoute aux métadonnées
        elif line.startswith('<VERSION '):
            metadata2['version'] = line[9:].strip().replace('>', '')
        # Si la ligne commence par "<DROITS ", extraire l'identification et l'ajoute aux métadonnées
        elif line.startswith('<DROITS '):
            metadata2['droits'] = line[8:].strip().replace('>', '')
        # Si la ligne commence par "<GENRE ", extraire l'identification et l'ajoute aux métadonnées
        elif line.startswith('<GENRE '):
            metadata2['genre'] = line[6:].strip().replace('>', '')
        # Si la ligne commence par "------------------------- DEBUT DU FICHIER tdm80j2 --------------------------------", , cela signifie que les données commencent
        elif line.startswith('------------------------- DEBUT DU FICHIER tdm80j2 --------------------------------'):
            # Initialise une variable qui indique si les données ont été trouvées
            data_found2 = True
        # Si les données ont été trouvées et que la ligne commence par "                               FIN \n", cela signifie que les données se sont terminées
        elif data_found2 and line.startswith('                               FIN \n'):
            # Initialise une variable qui indique que les données se sont terminées
            data_found2 = False
        # Si les données ont été trouvées, ajoutez la ligne aux données
        elif data_found2:
            data2.append(line)
# Affichez les données et les métadonnées extraites
print('data : ', filenames[2],  data2)
print('metadata : ', filenames[2],  metadata2)




# Importer le dictionnaire de lexique
compt = 0
text = 0
caract_dist_dic = {}
token_dist_dic = {}
for file in filenames:
    # Ouvrir le fichier actuel en lecture
    with open(data_folder + file, 'r', encoding='utf-8') as f:
        # Initialiser un nouveau dictionnaire pour le texte actuel
        current_text_dic = {}
        current_token_dic = {}
        punctuation_marks = ['.', ',', '!', '?', ':', ';', '"', '/', '(', ')', ' ', '', '“', '”', '[', ']', '«', '»', '°', '<', '>']
        # Pour chaque ligne dans le fichier
        for line in f:
            # Pour chaque caractère dans la ligne
            for caract in line:
                if caract in punctuation_marks:
                    continue
                # Si le caractère n'est pas déjà dans le dictionnaire, l'ajouter avec une fréquence de 1
                if caract not in current_text_dic.keys():
                    current_text_dic[caract] = 1
                    # Sinon, incrémenter la fréquence de 1
                else:
                    current_text_dic[caract] += 1

            # Diviser la ligne en tokens (mots ou parties de mots)
            token_line = line.split()
            # Pour chaque token dans la ligne
            for token in token_line:
                for punctuation_mark in punctuation_marks:
                    token = token.replace(punctuation_mark, '')
                if token in punctuation_marks:
                    continue
                # Si le token n'est pas déjà dans le dictionnaire, l'ajouter avec une fréquence de 1
                if token not in current_token_dic.keys():
                    current_token_dic[token] = 1
                # Sinon, incrémenter la fréquence de 1
                else:
                    current_token_dic[token] += 1

        # Organiser le dictionnaire du texte actuel par ordre décroissant de fréquence
        current_text_dic = sorted(current_text_dic.items(), key=lambda x: x[1], reverse=True)
        current_token_dic = sorted(current_token_dic.items(), key=lambda x: x[1], reverse=True)

        # Ajouter le dictionnaire du texte actuel au dictionnaire global
        caract_dist_dic[text] = current_text_dic
        # Afficher les caractères et leur fréquence dans le texte actuel
        print('Caractères texte : ', text, '\n', caract_dist_dic[text])
        token_dist_dic[text] = current_token_dic
        # Afficher les tokens et leur fréquence dans le texte actuel
        print('Token texte : ', text, '\n', token_dist_dic[text])

        # Récupération des tokens et de leurs fréquences dans le premier texte
        tokens, frequencies = zip(*token_dist_dic[text])

        # Tracé de l'histogramme
        plt.title("Distribution des tokens dans le texte " + str(text))
        plt.bar(tokens, frequencies)
        plt.axis([0, 10, 0, 4000])
        plt.show()

    # Ouvrir le fichier en mode écriture
    with open('../DATA/frequences_texte_{}.txt'.format(text), 'w') as f:
        # Écrire les fréquences de caractères dans le fichier
        f.write("Fréquences de caractères pour le texte {}:\n".format(text))
        for char, freq in current_text_dic:
            f.write("{} : {}\n".format(char, freq))

        # Écrire les fréquences de tokens dans le fichier
        f.write("Fréquences de tokens pour le texte {}:\n".format(text))
        for token, freq in current_token_dic:
            f.write("{} : {}\n".format(token, freq))

    # Incrémenter le compteur de 1
    compt += 1
    text += 1


# Importation du Lexique
# Ouvre le fichier de lexique en lecture
with open(data_folder+lexique[0], 'r', encoding='utf-8') as f:
    # Définit les séparateurs de mots et d'étiquettes
    mot_sep = "\t"
    etiquette_sep = "\t"
    # Crée un dictionnaire vide qui stockera les mots et leurs étiquettes grammaticales
    lexique = {}
    # Pour chaque ligne dans le fichier, ajoute le mot et ses étiquettes grammaticales au dictionnaire
    for ligne in f:
        index_etiquette = ligne.find(etiquette_sep)
        mot = ligne[0:index_etiquette]
        etiquettes = ligne[index_etiquette:].strip().split(etiquette_sep)
        lexique[mot] = etiquettes

# Importe le fichier de lexique et le stocke dans un dictionnaire
proper_nouns_dic = {}
for text, token_freq in token_dist_dic.items():
    with open("../DATA/SBP_text_%d.txt" % text, "w") as etiquetage:
        printed_words = set()
        # Ouvre le fichier en lecture
        for mot, _ in token_freq:
            # Pour chaque ligne dans le fichier
            if mot in lexique:
                # Si le mot a l'étiquette "SBP:sg" et n'a pas encore été imprimé
                if "SBP:sg" in lexique[mot] or "SBP:pl" in lexique[mot] and mot not in printed_words:
                    # Ajoute le mot à la variable "mot_etiq"
                    mot_etiq = '%s\n' % mot
                    # Écrit "mot_etiq" dans le fichier txt
                    etiquetage.write(mot_etiq)
                    # Ajoute le mot à l'ensemble "printed_words"
                    printed_words.add(mot)
        proper_nouns_dic[text] = sorted(printed_words, key=lambda x: x.lower())
# Affiche l'ensemble trié
print(proper_nouns_dic)

# Comparaison avec la liste des pays en anglais
english_country_nouns = ["Japan", "England", "China", "France", "Great-Britain", "India", "Holland", "Cambodia", "Malaysia", "Mexico", "Peru", "Chili", "Brazil", "Israel", "Scandinavia", "Germany"]
printed_country = set()
with open("../DATA/frequences_texte_1.txt", "r") as f:
    for line in f:
        # Pour chaque mot dans la ligne
        for mot in line.split():
            # Si le mot est dans la liste "english_country_nouns" et n'a pas encore été imprimé
            if mot in english_country_nouns and mot not in printed_country:
                # Ajoute le mot à l'ensemble "printed_country"
                printed_country.add(mot)

# Ouvre le fichier en mode écriture
with open("../DATA/english_country.txt", "w") as english_country:
    # Écrit chaque mot de l'ensemble dans le fichier "english_country.txt"
    for mot in printed_country:
        english_country.write(mot + "\n")

# Affiche l'ensemble
print(printed_country)

# Pour chaque phrase dans la liste
for phrase in phrases:
    annotations = []
    mots = []
    mot_temp = ""
    for caractere in phrase:
        # Si le caractère est une lettre, un chiffre, une apostrophe ou un tiret
        if caractere.isalpha() or caractere.isdigit() or caractere == "'" or caractere == "-":
            # Ajouter le caractère au mot en cours de traitement
            mot_temp += caractere
        else:
            # Si un mot est en cours de traitement
            if mot_temp:
                # Si l'apostrophe est présente dans le mot
                if "'" in mot_temp:
                    # Séparer le mot autour de l'apostrophe
                    index_apostrophe = mot_temp.index("'")
                    mot1 = mot_temp[:index_apostrophe+1]
                    mot2 = mot_temp[index_apostrophe+1:]
                    # Ajouter les deux morceaux séparés dans la liste des mots
                    mots.append(mot1)
                    mots.append(mot2)
                else:
                    # Sinon, ajouter le mot complet dans la liste des mots
                    mots.append(mot_temp)
            # Réinitialiser le mot en cours de traitement
            mot_temp = ""
            # Ajouter le caractère dans la liste des mots
            mots.append(caractere)

    # Pour chaque mot dans la phrase
    for mot in mots:
        if mot.isspace():
            # Si c'est un espace, on ignore et on passe au caractère suivant
            continue
        # Si le mot est présent dans le lexique
        if mot in lexique:
            # Récupère les étiquettes grammaticales du mot dans le lexique
            etiquettes = lexique[mot]
            # Ajoute le mot et ses étiquettes grammaticales à la liste d'annotations
            annotations.append((mot, etiquettes))
        # Si le mot n'est pas dans le lexique
        else:
            # Ajoute le mot avec l'étiquette "INCONNU" à la liste d'annotations
            annotations.append((mot, ["INCONNU"]))

    # Convertir les annotations en chaîne de caractères
    annotations_str = ["{} ({})".format(annotation[0], " ".join(annotation[1])) for annotation in annotations]
    # Concaténer les chaînes de caractères en une seule chaîne de caractères, séparées par des retours à la ligne
    annotations_str = "\n".join(annotations_str)
    # Ouvrir le fichier en mode écriture
    with open('../DATA/phrases_annotations.txt', 'a') as f:
        # Écrire la phrase dans le fichier
        f.write("\n" + phrase + "\n")
        # Écrire les annotations dans le fichier, en ajoutant un retour à la ligne à la fin
        f.write(annotations_str + "\n")


# Annotation du premier texte
with open(data_folder + filenames[0], 'r') as f:
    # Lire le contenu du fichier
    texte = f.read()

# Séparer le texte en phrases
phrases = texte.split('\n')
frequences = {}

# Pour chaque phrase, réaliser l'annotation
for phrase in phrases:
    annotations = []
    mots = []
    mot_temp = ""
    for caractere in phrase:
        if caractere.isalpha() or caractere.isdigit() or caractere == "'" or caractere == "-":
            mot_temp += caractere
        else:
            if mot_temp:
                if "'" in mot_temp:
                    index_apostrophe = mot_temp.index("'")
                    mot1 = mot_temp[:index_apostrophe+1]
                    mot2 = mot_temp[index_apostrophe+1:]
                    mots.append(mot1)
                    mots.append(mot2)
                else:
                    mots.append(mot_temp)
            mot_temp = ""
            mots.append(caractere)

    for mot in mots:
        if mot.isspace():
            continue
        if mot in lexique:
            etiquettes = lexique[mot]
            annotations.append((mot, etiquettes))
        else:
            annotations.append((mot, ["INCONNU"]))

    annotations_str = ["{} ({})".format(annotation[0], " ".join(annotation[1])) for annotation in annotations]
    annotations_str = "\n".join(annotations_str)

    with open('../DATA/texte0_annotations.txt', 'a') as f:
        f.write("\n" + phrase + "\n")
        f.write(annotations_str + "\n")

    for mot, etiquettes in annotations:
        for etiquette in etiquettes:
            if etiquette not in frequences:
                frequences[etiquette] = 1
            else:
                frequences[etiquette] += 1

with open("../DATA/etiquettes_frequence.txt", "w") as f:
    # Afficher les résultats de l'étude de fréquence
    f.write("Étude de fréquence des étiquettes :\n")
    for etiquette, frequence in frequences.items():
        print("- {} : {} occurrences\n".format(etiquette, frequence))
        f.write("- {} : {} occurrences\n".format(etiquette, frequence))

frequences_triees = sorted(frequences.items(), key=lambda x: x[1], reverse=True)
