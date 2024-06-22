import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        props_to_test = {"href": "https://www.google.com", "target": "_blank"}
        test_node = HTMLNode("p", "paragraph", None, props_to_test)
        expected_return_prop = 'href="https://www.google.com" target="_blank"'
        print('Testing...', test_node)
        self.assertEqual(test_node.props_to_html(), expected_return_prop)


if __name__ == "__main__":
    unittest.main()
