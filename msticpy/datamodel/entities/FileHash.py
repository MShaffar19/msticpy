# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
"""FileHash Entity class."""
import pprint
from abc import ABC, abstractmethod
from enum import Enum
from ipaddress import IPv4Address, IPv6Address, ip_address
from typing import Any, Dict, Mapping, Type, Union, Optional

from ..._version import VERSION
from ...common.utility import export
from .entity import Entity

__version__ = VERSION
__author__ = "Ian Hellen"


_ENTITY_ENUMS: Dict[str, Type] = {}


@export
class FileHash(Entity):
    """
    File Hash class.

    Attributes
    ----------
    Algorithm : Algorithm
        FileHash Algorithm
    Value : str
        FileHash Value


    """

    def __init__(self, src_entity: Mapping[str, Any] = None, **kwargs):
        """
        Create a new instance of the entity type.

        Parameters
        ----------
        src_entity : Mapping[str, Any], optional
            Create entity from existing entity or
            other mapping object that implements entity properties.
            (the default is None)

        Other Parameters
        ----------------
        kwargs : Dict[str, Any]
            Supply the entity properties as a set of
            kw arguments.

        """
        super().__init__(src_entity=src_entity, **kwargs)

    @property
    def description_str(self) -> str:
        """Return Entity Description."""
        return f"{self.Algorithm}: {self.Value}"

    _entity_schema = {
        # The hash algorithm (type System.String)
        "Algorithm": "Algorithm",
        # Value (type System.String)
        "Value": None,
    }
