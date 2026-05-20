# Analyse du projet Academy001 (mise à jour)

_Date : 2026-05-20_

## 1) Vue d’ensemble

Le projet est une application Django orientée gestion académique, structurée autour de 4 apps:

- `users`: gestion utilisateurs/authentification et rôles.
- `academics`: domaine académique (squelette, peu implémenté).
- `tracking`: suivi (squelette, peu implémenté).
- `analytics`: analytics/reporting (squelette, peu implémenté).

Le routage principal inclut la page d’accueil et les routes utilisateurs.

## 2) Points positifs

- Utilisation d’un `AUTH_USER_MODEL` custom (`users.User`) avec un modèle de rôles explicite.
- Modélisation hiérarchique utile (`University` -> `Department` -> `User`).
- Utilisation de formulaires dédiés (`CustomUserCreationForm`, `CustomLoginForm`).
- Templates de base et vues principales (home, login, dashboard, liste utilisateurs) déjà présents.

## 3) Problèmes critiques observés

### 3.1 Configuration Django invalide

Dans `academic_system/settings.py`, la ligne `AUTH_USER_MODEL = 'users.User'` est collée au contenu de `urls.py` (`from django.contrib import admin ...`). Cela rend `settings.py` invalide et empêche le démarrage normal du projet.

### 3.2 Duplication et code mort dans `users/views.py`

- Imports répétés.
- Plusieurs `return` successifs dans les mêmes fonctions (code inatteignable).
- Variables/contextes redondants.

Conséquence: maintenance difficile et risque d’incohérence fonctionnelle.

### 3.3 Sécurité / production

- `DEBUG = True` en dur.
- `SECRET_KEY` en clair dans le code.
- `ALLOWED_HOSTS = []` (incomplet pour un déploiement).

## 4) Risques fonctionnels

- Le flux d’authentification peut devenir fragile à cause de la duplication dans `login_view`.
- Le couplage `University`/`Department` n’est pas validé côté formulaire (pas de filtre dynamique département-université).
- Les apps `academics`, `tracking`, `analytics` sont surtout des squelettes: faible couverture métier réelle à ce stade.

## 5) Recommandations priorisées

### Priorité P0 (bloquant)

1. Corriger immédiatement la corruption de `settings.py` (séparer strictement `settings.py` et `urls.py`).
2. Lancer `python manage.py check` et corriger toutes erreurs de config.

### Priorité P1 (stabilité/qualité)

1. Refactor `users/views.py` pour retirer duplications et branches inatteignables.
2. Ajouter des tests unitaires de base pour:
   - création utilisateur,
   - connexion/déconnexion,
   - accès dashboard protégé.

### Priorité P2 (sécurité)

1. Externaliser `SECRET_KEY` via variable d’environnement.
2. Gérer `DEBUG` via environnement.
3. Définir correctement `ALLOWED_HOSTS` selon l’environnement.

### Priorité P3 (évolution produit)

1. Implémenter la logique métier dans `academics`, `tracking`, `analytics`.
2. Ajouter permissions par rôle (ex: decorators/mixins par niveau d’accès).
3. Préparer une API (DRF) si besoin d’intégration front/mobile.

## 6) Conclusion

Le socle est pertinent pour un MVP de gestion académique, mais l’état actuel contient au moins un défaut bloquant de configuration et plusieurs dettes de code visibles. La meilleure stratégie est de sécuriser d’abord le démarrage de l’application, puis de nettoyer les vues utilisateurs avant d’étendre les modules métier.
