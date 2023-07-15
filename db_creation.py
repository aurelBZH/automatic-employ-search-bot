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
                contenu TEXT,
                deja_repondu INTEGER,
                reponse TEXT
            )''')

# Exemple d'insertion d'une offre d'emploi dans la base de données
offre = {
    'titre': 'Développeur Python',
    'salaire_min': None,
    'salaire_max': None,
    'ville': 'Paris',
    'contenu': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
    'deja_repondu': 0,
    'reponse': ''
}

c.execute('''INSERT INTO offres_emploi
                (titre, salaire_max, salaire_min, ville, contenu, deja_repondu, reponse)
                VALUES (?, ?, ?, ?, ?, ?,?)''',
          (offre['titre'], offre['salaire_max'], offre['salaire_max'], offre['ville'], offre['contenu'], offre['deja_repondu'], offre['reponse']))


# Validation des modifications
conn.commit()
c.execute('''CREATE INDEX IF NOT EXISTS idx_titre ON offres_emploi (titre)''')
c.execute('''CREATE INDEX IF NOT EXISTS idx_ville ON offres_emploi (ville)''')
c.execute('''CREATE INDEX IF NOT EXISTS idx_salaire ON offres_emploi (salaire_min)''')

# Fermeture de la connexion à la base de données
conn.close()