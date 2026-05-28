frontend:
html + vanilla

backend:
├── __init__.py
    ├── api/                
    │   ├── __init__.py
    │   └── routes.py       # Defines your API endpoints (e.g., GET /api/posts)
    ├── core/               
    │   ├── __init__.py
    │   └── config.py       # Loads settings from .env (API keys, IG login, cache settings)
    ├── services/           
    │   ├── __init__.py
    │   └── instagram.py    # Where instaloader lives. Handles login, fetching feed, and caching
    └── schemas/            
        ├── __init__.py
        └── post.py         # Data models (e.g., Pydantic) to structure the data for the frontend