import json
import os
import sys

# Agregar la raíz del proyecto al path para imports
# Esto funciona tanto localmente como en GitHub Actions
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from src.app import lambda_handler


def test_lambda_handler():
    """Prueba básica del handler de Lambda"""
    # Simular evento de API Gateway GET /hello
    event = {
        "httpMethod": "GET",
        "path": "/hello",
        "queryStringParameters": None
    }
    context = None
    
    response = lambda_handler(event, context)
    
    # Validar estructura de respuesta
    assert response["statusCode"] == 200, f"Expected 200, got {response['statusCode']}"
    
    # Validar cuerpo de la respuesta
    body = json.loads(response["body"])
    assert "message" in body, "Response body should contain 'message' key"
    assert body["message"] == "Hello World", f"Expected 'Hello World', got {body['message']}"
    
    print("✅ Test passed: lambda_handler returns correct response")
