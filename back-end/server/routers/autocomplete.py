from fastapi import APIRouter
from server.models.api_models import AutocompleteResponse, SuggestionResponse
from server.services.app_context import AppContext

router = APIRouter(prefix="/api", tags=["Autocomplete"])


@router.get("/autocomplete", response_model=AutocompleteResponse)
def autocomplete(query: str, user_id: str = "guest", k: int = 5, debug: bool = False):
    qp, logger = AppContext.initialize()

    # If debug=true, processor returns both (results, debug_info)
    if debug:
        suggestions, debug_info = qp.autocomplete(query, user_id=user_id, k=k, debug=True, disable_cache=True)
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


@router.get("/debug/term")
def debug_term(term: str):
    qp, _ = AppContext.initialize()
    trie = qp.trie

    node = trie.find_prefix_node(term)
    if not node or not node.is_end:
        return {"exists": False}

    return {
        "term": node.term,
        "frequency": node.frequency,
        "last_used": node.last_used,
        "user_freq": node.user_freq,
    }
