import os

import uvicorn
from fastapi import FastAPI, Body, HTTPException, status

from api.models import *
from configs.api import get_base_router
from utils.coref_resolver import coref_resolve

app = FastAPI()
base_router = get_base_router()


@base_router.post(
    "/coref-resolver",
    response_description="coreference issue resolving",
    status_code=status.HTTP_200_OK,
    response_model=CorefResolverOutput
)
async def resolve_coref_issues(coref_resolve_input: CorefResolverInput = Body(...)) -> dict:
    resolved_text = coref_resolve(coref_resolve_input.text, coref_resolve_input.conv_dict)
    if resolved_text:
        return resolved_text
    raise HTTPException(status_code=status.HTTP_400_NOT_FOUND, detail="coreference resolving failed")


if __name__ == "__main__":
    app.include_router(base_router)
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
