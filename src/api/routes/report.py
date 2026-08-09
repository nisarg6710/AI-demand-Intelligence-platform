from fastapi import APIRouter, HTTPException

from src.api.schema import ReportRequest, ReportResponse
from src.ai.agents.orchestrator import AgentOrchestrator


router = APIRouter(
    prefix="/report",
    tags=["Reports"],
)

orchestrator = AgentOrchestrator()


@router.post(
    "",
    response_model=ReportResponse,
)
def report(request: ReportRequest):

    try:

        result = orchestrator.run(
            request.question
        )

        if result["executive_report"] is None:

            raise ValueError(
                "Unable to generate executive report."
            )

        return ReportResponse(
            success=True,
            question=request.question,
            selected_agents=result["selected_agents"],
            report=result["executive_report"],
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )