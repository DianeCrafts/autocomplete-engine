from typing import Optional, Any
from pydantic import BaseModel

class SuggestionResponse(BaseModel):
    term: str
    score: float

class AutocompleteResponse(BaseModel):
    query: str
    suggestions: list[SuggestionResponse]
    debug: Optional[Any] = None
