import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_html_to_props(self):
        node = HTMLNode("a","Link to my site", None, {"href": "https://example.com", "class": "magic-link"})
        str_props = node.props_to_html()
        self.assertEqual('href="https://example.com" class="magic-link"', str_props)

    def test_html_to_props_equal(self):
        node = HTMLNode("a","Link to my site", None, {"href": "https://example.com", "class": "magic-link"})
        node2 = HTMLNode("a","Link to my site", None, {"href": "https://example.com", "class": "magic-link"})
        self.assertEqual(node.props_to_html(), node2.props_to_html())

if __name__ == "__main__":
    unittest.main()
