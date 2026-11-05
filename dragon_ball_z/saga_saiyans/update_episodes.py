import os
import re

# On passe le nombre total d'épisodes à 15
TOTAL_EPISODES = 15

for i in range(1, TOTAL_EPISODES + 1):
    filename = f"ssaiyans_ep{i:02d}.html"
    
    if not os.path.exists(filename):
        print(f"Fichier non trouvé : {filename}, ignoré.")
        continue

    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    # Détermination des liens pour l'épisode précédent et suivant
    prev_ep = f"ssaiyans_ep{i-1:02d}.html" if i > 1 else "ssaiyans_présentation.html"
    next_ep = f"ssaiyans_ep{i+1:02d}.html" if i < TOTAL_EPISODES else "ssaiyans_présentation.html"

    # Bloc HTML de navigation en 3 cartes
    new_nav_block = f"""    <!-- Navigation horizontale sous forme de 3 cartes encadrées -->
    <div class="navigation-links">
      <!-- 1. Épisode Précédent -->
      <a href="{prev_ep}" class="nav-card">
        <img src="gant.png" alt="Main gantée">
        <span>ÉPISODE PRÉCÉDENT</span>
      </a>

      <!-- 2. Épisode Suivant -->
      <a href="{next_ep}" class="nav-card">
        <img src="gant.png" alt="Main gantée">
        <span>ÉPISODE SUIVANT</span>
      </a>

      <!-- 3. Liste des épisodes -->
      <a href="ssaiyans_présentation.html" class="nav-card">
        <img src="gant.png" alt="Main gantée">
        <span>LISTE DES ÉPISODES</span>
      </a>
    </div>"""

    # Recherche et remplacement de l'ancien lien de bas de page
    updated_content = False

    old_back_to_list_pattern = re.compile(
        r'\s*<!--\s*Lien bas de page.*?\n\s*<a href="ssaiyans_présentation\.html" class="back-to-list">.*?</a>', 
        re.DOTALL
    )
    
    if old_back_to_list_pattern.search(content):
        content = old_back_to_list_pattern.sub(f"\n\n{new_nav_block}\n", content)
        updated_content = True
    else:
        old_nav_links_pattern = re.compile(
            r'\s*<div class="navigation-links">.*?</div>\s*(?=</div>\s*</body>)', 
            re.DOTALL
        )
        if old_nav_links_pattern.search(content):
            content = old_nav_links_pattern.sub(f"\n\n{new_nav_block}\n", content)
            updated_content = True

    if updated_content:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Mis à jour avec succès : {filename}")
    else:
        print(f"Structure de navigation non reconnue dans : {filename}")

print("Traitement des 15 épisodes terminé !")
