# test_cubestorm.py
"""
Tests for CubeStorm module.
"""

import unittest
from cubestorm import CubeStorm

class TestCubeStorm(unittest.TestCase):
    """Test cases for CubeStorm class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CubeStorm()
        self.assertIsInstance(instance, CubeStorm)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CubeStorm()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
