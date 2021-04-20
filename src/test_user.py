import pytest
import sys, os
from authController import loginAuthController
from authController import registerAuthController

class TestUser:
    def test_login_one(self):
        user = loginAuthController("adm","123")
        assert str(user["_id"]) == "60755ceaad36fc8351af484b"
    def test_login_two(self):
        user = loginAuthController("13519079@std.stei.itb.ac.id","noobmaster123")
        assert str(user["_id"]) == "6074302706c2945460aed695" and user["nama"] == "Jesson Yo"
    # def test_register_one(self):
    #     user = registerAuthController("Jesson Yo","13519079@std.stei.itb.ac.id")