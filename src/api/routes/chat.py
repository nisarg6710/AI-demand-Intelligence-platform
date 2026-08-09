from fastapi import APIRouter, HTTPException

from src.api.schema import ChatRequest, ChatResponse
from src.ai.query.query_engine import QueryEngine


router = APIRouter()

query_engine = QueryEngine()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    try:

        result = query_engine.ask(request.question)

        # Extract the final response.
        #
        # For a single specialist agent, the response
        # is stored inside the specialists dictionary.
        if result.get("executive_report"):

            response = result["executive_report"]

        else:

            specialists = result.get("specialists", {})

            response = "\n\n".join(
                specialists.values()
            )

        return ChatResponse(
            success=result["success"],
            question=result["question"],
            selected_agents=result["selected_agents"],
            response=response,
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )