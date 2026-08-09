from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    question: str = Field(
        ...,
        min_length=1,
        description="Business question for the AI assistant.",
    )


class ChatResponse(BaseModel):
    success: bool
    question: str
    selected_agents: list[str]
    response: str


class ForecastRequest(BaseModel):

    question: str


class ForecastResponse(BaseModel):

    success: bool
    question: str
    selected_action: str
    response: str


class AnalyticsRequest(BaseModel):

    question: str


class AnalyticsResponse(BaseModel):

    success: bool
    question: str
    response: str

class ReportRequest(BaseModel):

    question: str


class ReportResponse(BaseModel):

    success: bool
    question: str
    selected_agents: list[str]
    report: str