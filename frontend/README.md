# Smart Documentation Agent - Frontend

Frontend React + TypeScript pour Smart Documentation Agent.

## Installation

```bash
npm install
```

## Démarrage du serveur de développement

```bash
npm run dev
```

L'application démarre sur `http://localhost:3000`

## Build pour la production

```bash
npm run build
```

## Structure du projet

```
frontend/
├── src/
│   ├── components/
│   │   └── ChatUI.tsx         # Composant principal du chat
│   ├── hooks/
│   │   └── useChat.ts         # Hook pour la gestion de l'état des messages
│   ├── types/
│   │   └── index.ts           # Types TypeScript
│   ├── App.tsx                # Composant racine
│   ├── main.tsx               # Point d'entrée React
│   └── index.css              # Styles globaux
├── index.html                 # HTML template
├── package.json               # Dépendances
├── tsconfig.json              # Configuration TypeScript
├── vite.config.ts             # Configuration Vite
└── README.md                  # Cette documentation
```

## Fonctionnalités

- **Chat UI intuitive** avec historique des messages
- **Streaming des réponses** en temps réel
- **Message state management** avec React hooks
- **TypeScript** pour la sécurité des types
- **Responsive design** avec Gradient UI
- **Support du streaming** des tokens du backend

## Configuration API

Le proxy API est configuré dans `vite.config.ts`:
- Les requêtes `/chat` sont routées vers `http://localhost:8000`

## Scripts disponibles

- `npm run dev` - Démarrer le serveur de développement
- `npm run build` - Build la production
- `npm run preview` - Prévisualiser la build production
- `npm run lint` - Lancer ESLint
