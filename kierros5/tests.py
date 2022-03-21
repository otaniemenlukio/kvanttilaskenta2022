from datetime import datetime
from qiskit import QuantumCircuit, Aer, transpile

separator = '-'*26
bits = '01'
states = [a + b + c for a in bits for b in bits for c in bits]

class full_adder_tests:
    def __init__(self, full_adder):
        self.qc = full_adder

    def run(self):
        print(f"{datetime.now().isoformat()} full_adder tests")
        print(separator)
        print("A B C sum --> e c correct?")

        numpassed = 0
        for state in states:
            qc = QuantumCircuit(5)
            qc.initialize(int(state, 2), [2, 1, 0])
            qc.append(self.qc, range(5))
            qc = qc.decompose()
            qc.measure_all()
            backend = Aer.get_backend('aer_simulator')
            output = list(backend.run(transpile(qc, backend)).result().get_counts().keys())
            assert len(output) == 1, "Output is non-deterministic! Expected only one possible result from the circuit."
            output = output[0]
            c = int(output[2], 2) # final sum
            e = int(output[0], 2) # carry
            sum_ = sum(map(lambda s: int(s, 2), state))
            correct = sum_ == 2*e + c
            print(f"{state[0]} {state[1]} {state[2]} {sum_:>3} --> {e} {c} {['wrong', 'correct'][correct]:>8}")
            if correct: numpassed += 1

        print(separator)
        print(f"{numpassed} out of {len(states)} tests passed.\n")

        return numpassed == len(states)

states2 = [[a, b] for a in states for b in states]

class adder3_tests:
    def __init__(self, adder):
        self.qc = adder

    def run(self):
        print(f"{datetime.now().isoformat()} adder (3bit) tests")
        print(separator)
        print("A B (A + B) -->  x correct?")

        numpassed = 0
        for a, b in states2:
            qc = QuantumCircuit(11, 4)
            qc.initialize(int(a, 2), range(0, 3))
            qc.initialize(int(b, 2), range(3, 6))
            qc.append(self.qc, range(11), range(4))
            qc = qc.decompose()
            backend = Aer.get_backend('aer_simulator')
            output = list(backend.run(transpile(qc, backend)).result().get_counts().keys())
            assert len(output) == 1, "Output is non-deterministic! Expected only one possible result from the circuit."
            x = output[0]
            inta = int(a, 2)
            intb = int(b, 2)
            intx = int(x, 2)
            correct = intx == inta + intb
            print(f"{inta} {intb} {inta + intb:>7} --> {intx:>2} {['wrong', 'correct'][correct]:>8}")
            if correct: numpassed += 1

        print(separator)
        print(f"{numpassed} out of {len(states2)} tests passed.\n")

        return numpassed == len(states2)

class uncomputeD_tests:
    def __init__(self, uncomputeD):
        self.qc = uncomputeD

    def run(self):
        print(f"{datetime.now().isoformat()} uncomputeD tests")
        print(separator)
        print("A B C --> d correct?")

        numpassed = 0
        for state in states:
            qc = QuantumCircuit(5)
            qc.initialize(int(state[::-1], 2), list(reversed(range(0, 3))))
            qc.append(self.qc, range(5))
            qc = qc.decompose()
            qc.measure_all()
            backend = Aer.get_backend('aer_simulator')
            output = list(backend.run(transpile(qc, backend)).result().get_counts().keys())
            assert len(output) == 1, "Output is non-deterministic! Expected only one possible result from the circuit."
            output = output[0]
            d = output[1]
            correct = d == '0'
            print(f"{state[0]} {state[1]} {state[2]} --> {d} {['wrong', 'correct'][correct]:>8}")
            if correct: numpassed += 1

        print(separator)
        print(f"{numpassed} out of {len(states)} tests passed.\n")

        return numpassed == len(states)