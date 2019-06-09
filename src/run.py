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


def grover_solution(m, n, hr, i, b):
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
        i_read = pytesseract.image_to_string(Image.open(
            i.name), lang='eng', config='-c preserve_interword_spaces=1')
        print(i_read)
        print(len(i_read))

    sat_oracle = SAT(sat_cnf)
    algorithm = Grover(sat_oracle)

    if b:
        backend = least_busy(IBMQ.backends(simulator=False))
    else:
        backend = Aer.get_backend('qasm_simulator')

    result = algorithm.run(backend)
    print(result['result'])
    plot_histogram(result['measurements'])


def main():
    args = parse_args()
    grover_solution(args.variable, args.equation,
                    args.hand_recognition, args.file_input, args.real_backend)


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
                        help='read from given file instead of stdin (still needs to be implemented)')
    parser.add_argument('-b',
                        '--real_backend',
                        action='store_true',
                        default=False,
                        help='if set is True for a real IBM Q backend and False (default) for the simulator Aer backend.)')

    return parser.parse_args()


if __name__ == "__main__":
    main()
