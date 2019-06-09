# Quantum SAT solver with Grover


## Usage

    usage: run.py [-h] [-v] [-a] [-b] [--output_filter OUTPUT_FILTER]
                  [-i INPUT]

    Solve SAT instance by reading from stdin using an iterative or recursive
    watchlist-based backtracking algorithm. Recursive algorithm is used by
    default, unless the --iterative flag is given. Empty lines and lines that
    starting with a # will be ignored.

    optional arguments:
      -h, --help            show this help message and exit
      -v, --verbose         verbose output.
      -a, --all             output all possible solutions.
      -b, --brief           brief output for assignemnts: outputs variables
                            assigned 1.
      --output_filter OUTPUT_FILTER
                            only output variables with name-string with given
                            string.
      --iterative           use the iterative solver.
      -i INPUT, --input INPUT
                            read from given file instead of stdin.

## Example Usage

    $ python run.py -v -i examples/03.in.txt
    
    

## Reference
\[1\] []()
