from fastapi import APIRouter, HTTPException

from src.api.schema import (
    AnalyticsRequest,
    AnalyticsResponse,
    MonthlySalesResponse,
)

from src.ai.agents.analytics_agent import AnalyticsAgent
from src.analytics.service import AnalyticsService

import json
import traceback


router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"],
)

analytics_agent = AnalyticsAgent()
analytics_service = AnalyticsService()

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

        traceback.print_exc()

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )

@router.get(
    "/monthly-sales",
    response_model=MonthlySalesResponse,
)
def monthly_sales():

    try:

        df = analytics_service.get_monthly_sales()

        data = json.loads(
            df.to_json(orient="records")
        )

        return MonthlySalesResponse(
            success=True,
            data=data,
        )

    except Exception as e:

        traceback.print_exc()

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )