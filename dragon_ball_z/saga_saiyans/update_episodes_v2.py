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

    # Détermination dynamique des liens précédent et suivant
    prev_ep = f"ssaiyans_ep{i-1:02d}.html" if i > 1 else "ssaiyans_présentation.html"
    next_ep = f"ssaiyans_ep{i+1:02d}.html" if i < TOTAL_EPISODES else "ssaiyans_présentation.html"

    # Le bloc CSS exact de l'épisode 16 pour les cartes de navigation
    css_to_add = """    /* Disposition des 3 cartes de navigation sur une même ligne horizontale */
    .navigation-links {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 12px;
      margin-top: 25px;
    }

    /* Adaptation mobile pour garder une bonne lisibilité */
    @media (max-width: 650px) {
      .navigation-links {
        grid-template-columns: 1fr;
      }
    }

    /* Style de chaque carte encadrée avec le gant */
    .nav-card {
      display: flex;
      align-items: center;
      gap: 10px;
      padding: 12px 10px;
      background-color: #ffffff;
      border: 1px solid #e0e4e8;
      border-radius: 6px;
      text-decoration: none;
      transition: border-color 0.2s ease, box-shadow 0.2s ease;
    }

    .nav-card img {
      width: 35px;
      height: auto;
      mix-blend-mode: multiply;
      flex-shrink: 0;
    }

    .nav-card span {
      font-family: 'Liberation Serif', serif;
      font-size: 0.95rem;
      font-weight: bold;
      color: #000000;
      letter-spacing: 0.5px;
      transition: color 0.2s ease;
    }

    .nav-card:hover {
      border-color: #bbbbbb;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
    }

    .nav-card:hover span {
      color: #cc0000;
    }
  </style>"""

    # Le bloc HTML des 3 cartes de navigation
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

    # 1. Insertion du CSS si la classe .nav-card n'est pas déjà présente dans le fichier
    if ".nav-card" not in content:
        content = content.replace("  </style>", css_to_add)

    # 2. Remplacement de l'ancien lien de bas de page par les 3 cartes
    old_back_to_list_pattern = re.compile(
        r'\s*<!--\s*Lien bas de page.*?\n\s*<a href="ssaiyans_présentation\.html" class="back-to-list">.*?</a>', 
        re.DOTALL
    )
    
    updated = False
    if old_back_to_list_pattern.search(content):
        content = old_back_to_list_pattern.sub(f"\n\n{new_nav_block}\n", content)
        updated = True
    else:
        # Sécurité si une ancienne version de .navigation-links était présente
        old_nav_links_pattern = re.compile(
            r'\s*<div class="navigation-links">.*?</div>\s*(?=</div>\s*</body>)', 
            re.DOTALL
        )
        if old_nav_links_pattern.search(content):
            content = old_nav_links_pattern.sub(f"\n\n{new_nav_block}\n", content)
            updated = True

    if updated:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Mis à jour avec succès : {filename}")
    else:
        print(f"Attention : Ancien lien de bas de page non trouvé dans {filename}")

print("Mise à jour des 15 épisodes terminée avec succès !")
