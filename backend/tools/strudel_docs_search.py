import asyncio
import json
import urllib.request

from pydantic import BaseModel

from backend.tools.registry import registry

ALGOLIA_URL = (
    "https://SAZ71S8CLS-dsn.algolia.net/1/indexes/strudel-tidalcycles/query"
)
ALGOLIA_HEADERS = {
    "X-Algolia-Application-Id": "SAZ71S8CLS",
    "X-Algolia-API-Key": "d5044f9d21b80e7721e5b0067a8730b1",
    "Content-Type": "application/json",
}


class StrudelDocsSearchParams(BaseModel):
    query: str


@registry.tool(
    name="strudel_docs_search",
    description="Search the official Strudel documentation at strudel.cc for functions, effects, and techniques.",
    params_model=StrudelDocsSearchParams,
)
async def strudel_docs_search(params: StrudelDocsSearchParams) -> dict:
    def _search() -> list[dict]:
        body = json.dumps({"query": params.query, "hitsPerPage": 5}).encode()
        req = urllib.request.Request(ALGOLIA_URL, data=body, headers=ALGOLIA_HEADERS)
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode())
        results = []
        for hit in data.get("hits", []):
            hierarchy = hit.get("hierarchy", {})
            title = " > ".join(
                v for _, v in sorted(hierarchy.items()) if v is not None
            )
            results.append(
                {
                    "title": title,
                    "url": hit.get("url", ""),
                    "content": hit.get("content") or "",
                }
            )
        return results

    results = await asyncio.to_thread(_search)
    return {"query": params.query, "results": results}