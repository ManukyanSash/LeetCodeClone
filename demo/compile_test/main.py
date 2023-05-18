import sys
from compile import compile_code as Compile

if __name__ == "__main__":
    Compile(sys.argv[1], "res.json")
