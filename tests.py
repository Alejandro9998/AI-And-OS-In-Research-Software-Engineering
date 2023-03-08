import unittest
from article_analysis import *

class TestArticleAnalysis(unittest.TestCase):

    def test_text_extraction(self):
        text = extract_text("article1.pdf")
        self.assertEqual(type(text), str)
        self.assertNotEqual(len(text), 0)
        
    def test_keyword_extraction(self):
        text = extract_text("article1.pdf")
        keywords = extract_keywords(text)
        self.assertEqual(type(keywords), list)
        self.assertNotEqual(len(keywords), 0)
        
    def test_figure_count(self):
        text = extract_text("article1.pdf")
        figure_count = count_figures(text)
        self.assertEqual(type(figure_count), int)
        self.assertGreaterEqual(figure_count, 0)
        
    def test_link_extraction(self):
        links = extract_links("article1.pdf")
        self.assertEqual(type(links), list)
        self.assertNotEqual(len(links), 0)
        
if __name__ == '__main__':
    unittest.main()
