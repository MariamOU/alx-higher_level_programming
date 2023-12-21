#!/usr/bin/python3
import importlib
"""Imports a variable and prints its value"""
if __name__ == "__main__":
    module = importlib.import_module('variable_load_5')
    print(module.a)
