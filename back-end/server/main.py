from fastapi import FastAPI
from server.routers import autocomplete
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Autocomplete Engine API",
    description="FastAPI backend for Trie + Ranking + Typo Engine",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes
app.include_router(autocomplete.router)

@app.get("/")
def root():
    return {"message": "Autocomplete Engine API running!"}
