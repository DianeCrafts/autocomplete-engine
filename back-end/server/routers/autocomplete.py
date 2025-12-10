from fastapi import APIRouter
from server.models.api_models import AutocompleteResponse, SuggestionResponse
from server.services.app_context import AppContext

router = APIRouter(prefix="/api", tags=["Autocomplete"])


@router.get("/autocomplete", response_model=AutocompleteResponse)
def autocomplete(query: str, user_id: str = "guest", k: int = 5, debug: bool = False):
    qp, logger = AppContext.initialize()

    # If debug=true, processor returns both (results, debug_info)
    if debug:
        suggestions, debug_info = qp.autocomplete(query, user_id=user_id, k=k, debug=True)
    else:
        suggestions = qp.autocomplete(query, user_id=user_id, k=k)
        debug_info = None

    response_suggestions = [
        SuggestionResponse(term=s.term, score=s.score)
        for s in suggestions
    ]

    return AutocompleteResponse(
        query=query,
        suggestions=response_suggestions,
        debug=debug_info
    )


@router.post("/select")
def log_selection(term: str, user_id: str = "guest"):
    _, logger = AppContext.initialize()
    logger.log(user_id, term)
    return {"message": f"Selection logged for user {user_id}: {term}"}
