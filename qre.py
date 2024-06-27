# This is the main module that will be used for generating the Grover's circuit
# and then running the different QRE tools against the circuit.

from typing import List

from bitstring_util import generate_binary_string
from grovers import generate_grover_circuit

from qiskit import QuantumCircuit


def generate_marked_states(num_bits: int, num_states: int = 1) -> List[str]:
    ret_val = []
    for _ in range(num_states):
        ret_val.append(generate_binary_string(num_bits))
    return ret_val


def generate_qiskit_grovers(
    num_bits: int,
    num_states: int = 1,
) -> QuantumCircuit:
    # generate the marked states
    marked_states = generate_marked_states(num_bits, num_states)

    # pass marked states to generate Qiskit circuit
    return generate_grover_circuit(marked_states)
