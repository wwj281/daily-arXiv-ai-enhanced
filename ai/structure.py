from pydantic import BaseModel, Field


class Structure(BaseModel):
    tldr: str = Field(
        description="A one-sentence summary of the paper's core contribution."
    )
    problem: str = Field(
        description="The main problem or limitation this paper aims to solve."
    )
    key_idea: str = Field(
        description="The central idea or insight behind the paper."
    )
    system_method_design: str = Field(
        description="The main system design, method, algorithm, or architecture proposed by the paper."
    )
    experiments: str = Field(
        description="The key experimental setup, baselines, metrics, and main results."
    )
    why_it_matters: str = Field(
        description="Why this work is important or what broader value it provides."
    )
    relevance_to_llm_moe_system_research: str = Field(
        description="How this work is relevant to LLM systems, MoE, inference acceleration, memory systems, KV cache, distributed systems, or computer architecture."
    )