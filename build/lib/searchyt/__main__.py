import pprint
import logging

from searchyt import searchyt

def main():
    logging.basicConfig(format="[%(filename)s:%(lineno)d]:%(levelname)s: %(message)s", level=logging.INFO)
    s = searchyt()
    pp = pprint.PrettyPrinter(indent=2)

    inp = input("Search query: ")
    while inp != "exit":
        pp.pprint(s.search(inp))
        inp = input("Search query: ")

if __name__ == "__main__":
    main()