# test_zkgrid.py
"""
Tests for ZKGrid module.
"""

import unittest
from zkgrid import ZKGrid

class TestZKGrid(unittest.TestCase):
    """Test cases for ZKGrid class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ZKGrid()
        self.assertIsInstance(instance, ZKGrid)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ZKGrid()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
