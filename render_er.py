import json
import base64
import pydot
import tempfile
import os

from utils.diagram_utils import dsl_to_dot
from validators import validate_dsl

def lambda_handler(event, context):
    try:
        # Si estás usando API Gateway, el body viene como string
        body = event.get("body", "")
        if event.get("isBase64Encoded", False):
            body = base64.b64decode(body).decode()

        # Validar y procesar el DSL
        validate_dsl(body)
        dot_graph = dsl_to_dot(body)  # Esta debe retornar el DOT string
        graphs = pydot.graph_from_dot_data(dot_graph)

        if not graphs:
            raise Exception("DOT parsing failed")

        png_data = graphs[0].create_png()

        return {
            "statusCode": 200,
            "headers": {"Content-Type": "image/png"},
            "body": base64.b64encode(png_data).decode("utf-8"),
            "isBase64Encoded": True
        }

    except ValueError as e:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": str(e)})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": "Error interno del servidor", "details": str(e)})
        }

