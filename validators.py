from aws import node_types

def validate_aws_json(data):
    if not isinstance(data, dict):
        raise ValueError("Entrada inválida: debe ser JSON.")
    if "nodes" not in data or "edges" not in data:
        raise ValueError("Debe contener 'nodes' y 'edges'")
    for node in data["nodes"]:
        if node["type"] not in node_types:
            raise ValueError(f"Tipo no soportado: {node['type']}")

def validate_dsl(dsl):
    if not dsl.strip().startswith("entity"):
        raise ValueError("El código DSL debe comenzar con 'entity'.")
    if "{" not in dsl or "}" not in dsl:
        raise ValueError("Faltan llaves '{' o '}' en la definición.")
    if "->" not in dsl and "entity" not in dsl:
        raise ValueError("Debe incluir al menos una relación o entidad.")

def validate_json_input(data):
    if not isinstance(data, (dict, list)):
        raise ValueError("Debe enviar un objeto JSON válido (dict o lista).")
