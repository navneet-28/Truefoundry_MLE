import json
import httpx
from pydantic import BaseModel, Field
from fastapi import FastAPI, Request
from typing import Dict, Any, Optional

app = FastAPI()


class PredictRequest(BaseModel):
    hf_pipeline: str
    model_deployed_url: str
    inputs: str
    parameters: Dict[str, Any] = Field(default_factory=dict)


@app.post(path="/predict")
async def predict(request: Request):
    # Write your code here to translate input into V2 protocol and send it to model_deployed_url
    try:
        data = await request.json()
        hf_pipeline = data.get("hf_pipeline")
        model_deployed_url = data.get("model_deployed_url")
        inputs = data.get("inputs")
        parameters = data.get("parameters")

        # perform input validation and handle errors
        if not hf_pipeline:
            raise ValueError("hf_pipeline is required")
        if not model_deployed_url:
            raise ValueError("model_deployed_url is required")
        if not inputs:
            raise ValueError("inputs is required")
        
        # convert inputs to V2 interference protocols based on hf_pipeline
        if hf_pipeline == "zero-shot-classification":
            candidate_labels = parameters.get("candidate_labels", [])
            payload = {
                "inputs": inputs,
                "parameters": parameters
            }
        elif hf_pipeline == "text-generation":
            payload = {
                "inputs": inputs,
                "parameters": parameters
            }
        elif hf_pipeline == "object-detection":
            payload = {
                "inputs": inputs,
                "parameters": parameters
            }
        elif hf_pipeline == "token-classification":
            payload = {
                "inputs": inputs,
                "parameters": parameters
            }
        else:
            raise ValueError("hf_pipeline not supported")
        
        # Invoke huggingFace model using model_deployed_url and converted payload
        async with httpx.AsyncClient() as client:
            response = await client.post(model_deployed_url, json=payload)
            response.raise_for_status()
            output = response.json()
            return output
    except Exception as e:
        print(e)

    #return {}