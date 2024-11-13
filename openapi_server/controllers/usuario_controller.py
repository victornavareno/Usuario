import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.usuario import Usuario  # noqa: E501
from openapi_server import util


def usuario_email_delete(email):  # noqa: E501
    """Eliminar un usuario específico por su email

    Elimina un usuario específico del sistema # noqa: E501

    :param email: 
    :type email: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def usuario_email_get(email):  # noqa: E501
    """Obtener un usuario específico por su email

    Retorna la información de un usuario por su email # noqa: E501

    :param email: 
    :type email: str

    :rtype: Union[Usuario, Tuple[Usuario, int], Tuple[Usuario, int, Dict[str, str]]
    """
    return 'do some magic!'


def usuario_email_nombre_delete(email, nombre):  # noqa: E501
    """Eliminar un perfil específico de un usuario determinado por su email

    Elimina un perfil específico de un usuario # noqa: E501

    :param email: 
    :type email: str
    :param nombre: 
    :type nombre: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def usuario_email_nombre_get(email, nombre):  # noqa: E501
    """Obtener un perfil específico

    Retorna los datos de un perfil específico de un usuario # noqa: E501

    :param email: 
    :type email: str
    :param nombre: 
    :type nombre: str

    :rtype: Union[Usuario, Tuple[Usuario, int], Tuple[Usuario, int, Dict[str, str]]
    """
    return 'do some magic!'


def usuario_email_nombre_put(email, nombre):  # noqa: E501
    """Actualizar un perfil específico

    Actualiza un perfil específico de un usuario registrado en el sistema # noqa: E501

    :param email: 
    :type email: str
    :param nombre: 
    :type nombre: str

    :rtype: Union[Usuario, Tuple[Usuario, int], Tuple[Usuario, int, Dict[str, str]]
    """
    return 'do some magic!'


def usuario_email_perfil_get(email):  # noqa: E501
    """Obtener una lista de perfiles de un usuario

    Retorna la lista de perfiles de un usuario específico # noqa: E501

    :param email: 
    :type email: str

    :rtype: Union[List[Usuario], Tuple[List[Usuario], int], Tuple[List[Usuario], int, Dict[str, str]]
    """
    return 'do some magic!'


def usuario_email_perfil_post(email, usuario):  # noqa: E501
    """Añadir un nuevo perfil a un usuario

    Añade un nuevo perfil a un usuario dado su email # noqa: E501

    :param email: 
    :type email: str
    :param usuario: 
    :type usuario: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        usuario = Usuario.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def usuario_email_put(email):  # noqa: E501
    """Actualizar un usuario específico por su email

    Actualiza un usuario registrado en el sistema # noqa: E501

    :param email: 
    :type email: str

    :rtype: Union[Usuario, Tuple[Usuario, int], Tuple[Usuario, int, Dict[str, str]]
    """
    return 'do some magic!'


def usuario_get():  # noqa: E501
    """Obtener lista de usuarios registrados

    Retorna una lista de los usuarios registrados en la aplicación # noqa: E501


    :rtype: Union[List[Usuario], Tuple[List[Usuario], int], Tuple[List[Usuario], int, Dict[str, str]]
    """
    return 'do some magic!'


def usuario_post(usuario):  # noqa: E501
    """Crear un nuevo usuario

    Crea un nuevo usuario # noqa: E501

    :param usuario: 
    :type usuario: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        usuario = Usuario.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
