import pytest
import sys
import os
from authController import loginAuthController
from authController import registerAuthController
from authController import logoutAuthController


class TestUser:
    def test_login_one(self):
        user = loginAuthController("adm", "123")
        assert str(user["_id"]) == "60755ceaad36fc8351af484b"

    def test_login_two(self):
        user = loginAuthController(
            "13519079@std.stei.itb.ac.id", "noobmaster123")
        assert str(
            user["_id"]) == "6074302706c2945460aed695" and user["nama"] == "Jesson Yo"

    def test_login_three(self):
        user = loginAuthController("adm", "1234")
        assert user == None

    def test_register_one(self):
        response = registerAuthController("Jesson Yo", "13519079@std.stei.itb.ac.id",
                                          "kaoskakifiraun", "kaoskakifiraun", "081311111111", "Beverly Hills A207")
        assert response == "EMAILALREADYREGISTERED"

    def test_register_two(self):
        response = registerAuthController("Jesson Yo","13519079@std.stei.itb.ac.id","kaoskakifiraun","gajahmada","081311111111","Beverly Hills A207")
        assert response == "PASSNOTMATCH"
    def test_logout_one(self):
        response = logoutAuthController(None)
        assert response == "ALREADYLOGGEDOUT"
    def test_logout_two(self):
        user = loginAuthController("adm","123")
        response = logoutAuthController(user)
        assert response == None
