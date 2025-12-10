from fastapi import FastAPI
from backend.routers import autocomplete

app = FastAPI(
    title="Autocomplete Engine API",
    description="FastAPI backend for Trie + Ranking + Typo Engine",
)

# Register routes
app.include_router(autocomplete.router)

@app.get("/")
def root():
    return {"message": "Autocomplete Engine API running!"}
