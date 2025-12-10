from fastapi import APIRouter
from backend.models.api_models import AutocompleteResponse, SuggestionResponse
from backend.services.app_context import AppContext

router = APIRouter(prefix="/api", tags=["Autocomplete"])

@router.get("/autocomplete", response_model=AutocompleteResponse)
def autocomplete(query: str, user_id: str = "guest", k: int = 5):
    qp, logger = AppContext.initialize()

    suggestions = qp.autocomplete(query, user_id=user_id, k=k)

    # Convert engine suggestions → JSON-compatible response objects
    response_suggestions = [
        SuggestionResponse(term=s.term, score=s.score)
        for s in suggestions
    ]

    return AutocompleteResponse(
        query=query,
        suggestions=response_suggestions
    )

@router.post("/select")
def log_selection(term: str, user_id: str = "guest"):
    _, logger = AppContext.initialize()
    logger.log(user_id, term)
    return {"message": f"Selection logged for user {user_id}: {term}"}
