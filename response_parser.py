"""
parser.py

This module defines Pydantic models to parse and validate JSON responses containing a question,
reasoning, and an action specifying a tool and its input. It provides a `parse` function to
convert a JSON string into a validated Python object, raising an error if the input is invalid.

Usage:
    from parser import parse
    parsed_data = parse(json_string)
"""

from pydantic import BaseModel, ValidationError
from typing import Optional

class Action(BaseModel):
    tool: str
    input: str


class ResponsePayload(BaseModel):
    question: str
    reasoning: str
    action: Action


def parse(json_string: str) -> ResponsePayload:
    try:
        return ResponsePayload.model_validate_json(json_string)
    except ValidationError as e:
        raise ValueError(f"Invalid input JSON: {e}")
    
    
