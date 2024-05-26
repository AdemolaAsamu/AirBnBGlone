#!/usr/bin/env python3
"""
This is the console Module
HBNBCommand Class
"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.review import Review
from models.city import City
from models.place import Place
from models.amenity import Amenity
import re
import json

class HBNBCommand(cmd.Cmd):
    """
    HBNB Command Class Interpreter
    """

    prompt = "(hbnb) "

