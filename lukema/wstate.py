from qiskit import QuantumCircuit
from numpy import matrix
from cmath import cos, sin, acos, sqrt

def W(theta):
    return matrix([[cos(theta), sin(theta)], [sin(theta), -cos(theta)]])
    
def Wstate(n):
    """Returns a QuantumCircuit with n qubits which are entangled in a W state

    Classical arguments:
    n -- the number of qubits and the order of the W state
    
    Quantum arguments:
    0..n -- expects zeroes to be supplied in all inputs
    
    Algorithm is from https://arxiv.org/pdf/1606.09290.pdf
    """
    w = QuantumCircuit(n)
    
    w.x(0)
    for i in range(n - 1):
        theta = 1/2 * acos(1/sqrt(n - i)) # note: paper (12) is wrong, 1/4 is incorrect

        w.unitary(W(theta), i + 1, label=f'W{i}')
        w.cz(i + 1, i)
        w.unitary(W(theta), i + 1, label=f'W{i}')
        
        w.cx(i + 1, i)

    return w.to_instruction(label="W state")