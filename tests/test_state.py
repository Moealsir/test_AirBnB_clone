"""whew"""
import unittest
import sys
from unittest.mock import patch
import unittest
from models.base_model import BaseModel
from models.state import State
from datetime import datetime
sys.path.append('../')


class TestState(unittest.TestCase):
    """whew"""

    def test_state_inheritance(self):
        """whew"""
        self.assertTrue(issubclass(State, BaseModel))

    def test_state_attributes(self):
        """whew"""
        state = State()
        self.assertTrue(hasattr(state, "id"))
        self.assertTrue(hasattr(state, "created_at"))
        self.assertTrue(hasattr(state, "updated_at"))
        self.assertTrue(hasattr(state, "name"))
        self.assertEqual(state.name, "")

    def test_state_attribute_type(self):
        """whew"""
        state = State()
        self.assertIsInstance(state.id, str)
        self.assertIsInstance(state.created_at, datetime)
        self.assertIsInstance(state.updated_at, datetime)
        self.assertIsInstance(state.name, str)

    @patch('models.state.BaseModel.save')
    def test_state_save(self, mock_save):
        """whew"""
        state = State()
        state.save()
        mock_save.assert_called_once()

    @patch('models.state.BaseModel.to_dict')
    def test_state_to_dict(self, mock_to_dict):
        """whew"""
        state = State()
        state.to_dict()
        mock_to_dict.assert_called_once()

    def test_state_init_no_args(self):
        """whew"""
        state = State()
        self.assertIsInstance(state, State)

    def test_state_init_kwargs(self):
        """whew"""
        kwargs = {
            "id": "1234",
            "created_at": datetime.utcnow().isoformat(),
            "updated_at": datetime.utcnow().isoformat(),
            "name": "California"
        }
        state = State(**kwargs)
        for key, value in kwargs.items():
            if key in ["created_at", "updated_at"]:
                value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
            self.assertEqual(getattr(state, key), value)

    def test_state_str(self):
        """whew"""
        state = State()
        expected_format = f"[State] ({state.id}) {state.__dict__}"
        self.assertEqual(str(state), expected_format)


if __name__ == "__main__":
    unittest.main()
