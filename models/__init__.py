#!/usr/bin/python3
""" Init Method for our Console. """
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()