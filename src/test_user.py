import pytest
import sys, os
from authController import loginAuthController

class TestUser:
    def test_one(self):
        user = loginAuthController("adm","123")
        assert 1==1
    def test_two(self):
        x = "hello"
        assert "e" in x