from nltk.grammar import CFG, Nonterminal
from nltk.tree import Tree


def cky(file: str, sentence: str, parser=False):
    """Main function for CKY Recognizer and Parser.

    Args:
    file: Filepath to a textfile containing a grammar in nltk format.
    sentence: Sentence to parse/recognize.
    parser: If True, sentence gets parsed, if False only recognized.

    Returns:
    True/False if called as Recognizer
    List of Tree Objects if called as Parser
    """
    pass


def grammar_from_file(file: str):
    """Read grammar from file.

    Args:
    file: Filepath to a textfile containing a grammar in nltk format.

    Returns:
    nltk grammar object
    """
    pass


def initialize_chart(sentence: str):
    """Initialize an empty chart of appropriate size.
    Size depends on input sentence.

    Args:
    sentence: Sentence to parse/recognize.

    Returns:
    Empty chart
    """
    pass


def terminal_rules(sentence: str, grammar: CFG, chart: list):
    """Applies all terminal rules to the sentence and fills in chart.

    Args:
    sentence: Sentence to parse/recognize.
    grammar: Grammar used for parsing/recognizing.
    chart: Empty chart.

    Returns:
    Filled in chart.
    """
    pass


def nonterminal_rules(sentence: str, grammar: CFG, chart: list):
    """Applies all nonterminal rules to the sentence and fills in chart.

    Args:
    sentence: Sentence to parse/recognize.
    grammar: Grammar used for parsing/recognizing.
    chart: Chart already filled in with terminal rules.
    """
    pass


def check_coverage(sentence: str, grammar: CFG, chart: list):
    """Checks if input sentence is in the language.

    Args:
    sentence: Sentence to parse/recognize.
    grammar: Grammar used for parsing/recognizing.
    chart: Completely filled out chart.

    Returns:
    True if covered, False if not.
    """
    pass


def generate_trees(chart: list, start: int, end: int, nonterminal: Nonterminal):
    """Recursively generates Tree objects from filled out chart.

    Args:
    chart: Completely filled out chart.
    start: Start index of parsed sentence.
    end: End index of parsed sentence.
    nonterminal: Current nonterminal the function is looking at.

    Returns:
    List of Tree objects
    """
    pass


def main(file: str, sentence: str, parser=False):
    cky(file, sentence, parser)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--file", type=str, help=("Path to a .txt file containing a grammar in nltk format."))

    parser.add_argument("--sentence", type=str, help=("Sentence to parse as string."))

    parser.add_argument("--parser", action="store_true", help=("Flag for choosing to run parser. If omitted, recognizer is run."))

    args = parser.parse_args()

    file = args.file
    sentence = args.sentence
    parser = args.parser

    main(file, sentence, parser)

