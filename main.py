import json
import httpx
from pydantic import BaseModel, Field
from fastapi import FastAPI, Request
from typing import Dict, Any, Optional

app = FastAPI()


class PredictRequest(BaseModel):
    hf_pipeline: str
    model_deployed_url: str
    inputs: Any
    parameters: Dict[str, Any] = Field(default_factory=dict)


@app.post(path="/predict")
async def predict(request: Request):
    try:
        data = await request.json()
        hf_pipeline = data.get("hf_pipeline")
        model_deployed_url = data.get("model_deployed_url")
        inputs = data.get("inputs")
        parameters = data.get("parameters")

        if not hf_pipeline:
            raise ValueError("hf_pipeline is required")
        if not model_deployed_url:
            raise ValueError("model_deployed_url is required")
        if not inputs:
            raise ValueError("inputs is required")

        if hf_pipeline == "zero-shot-classification":
            candidate_labels = parameters.get("candidate_labels")
            cl = json.dumps(candidate_labels)
            # cl = json.loads(cl)
            # print(cl)
            payload = {
                "id": "string",
                "parameters": {"content_type": "string", "headers": {}},
                "inputs": [
                    {
                        "name": "array_inputs",
                        "shape": [1],
                        "datatype": "BYTES",
                        "data": [inputs],
                    },
                    {
                        "name": "candidate_labels",
                        "shape": [-1],
                        "datatype": "BYTES",
                        "data": [cl],
                    },
                ],
                "outputs": [],
            }
        elif hf_pipeline == "text-generation":
            payload = {
                "inputs": [
                    {
                        "name": "array_inputs",
                        "shape": [1],
                        "datatype": "BYTES",
                        "data": [inputs],
                    },
                    {
                        "name": "max_new_tokens",
                        "shape": [-1],
                        "datatype": "BYTES",
                        "data": ["20"],
                        "parameters": {"content_type": "hg_json"},
                    },
                ],
                "parameters": parameters,
            }
        elif hf_pipeline == "object-detection":
            print(inputs)
            payload = {
                "id": "string",
                "parameters": parameters,
                "inputs": [
                    {
                        "name": "inputs",
                        "shape": [-1],
                        "datatype": "BYTES",
                        "data": [
                            "https://www.w3.org/WAI/WCAG22/Techniques/pdf/img/table-word.jpg"
                        ],
                    }
                ],
                "outputs": [],
            }
        elif hf_pipeline == "token-classification":
            payload = {
                "id": "string",
                "parameters": {"content_type": "string", "headers": {}},
                "inputs": [
                    {
                        "name": "array_inputs",
                        "shape": [1],
                        "datatype": "BYTES",
                        "data": [inputs],
                    }
                ],
                "outputs": [
                    {
                        "name": "string",
                        "parameters": {"content_type": "string", "headers": {}},
                    }
                ],
            }

        else:
            raise ValueError("hf_pipeline not supported")

        async with httpx.AsyncClient() as client:
            response = await client.post(model_deployed_url, json=payload)
            response.raise_for_status()
            output = response.json()
            return output
    except Exception as e:
        print(e)

    # return {}
