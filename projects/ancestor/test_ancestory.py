import unittest
from ancestor import Graph


class Test(unittest.TestCase):

    '''
       10
     /
    1   2   4  11
     \ /   / \ /
      3   5   8
       \ / \   \
        6   7   9
    '''

    def test_earliest_ancestor(self):
        test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6),
                          (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
        g = Graph()
        g.add_nodes_and_edges(test_ancestors)
        self.assertEqual(g.find_ancestor(1), 10)
        self.assertEqual(g.find_ancestor(2), -1)
        self.assertEqual(g.find_ancestor(3), 10)
        self.assertEqual(g.find_ancestor(4), -1)
        self.assertEqual(g.find_ancestor(5), 4)
        self.assertEqual(g.find_ancestor(6), 10)
        self.assertEqual(g.find_ancestor(7), 4)
        self.assertEqual(g.find_ancestor(8), 4)
        self.assertEqual(g.find_ancestor(9), 4)
        self.assertEqual(g.find_ancestor(10), -1)
        self.assertEqual(g.find_ancestor(11), -1)


if __name__ == '__main__':
    unittest.main()
