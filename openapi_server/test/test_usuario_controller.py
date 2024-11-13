import unittest

from flask import json

from openapi_server.models.usuario import Usuario  # noqa: E501
from openapi_server.test import BaseTestCase


class TestUsuarioController(BaseTestCase):
    """UsuarioController integration test stubs"""

    def test_usuario_email_delete(self):
        """Test case for usuario_email_delete

        Eliminar un usuario específico por su email
        """
        headers = { 
        }
        response = self.client.open(
            '/usuario/{email}'.format(email='email_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_usuario_email_get(self):
        """Test case for usuario_email_get

        Obtener un usuario específico por su email
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/usuario/{email}'.format(email='email_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_usuario_email_nombre_delete(self):
        """Test case for usuario_email_nombre_delete

        Eliminar un perfil específico de un usuario determinado por su email
        """
        headers = { 
        }
        response = self.client.open(
            '/usuario/{email}/{nombre}'.format(email='email_example', nombre='nombre_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_usuario_email_nombre_get(self):
        """Test case for usuario_email_nombre_get

        Obtener un perfil específico
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/usuario/{email}/{nombre}'.format(email='email_example', nombre='nombre_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_usuario_email_nombre_put(self):
        """Test case for usuario_email_nombre_put

        Actualizar un perfil específico
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/usuario/{email}/{nombre}'.format(email='email_example', nombre='nombre_example'),
            method='PUT',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_usuario_email_perfil_get(self):
        """Test case for usuario_email_perfil_get

        Obtener una lista de perfiles de un usuario
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/usuario/{email}/Perfil'.format(email='email_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_usuario_email_perfil_post(self):
        """Test case for usuario_email_perfil_post

        Añadir un nuevo perfil a un usuario
        """
        usuario = {"metodoPago":"tarjeta de credito","idUsuario":10,"perfiles":[{"imagen":["imagen","imagen"],"nombre":"nombre"},{"imagen":["imagen","imagen"],"nombre":"nombre"}],"email":"email","contraseña":"contraseña","status":"activo"}
        headers = { 
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/usuario/{email}/Perfil'.format(email='email_example'),
            method='POST',
            headers=headers,
            data=json.dumps(usuario),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_usuario_email_put(self):
        """Test case for usuario_email_put

        Actualizar un usuario específico por su email
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/usuario/{email}'.format(email='email_example'),
            method='PUT',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_usuario_get(self):
        """Test case for usuario_get

        Obtener lista de usuarios registrados
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/usuario',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_usuario_post(self):
        """Test case for usuario_post

        Crear un nuevo usuario
        """
        usuario = {"metodoPago":"tarjeta de credito","idUsuario":10,"perfiles":[{"imagen":["imagen","imagen"],"nombre":"nombre"},{"imagen":["imagen","imagen"],"nombre":"nombre"}],"email":"email","contraseña":"contraseña","status":"activo"}
        headers = { 
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/usuario',
            method='POST',
            headers=headers,
            data=json.dumps(usuario),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
