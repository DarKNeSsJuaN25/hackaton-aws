import os
import tempfile
import subprocess
from graphviz import Digraph
from diagrams import Diagram
from aws import node_types
def dsl_to_plantuml(dsl_text):
    lines = dsl_text.strip().split("\n")
    entities = {}
    relations = []
    current_entity = None

    for line in lines:
        line = line.strip()
        if line.startswith("entity"):
            parts = line.split()
            current_entity = parts[1]
            entities[current_entity] = []
        elif "->" in line:
            relations.append(line)
        elif line != "}" and current_entity:
            entities[current_entity].append(line)

    uml = ["@startuml", "hide circle", "skinparam linetype ortho"]
    for name, attrs in entities.items():
        uml.append(f"entity {name} {{")
        for attr in attrs:
            uml.append(f"  {attr}")
        uml.append("}")
    for rel in relations:
        left, right = rel.split("->")
        left_entity = left.strip().split(".")[0]
        right_entity = right.strip().split(".")[0]
        uml.append(f"{left_entity} --> {right_entity}")
    uml.append("@enduml")
    return "\n".join(uml)

def dsl_to_dot(dsl_text):
    lines = dsl_text.strip().split("\n")
    entities = {}
    relations = []
    current_entity = None

    for line in lines:
        line = line.strip()
        if line.startswith("entity"):
            parts = line.split()
            current_entity = parts[1]
            entities[current_entity] = []
        elif "->" in line:
            relations.append(line)
        elif line != "}" and current_entity:
            entities[current_entity].append(line)

    dot = Digraph(format="png")
    dot.attr('node', shape='record')

    for entity, attrs in entities.items():
        attrs_formatted = "\\l".join(attrs) + "\\l"
        label = f"{{{entity}|{attrs_formatted}}}"
        dot.node(entity, label=label)


    for rel in relations:
        left, right = rel.split("->")
        left = left.strip().split(".")[0]
        right = right.strip().split(".")[0]
        dot.edge(left, right)

    return dot

def json_to_dot(data, dot=None, parent="root"):
    if dot is None:
        dot = Digraph()
        dot.node(parent)

    if isinstance(data, dict):
        for key, value in data.items():
            node_id = f"{parent}_{key}"
            dot.node(node_id, key)
            dot.edge(parent, node_id)
            json_to_dot(value, dot, node_id)
    elif isinstance(data, list):
        for i, item in enumerate(data):
            node_id = f"{parent}_{i}"
            dot.node(node_id, str(i + 1))  # numbered
            dot.edge(parent, node_id)
            json_to_dot(item, dot, node_id)
    else:
        value_node = f"{parent}_value"
        dot.node(value_node, str(data))
        dot.edge(parent, value_node)

    return dot

def render_aws_architecture(nodes_data, edges_data, out_path):
    with Diagram("Arquitectura AWS", filename=out_path, outformat="png"):
        nodes = {}
        for node in nodes_data:
            node_id = node["id"]
            node_type = node["type"]
            label = node.get("label", node_id)

            cls = node_types.get(node_type)
            if not cls:
                raise ValueError(f"Tipo no soportado: {node_type}")

            nodes[node_id] = cls(label)

        for src_id, tgt_id in edges_data:
            nodes[src_id] >> nodes[tgt_id]
