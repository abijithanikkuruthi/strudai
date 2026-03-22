from pydantic import BaseModel

from backend.tools.registry import registry
from backend.ws import manager


class EditCodeParams(BaseModel):
    old_string: str
    new_string: str


@registry.tool(
    name="strudel_edit_code",
    description="Search-and-replace a section of the Strudel editor code. The old_string must match exactly once in the current code. Returns {ok, logs} on success or {ok: false, error, current_code} if the old_string is not found or is ambiguous.",
    params_model=EditCodeParams,
)
async def strudel_edit_code(params: EditCodeParams) -> dict:
    resp = await manager.request_from_frontend(
        "edit_code", {"old_string": params.old_string, "new_string": params.new_string}
    )
    return resp
