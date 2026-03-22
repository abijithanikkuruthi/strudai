from pydantic import BaseModel

from backend.tools.registry import registry
from backend.ws import manager


class RewriteCodeParams(BaseModel):
    code: str


@registry.tool(
    name="strudel_rewrite_code",
    description="Replace the entire Strudel editor code and evaluate it. Use this when writing code from scratch or rewriting most of the code. Returns {ok, logs}.",
    params_model=RewriteCodeParams,
)
async def strudel_rewrite_code(params: RewriteCodeParams) -> dict:
    resp = await manager.request_from_frontend("rewrite_code", {"code": params.code})
    return resp
