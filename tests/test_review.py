"""whew"""
import unittest
import sys
from unittest.mock import patch
import unittest
from datetime import datetime
from models.review import Review
from models.base_model import BaseModel
sys.path.append('../')


class TestReview(unittest.TestCase):
    """whew"""

    def test_inheritance(self):
        """whew"""
        review = Review()
        self.assertIsInstance(review, BaseModel)

    def test_attributes(self):
        """whew"""
        review = Review()
        self.assertTrue(hasattr(review, "id"))
        self.assertTrue(hasattr(review, "created_at"))
        self.assertTrue(hasattr(review, "updated_at"))
        self.assertTrue(hasattr(review, "place_id"))
        self.assertTrue(hasattr(review, "user_id"))
        self.assertTrue(hasattr(review, "text"))
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_id_is_unique(self):
        """whew"""
        review1 = Review()
        review2 = Review()
        self.assertNotEqual(review1.id, review2.id)

    def test_dates_are_datetime(self):
        """whew"""
        review = Review()
        self.assertIsInstance(review.created_at, datetime)
        self.assertIsInstance(review.updated_at, datetime)

    def test_str_representation(self):
        """whew"""
        review = Review()
        expected_format = f"[Review] ({review.id}) {review.__dict__}"
        self.assertEqual(expected_format, review.__str__())

    def test_save(self):
        """whew"""
        review = Review()
        old_updated_at = review.updated_at
        review.save()
        self.assertNotEqual(old_updated_at, review.updated_at)

    @patch('models.review.Review.save')
    def test_save_called(self, mock_save):
        """whew"""
        review = Review()
        review.save()
        mock_save.assert_called_once()

    def test_to_dict_contains_right_keys(self):
        """whew"""
        review = Review()
        self.assertIn("id", review.to_dict())
        self.assertIn("created_at", review.to_dict())
        self.assertIn("updated_at", review.to_dict())

    def test_to_dict_contains_added_attribute(self):
        """whew"""
        review = Review()
        review.new_attribute = "value"
        self.assertIn("new_attribute", review.to_dict())

    def test_to_dict_correct_time_format(self):
        """whew"""
        review = Review()
        review_dict = review.to_dict()
        self.assertEqual(type(review_dict["created_at"]), str)
        self.assertEqual(type(review_dict["updated_at"]), str)

    def test_init_from_dict(self):
        """whew"""
        review_dict = {
            "id": "some-id",
            "created_at": "2021-02-11T00:49:50.921259",
            "updated_at": "2021-02-11T00:49:52.921259",
            "place_id": "some-place-id",
            "user_id": "some-user-id",
            "text": "some-text"
        }
        review = Review(**review_dict)
        self.assertEqual(review.id, review_dict["id"])
        self.assertEqual(review.place_id, review_dict["place_id"])
        self.assertEqual(review.user_id, review_dict["user_id"])
        self.assertEqual(review.text, review_dict["text"])

    def test_init_from_empty_dict(self):
        """whew"""
        review = Review(**{})
        self.assertIsInstance(review, Review)
        self.assertTrue(hasattr(review, "id"))
        self.assertTrue(hasattr(review, "created_at"))
        self.assertTrue(hasattr(review, "updated_at"))
        self.assertTrue(hasattr(review, "place_id"))
        self.assertTrue(hasattr(review, "user_id"))
        self.assertTrue(hasattr(review, "text"))


if __name__ == '__main__':
    unittest.main()
