import os
import re

TOTAL_EPISODES = 15

for i in range(1, TOTAL_EPISODES + 1):
    filename = f"ssaiyans_ep{i:02d}.html"
    
    if not os.path.exists(filename):
        print(f"Fichier non trouvé : {filename}, ignoré.")
        continue

    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    # Le bloc d'origine à remettre en bas de page
    original_bottom_block = """    <!-- Lien bas de page : Gant (gant.png) + LISTE DES EPISODES vers ssaiyans_présentation.html -->
    <a href="ssaiyans_présentation.html" class="back-to-list">
      <img src="gant.png" alt="Main gantée pointant vers la liste">
      <span>LISTE DES ÉPISODES</span>
    </a>"""

    # Expression régulière pour cibler le bloc des 3 cartes (.navigation-links)
    nav_links_pattern = re.compile(
        r'\s*<!--\s*Navigation horizontale sous forme de 3 cartes encadrées\s*-->\s*<div class="navigation-links">.*?</div>\s*</div>',
        re.DOTALL
    )

    if nav_links_pattern.search(content):
        # On remplace les 3 cartes par le lien d'origine
        content = nav_links_pattern.sub(f"\n\n{original_bottom_block}\n", content)
        
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Restauré avec succès : {filename}")
    else:
        print(f"Bloc de navigation 3 cartes non trouvé dans : {filename}")

print("Restauration des 15 épisodes terminée !")
