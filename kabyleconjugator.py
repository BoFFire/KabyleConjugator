#!/usr/bin/env python3
import json
import argparse
import sys
import os

# Dictionnaire de mappage pour les pronoms personnels
PRONOUN_MAPPING = {
    "firstSingular": "1ère personne du singulier",
    "secondSingular": "2ème personne du singulier",
    "thirdSingular": "3ème personne du singulier masculin",
    "thirdSingularFeminine": "3ème personne du singulier féminin",
    "firstPlural": "1ère personne du pluriel",
    "secondPlural": "2ème personne du pluriel masculin",
    "secondPluralFeminine": "2ème personne du pluriel féminin",
    "thirdPlural": "3ème personne du pluriel masculin",
    "thirdPluralFeminine": "3ème personne du pluriel féminin"
}

def load_conjugation_data(filepath):
    """
    Charge le fichier JSON contenant les conjugaisons.
    Le fichier est attendu sous forme d'une liste d'objets.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except Exception as e:
        print(f"Erreur lors du chargement du fichier JSON: {e}")
        sys.exit(1)

def find_verb(data, verb_name):
    """
    Recherche l'objet du verbe dont le champ "name" correspond à verb_name.
    La comparaison se fait en minuscules et en supprimant les espaces.
    """
    verb_name_norm = verb_name.lower().strip()
    for verb_obj in data:
        if verb_obj.get("name", "").lower().strip() == verb_name_norm:
            return verb_obj
    return None

def print_value(label, value, indent=2):
    """
    Affiche la valeur associée à une catégorie sous un format indenté.
    Pour la clé "Formes Intensives", on formate chaque variante de façon lisible.
    """
    prefix = " " * indent
    if label.lower() == "formes intensives":
        print(f"{prefix}{label}:")
        if isinstance(value, list):
            for idx, item in enumerate(value, start=1):
                print(f"{prefix}  Variante {idx}: {item.get('name', 'N/A')}")
                intensive_keys = [
                    ("intensiveImperative", "Impératif Intensif"),
                    ("intensiveAorist", "Aoriste Intensif"),
                    ("intensiveAoristParticiple", "Participe de l'aoriste intensif"),
                    ("negativeIntensiveAoristParticiple", "Participe de l'aoriste intensif négatif")
                ]
                for subkey, sublabel in intensive_keys:
                    subvalue = item.get(subkey)
                    if subvalue:
                        if isinstance(subvalue, dict):
                            print(f"{prefix}    {sublabel}:")
                            for key, val in subvalue.items():
                                human_key = PRONOUN_MAPPING.get(key, key)
                                if isinstance(val, list):
                                    print(f"{prefix}      {human_key}: {', '.join(val)}")
                                else:
                                    print(f"{prefix}      {human_key}: {val}")
                        elif isinstance(subvalue, list):
                            print(f"{prefix}    {sublabel}: {', '.join(subvalue)}")
                        else:
                            print(f"{prefix}    {sublabel}: {subvalue}")
        else:
            print(f"{prefix}{value}")
    elif isinstance(value, dict):
        print(f"{prefix}{label}:")
        for key, val in value.items():
            human_key = PRONOUN_MAPPING.get(key, key)
            if isinstance(val, list):
                print(f"{prefix}  {human_key}: {', '.join(val)}")
            else:
                print(f"{prefix}  {human_key}: {val}")
    elif isinstance(value, list):
        print(f"{prefix}{label}: {', '.join(value)}")
    else:
        print(f"{prefix}{label}: {value}")

def print_conjugations(verb_obj):
    """
    Affiche toutes les catégories de conjugaison du verbe en utilisant des noms lisibles.
    """
    label_mapping = {
        "translation": "Traduction",
        "preterite": "Prétérit",
        "negativePreterite": "Prétérit Négatif",
        "aorist": "Aoriste",
        "imperative": "Impératif",
        "aoristParticiple": "Participe de l'aoriste",
        "preteriteParticiple": "Participe du prétérit (positif)",
        "negativePreteriteParticiple": "Participe du prétérit (négatif)",
        "intensiveForms": "Formes Intensives"
    }
    
    print(f"\nConjugaison du verbe '{verb_obj.get('name')}' (ID: {verb_obj.get('id')}) :")
    for key, label in label_mapping.items():
        value = verb_obj.get(key)
        if value is not None:
            print_value(label, value, indent=2)

def main():
    # Vérification : on s'assure que le nombre d'arguments ne dépasse pas 3 (script, json_filepath, verbe)
    if len(sys.argv) > 3:
        print("Erreur : Trop d'arguments fournis. Veuillez ne pas utiliser de caractères génériques (*) ou autres.")
        sys.exit(1)

    # Chemin par défaut : "conjugation.json" dans le même répertoire que ce script.
    default_json_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "conjugation.json")
    
    parser = argparse.ArgumentParser(
        description="Conjugueur de verbes kabyles à partir d'un fichier JSON de conjugaison.",
        epilog=f"Exemple d'utilisation: python {os.path.basename(__file__)} {default_json_path} addi"
    )
    parser.add_argument("json_filepath", nargs="?", default=default_json_path,
                        help="Chemin vers le fichier conjugation.json (par défaut, 'conjugation.json' dans le même répertoire)")
    parser.add_argument("verb", help="La racine du verbe à conjuguer (ex: addi)")
    args = parser.parse_args()

    # Empêcher l'usage explicite du caractère '*' dans le paramètre du verbe.
    if "*" in args.verb:
        print("Erreur : L'utilisation du caractère '*' n'est pas autorisée. Veuillez spécifier une racine de verbe valide.")
        sys.exit(1)
    
    data = load_conjugation_data(args.json_filepath)
    verb_obj = find_verb(data, args.verb)
    if not verb_obj:
        print(f"Le verbe '{args.verb}' n'est pas trouvé dans le fichier JSON.")
        sample_names = [obj.get("name") for obj in data[:10]]
        print("Exemple de verbes présents :", sample_names)
        sys.exit(1)
    
    print_conjugations(verb_obj)

if __name__ == "__main__":
    main()
