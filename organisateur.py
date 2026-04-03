"""
Code python pour trié mon superbe bureau, et aussi pour avoir une todo bien pratique
Amir HILALY
"""

import os, sys
import shutil

#if (len(sys.argv) != 2):
#    print("PAS BON")


def trier():
    print(f"Voulez-vous trier votre répertoire actuel ? y/n\n{cwd}")
    reponse = input().lower()

    if reponse not in ('y', 'n'):
        print('Veuillez ne rentrez que y ou n.')
        return
    
    if (reponse == 'n'):
        return
    
    REGLES = {".pcap": "captures_shark/", ".log": "logs/", ".csv": "rapports/", ".json": "rapports/", ".py": "scripts/", ".sh": "scripts/", ".zip": "archives/"}

    # Pour recup le nom de ce fichier
    file_name =  os.path.basename(sys.argv[0])

    compte = 0
    scanned = os.scandir(".")

    for f in scanned:
        if f.is_file():
            compte += 1
            # print(f'{compte} : {f.name}')
            valeur = '.' + f.name.split(".")[-1]

            try:
                new_path = cwd + '/' + REGLES[valeur] + f.name
                old_path = cwd + '/' + f.name

                # Check pour ne pas bouger notre fichier actuel
                if (f.name != file_name):
                    print(f'Direction -> {new_path}')
                    shutil.move(old_path, new_path)

                new_path = ''
                old_path = ''

            except:
                print(f'{f.name} n a pas de dossier pour lui')
    print(f'Total : {compte} fichier(s)')



def to_do_list():
    tasks = []
    try:
        with open("data.txt", "r") as f:
            tasks = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        pass

    while True:
        print("1 - Voir")
        print("2 - Ajouter")
        print("3 - Supprimer")
        print("4 - Quitter")
        choice = input("-> ").strip()

        if choice == "1":
            for i, t in enumerate(tasks, 1):
                print(f"Tâche numéro {i} : {t}")

        elif choice == "2":
            tasks.append(input("Tâche: ").strip())
            open("data.txt", "w").write("\n".join(tasks))

        elif choice == "3":
            n = int(input("Numéro: ")) - 1

            if (n <= 0 or n >= len(tasks)):
                print('Invalide)')
            else:
                tasks.pop(n)
                open("data.txt", "w").write("\n".join(tasks))

        elif choice == "4":
            break

        else:
            print('Invalide')





if __name__ == '__main__':

    # Pour recup' le path du fichier actuel
    cwd = os.getcwd()

    while True:
        print("\nMulti-script:")
        print("1 - Trier")
        print("2 - To-do List")
        print("3 - Quitter")

        choice = input("Choisir une option: ").strip()

        if choice == '1':
            trier()
        elif choice == '2':
            to_do_list()
        
        elif choice == '3':
            break

        else:
            print('Invalide')