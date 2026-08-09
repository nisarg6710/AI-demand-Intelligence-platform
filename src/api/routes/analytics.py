from fastapi import APIRouter, HTTPException

from src.api.schema import AnalyticsRequest, AnalyticsResponse
from src.ai.agents.analytics_agent import AnalyticsAgent


router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"],
)

analytics_agent = AnalyticsAgent()


@router.post(
    "",
    response_model=AnalyticsResponse,
)
def analytics(request: AnalyticsRequest):

    try:

        result = analytics_agent.run(
            request.question
        )

        return AnalyticsResponse(
            success=True,
            question=request.question,
            response=result,
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )