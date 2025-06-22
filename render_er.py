import json
import os
import tempfile
from utils.diagram_utils import dsl_to_dot
from validators import validate_dsl

def render_er(event, context):
    try:
        dsl = event["body"]
        validate_dsl(dsl)
        dot = dsl_to_dot(dsl)

        with tempfile.TemporaryDirectory() as tmpdir:
            output_path = os.path.join(tmpdir, "er_diagram")
            dot.render(output_path, format="png", cleanup=True)
            png_path = output_path + ".png"

            with open(png_path, "rb") as f:
                image_data = f.read()

        return {
            "statusCode": 200,
            "headers": {"Content-Type": "image/png"},
            "body": image_data.decode("latin1"),  # base64 is more robust (see note)
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
