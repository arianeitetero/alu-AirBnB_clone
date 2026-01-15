#!/usr/bin/python3
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def test_id_exists(self):
        b = BaseModel()
        self.assertTrue(hasattr(b, "id"))

    def test_to_dict(self):
        b = BaseModel()
        d = b.to_dict()
        self.assertEqual(d["__class__"], "BaseModel")


if __name__ == "__main__":
    unittest.main()
