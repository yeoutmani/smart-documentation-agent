# Import de BaseModel → permet de créer des modèles typés + validation automatique
# Field → permet d’ajouter des contraintes (min_length, description, etc.)
# field_validator → permet de définir des règles de validation personnalisées
from pydantic import BaseModel, Field, field_validator

# Literal → permet de limiter une valeur à un ensemble précis (type sécurisé)
from typing import Literal


# Définition du modèle de données pour le routing de l’agent
class RoutingDecision(BaseModel):

    # Champ "route" → ne peut prendre QUE ces deux valeurs
    # Cela garantit que l’agent ne produit pas de valeur imprévisible
    route: Literal["direct_answer", "search_docs"] = Field(
        description="Routing decision for the agent"  # utile pour la doc API (Swagger)
    )

    # Champ "question" → chaîne de caractères obligatoire
    # min_length=1 → empêche une chaîne vide
    # max_length=500 → évite abus / prompts trop longs
    question: str = Field(
        min_length=1,
        max_length=500,
        description="User input question"
    )

    # Validator personnalisé sur le champ "question"
    @field_validator("question")
    @classmethod
    def clean_question(cls, value: str) -> str:

        # Nettoyage → supprime les espaces inutiles
        value = value.strip()

        # Vérification supplémentaire :
        # empêche les cas comme "   " (que min_length ne détecte pas)
        if not value:
            raise ValueError("Question cannot be empty")

        # Retourne la version propre de la question
        return value

    # Configuration du modèle
    class Config:

        # Ajoute un exemple dans la documentation automatique (FastAPI / Swagger)
        # Très utile pour les développeurs et recruteurs
        json_schema_extra = {
            "example": {
                "route": "search_docs",
                "question": "How to configure the API?"
            }
        }

# Ce modèle Pydantic impose un typage strict pour la décision de routage et nettoie les entrées utilisateur afin de garantir que seules des données valides et propres entrent dans le pipeline de l’agent.