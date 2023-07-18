"""module creating the database"""
import sqlite3

# Connexion à la base de données (le fichier sera créé s'il n'existe pas)
conn = sqlite3.connect('offres_emploi.db')
c = conn.cursor()

# Création de la table pour stocker les offres d'emploi
c.execute('''CREATE TABLE IF NOT EXISTS offres_emploi (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titre TEXT,
                salaire_max INTEGER,
                salaire_min INTEGER,
                type TEXT
                ville TEXT,
                contenu TEXT
                compagny TEXT
                deja_repondu INTEGER,
                reponse TEXT,
                reference TEXT,
                publication_date TEXT,
                link TEXT

            )''')

# Exemple d'insertion d'une offre d'emploi dans la base de données
job1 = {
    'titre': 'Job Title 1',
    'salaire_max': 5000,
    'salaire_min': 4000,
    'type': 'Full-time',
    'ville': 'Paris',
    'contenu': 'Content 1',
    'compagny': 'Company 1',
    'deja_repondu': 0,
    'reponse': '',
    'reference': 'REF001',
    'publication_date': '2023-07-13',
    'link': 'https://example.com/job1'
}

job2 = {
    'titre': 'Job Title 2',
    'salaire_max': 6000,
    'salaire_min': 4500,
    'type': 'Part-time',
    'ville': 'London',
    'contenu': 'Content 2',
    'compagny': 'Company 2',
    'deja_repondu': 1,
    'reponse': 'Accepted',
    'reference': 'REF002',
    'publication_date': '2023-07-14',
    'link': 'https://example.com/job2'
}

c.execute('''INSERT INTO offres_emploi (titre, salaire_max, salaire_min, type, ville, contenu, compagny, deja_repondu, reponse, reference, publication_date, link)
                  VALUES (:titre, :salaire_max, :salaire_min, :type, :ville, :contenu, :compagny, :deja_repondu, :reponse, :reference, :publication_date, :link)''', job1)

c.execute('''INSERT INTO offres_emploi (titre, salaire_max, salaire_min, type, ville, contenu, compagny, deja_repondu, reponse, reference, publication_date, link)
                  VALUES (:titre, :salaire_max, :salaire_min, :type, :ville, :contenu, :compagny, :deja_repondu, :reponse, :reference, :publication_date, :link)''', job2)

# Validation des modifications
conn.commit()
c.execute('''CREATE INDEX IF NOT EXISTS idx_titre ON offres_emploi (titre)''')
c.execute('''CREATE INDEX IF NOT EXISTS idx_ville ON offres_emploi (ville)''')
c.execute('''CREATE INDEX IF NOT EXISTS idx_salaire ON offres_emploi (salaire_min)''')

# Fermeture de la connexion à la base de données
conn.close()
