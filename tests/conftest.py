# tests/conftest.py
"""Configuración global para pytest - se ejecuta antes de la colección de tests"""
import os
import sys

# Agregar raíz del proyecto al PYTHONPATH antes de cualquier import
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)
