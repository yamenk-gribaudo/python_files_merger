import unittest
import python_files_merger

class Circular_dependencies(unittest.TestCase):

    def test_not_circular_dependency(self):
        input_ = [
            {'parents': ["a"], 'dependencies':["b"]}, 
            {'parents': ["b"], 'dependencies':["c"]},
            {'parents': ["c"], 'dependencies':[]}
        ]
        output = python_files_merger.find_circular_dependencies(input_)
        self.assertEqual(0, len(output))
        
    def test_circular_dependency(self):
        input_ = [
            {'parents': ["a"], 'dependencies':["b"]}, 
            {'parents': ["b"], 'dependencies':["a"]}
        ]
        output = python_files_merger.find_circular_dependencies(input_)
        self.assertEqual(3, len(output))

    def test_no_parents(self):
        input_ = [
            {'dependencies':["b"]}, 
        ]
        self.assertRaises(TypeError, python_files_merger.find_circular_dependencies, input_)

    def test_is_dependency_but_not_parent(self):
        input_ = [
            {'parents': ["a"], 'dependencies':["b"]}, 
            {'parents': ["b"], 'dependencies':["c"]},
        ]
        output = python_files_merger.find_circular_dependencies(input_)
        self.assertEqual(0, len(output))


    def test_parent_with_multiple_dependencies(self):
        input_ = [
            {'parents': ["a"], 'dependencies':["b","c","d"]}, 
            {'parents': ["b"], 'dependencies':["c"]},
            {'parents': ["c"], 'dependencies':["d","e"]},
            {'parents': ["d"], 'dependencies':["e", "f"]},
            {'parents': ["e"], 'dependencies':["b", "a"]},
        ]
        output = python_files_merger.find_circular_dependencies(input_)
        self.assertEqual(4, len(output))

if __name__ == '__main__':
    unittest.main()
