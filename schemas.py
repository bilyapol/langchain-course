from typing import List

from pydantic import BaseModel, Field


class Source(BaseModel):
    url: str = Field(description="The url of the source")


class AgentResponse(BaseModel):
    """Schema for agent response with answer and sources"""

    answer: str = Field(description="The agents answer to the querry")
    sources: list[Source] = Field(
        default_factory=list, description="List of sources to generate the answer"
    )
