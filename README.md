# KabyleConjugator

**KabyleConjugator** est un outil en Python permettant d'extraire et d'afficher les formes de conjugaison de verbes kabyles à partir d'un fichier JSON (par exemple, `conjugation.json`).

## Fonctionnalités

- **Chargement du fichier JSON** : Le script charge automatiquement le fichier `conjugation.json` situé dans le même répertoire, si aucun chemin n'est spécifié.
- **Recherche de verbe** : Recherchez un verbe en indiquant sa racine.
- **Affichage détaillé** : Affiche toutes les catégories de conjugaison disponibles, y compris les aspects de prétérit, prétérit négatif, aoriste, impératif, participes, et formes intensives.
- **Libellés lisibles** : Les clés internes (ex. `preterite`, `aorist`, etc.) et les pronoms personnels (ex. `firstSingular`) sont convertis en libellés en français pour une meilleure lisibilité.

## Prérequis

- Python 3.x (de préférence Python 3.6 ou plus récent)
- Le fichier `conjugation.json` doit être présent dans le même répertoire que le script, ou spécifié via l'argument.

## Installation

1. Clonez ce dépôt sur votre machine :

   ```bash
   git clone https://github.com/BoFFire/KabyleConjugator.git


**2. Se placer dans le répertoire du projet**

Déplacez-vous dans le dossier cloné :

```bash
cd KabyleConjugator
```

**3. Vérifier la présence du fichier JSON**

Assurez-vous que le fichier `conjugation.json` se trouve dans le même répertoire que le script `kabyleconjugator.py`. Ce fichier doit contenir les données de conjugaison au format JSON.

**4. Exécuter le script**

Pour afficher la conjugaison d'un verbe (par exemple, pour le verbe `nadi`), utilisez la commande suivante :

```bash 
python kabyleconjugator.py nadi
```

**4. Exécuter le script**

Pour afficher la conjugaison d'un verbe (par exemple, pour le verbe `nadi`), utilisez la commande suivante :

```bash
python kabyleconjugator.py nadi
```

***Source***

This `conjugation.json` file source is from : [DigitizedDallet](https://github.com/sferhah/DigitizedDallet) based on [amyag.com](https://www.amyag.com/)
