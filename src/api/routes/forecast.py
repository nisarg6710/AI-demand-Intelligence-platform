from fastapi import APIRouter, HTTPException

from src.api.schema import ForecastRequest, ForecastResponse
from src.ai.agents.forecast_agent import ForecastAgent

import traceback


router = APIRouter(
    prefix="/forecast",
    tags=["Forecasting"],
)

forecast_agent = ForecastAgent()


@router.post(
    "",
    response_model=ForecastResponse,
)
def forecast(request: ForecastRequest):

    try:

        result = forecast_agent.run(
            request.question
        )

        return ForecastResponse(
            success=True,
            question=request.question,
            selected_action=result["selected_action"],
            response=result["response"],
        )

    except Exception as e:

        traceback.print_exc()

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


@router.get(
    "/predictions",
)
def forecast_predictions():

    try:

        # Use the existing forecasting service/logic
        # that generates the forecast predictions.
        result = forecast_agent.run(
            "Get the forecast predictions."
        )

        return {
            "success": True,
            "data": result,
        }

    except Exception as e:

        traceback.print_exc()

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )