# Smart Documentation Agent API

API backend pour Smart Documentation Agent construite avec FastAPI.

## Installation

1. Créer un environnement virtuel:
```bash
python -m venv venv
source venv/bin/activate  # Sur macOS/Linux
# ou
venv\Scripts\activate  # Sur Windows
```

2. Installer les dépendances:
```bash
pip install -r requirements.txt
```

## Démarrage du serveur

```bash
python main.py
```

Ou utiliser uvicorn directement:
```bash
uvicorn main:app --reload
```

Le serveur démarre sur `http://localhost:8000`

## Documentation interactive

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Endpoints disponibles

- `GET /` - Endpoint racine
- `GET /health` - Vérification de la santé du service
- `GET /api/v1/docs` - Endpoint de documentation

## Structure du projet

```
backend/
├── main.py              # Application principale FastAPI
├── requirements.txt     # Dépendances Python
├── .gitignore          # Fichiers à ignorer dans git
└── README.md           # Cette documentation
```

## Développement

Pour contribuer au projet, assurez-vous que votre environnement est configuré et testez vos changements avant de les commiter.
