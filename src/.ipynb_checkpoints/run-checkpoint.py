"""
Solves SAT instance by reading from stdin using Qiskit framework from IBM.
For text recognition as input you have to set the path to your lib.
"""
import pylab
import numpy as np
from sys import stdin
import argparse
from argparse import ArgumentParser
from argparse import FileType
from PIL import Image
import pytesseract

from qiskit.providers.ibmq import least_busy
from qiskit import LegacySimulators, execute, IBMQ, Aer
from qiskit.tools.visualization import plot_histogram
from qiskit_aqua import QuantumInstance
from qiskit_aqua import run_algorithm
from qiskit_aqua.algorithms import Grover
from qiskit_aqua.components.oracles import SAT
# from qiskit_aqua.components.oracles import LogicalExpressionOracle


def grover_solution(m, n, hr, i):
    # normal parser
    if m and n is not None:
        satProblem = 'examples\\3sat' + m + '-' + n + '.cnf'
        with open(satProblem, 'r') as f:
            sat_cnf = f.read()
        print(sat_cnf)
    # hand recognition parser: still needs to be implemented
    elif hr:
        # tesseract parser
        pass
    else:
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        i_read = pytesseract.image_to_string(Image.open(i.name), lang='eng')
        print(i_read)

    sat_oracle = SAT(sat_cnf)
    algorithm = Grover(sat_oracle)
    backend = Aer.get_backend('qasm_simulator')
    algorithm = Grover(sat_oracle)
    result = algorithm.run(backend)
    print(result['result'])
    plot_histogram(result['measurements'])


def main():
    args = parse_args()
    grover_solution(args.variable, args.equation,
                    args.hand_recognition, args.file_input)


def parse_args():
    parser = ArgumentParser(
        description='Quantum SAT solver with Grovers algorithm')
    parser.add_argument('-m',
                        '--variable',
                        help='the number of variable for the SAT-Problem from examples')
    parser.add_argument('-n',
                        '--equation',
                        help='the number of equation for the SAT-Problem from examples')
    parser.add_argument('-hr',
                        '--hand_recognition',
                        action='store_true',
                        help='set to true, if your file is handwritten (still needs to be implemented)')
    parser.add_argument('-i',
                        '--file_input',
                        type=FileType('r'),
                        help='read from given file instead of stdin',)

    return parser.parse_args()


if __name__ == "__main__":
    main()
'''
 print('Type the number of m variables and on the next line the number of n equations for the SAT-Problem:')
    m = input()
    n = input()
    print('You set the SAT-Problem with ' + m +
          ' variables and ' + n + ' equations.')
    (m, n)


parser.add_argument('-i',
                        '--input',
                        help='read from given file instead of stdin',
                        type=FileType('r'),
                        default=stdin)
    parser.add_argument('-o',
                        '--output',
                        help='write to given file instead of default stdout',
                        type=FileType('w'),
                        default=stdout)

'''
