#!/usr/bin/python3
""" Test file. """
import unittest
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO
import os

class TestHBNBCommand(unittest.TestCase):
    """ Test module. """
    def test_EOF(self):
        """ Tests the EOF to ensure it behaves as expected. """
        cmd_instance = HBNBCommand()
        result = cmd_instance.do_EOF('')
        self.assertTrue(result)

    def setUp(self):
        """ Prepare environment for the tests. """
        self.cmd_instance = HBNBCommand()
        self.mock_print_patcher = patch('builtins.print')
        self.mock_print = self.mock_print_patcher.start()
        self.mock_eval_patcher = patch('console.eval')
        self.mock_eval = self.mock_eval_patcher.start()

    def tearDown(self):
        """ Clean up after each test method. """
        self.mock_print_patcher.stop()
        self.mock_eval_patcher.stop()
    
    def test_do_create_with_no_args(self):
        """ Test do_create with no arguments to check for error message. """
        self.cmd_instance.do_create('')
        self.mock_print.assert_called_once_with("** class name missing **")

    def test_quit(self):
        """ Tests do_quit to sure it behaves as expected. """
        cmd_instance = HBNBCommand()
        result = cmd_instance.do_quit('')
        self.assertTrue(result)

    def test_empty_line(self):
        """ Testing empty line. """
        cmd_instance = HBNBCommand()
        try:
            cmd_instance.emptyline()
        except Exception as excep:
            self.fail(f"emptyline raised Exception{excep}")

    def test_do_create(self):
        """ Testing do create. """
        