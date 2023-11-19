
import cky
from nltk.grammar import CFG
from nltk.tree import Tree


class TestCKY():

    def test_grammar_from_file(self):
        grammar = cky.grammar_from_file(
            "fernrohr_gramm.txt")
        assert isinstance(grammar, CFG)

    def test_initialize_chart(self):
        chart = cky.initialize_chart(
            "Hans beobachtet den Mann mit dem Fernrohr")
        assert len(chart) == 8

    def check_for_dict(self):
        chart = cky.initialize_chart(
            "Hans beobachtet den Mann mit dem Fernrohr")
        assert isinstance(chart[0][0], dict)

    def test_fernrohr(self):
        assert cky.cky("fernrohr_gramm.txt",
                       "Hans beobachtet den Mann mit dem Fernrohr")

    def test_fernrohr2(self):
        assert cky.cky("fernrohr_gramm.txt", "Hans sieht den Mann mit dem Fernrohr") == False

    def test_fernrohr_trees(self):
        trees = cky.cky("fernrohr_gramm.txt",
                        "Hans beobachtet den Mann mit dem Fernrohr", True)
        assert isinstance(trees, list)
        assert isinstance(trees[0], Tree)
        assert len(trees) == 2
