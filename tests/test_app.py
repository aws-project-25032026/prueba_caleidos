# tests/test_app.py
"""Pruebas unitarias para Caleidos Hello API"""
import json
import os
import sys

# ⚠️ IMPORTANTE: Configurar path ANTES de cualquier import de la app
_project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if _project_root not in sys.path:
    sys.path.insert(0, _project_root)
# Ahora sí podemos importar de src/
from src.app import lambda_handler


def test_lambda_handler():
    """Prueba básica: GET /hello retorna Hello World"""
    event = {"httpMethod": "GET", "path": "/hello"}
    context = None
    
    response = lambda_handler(event, context)
    
    # Validar respuesta
    assert response["statusCode"] == 200, f"Esperaba 200, obtuvo {response['statusCode']}"
    
    body = json.loads(response["body"])
    assert "message" in body, "La respuesta debe contener 'message'"
    assert body["message"] == "Hola Mundo", f"Esperaba 'Hola Mundo', obtuvo '{body['message']}'"
