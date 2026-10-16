# ⚛️ Qubit Simulation

## 📖 Background

Quantum Computing is an emerging field in modern computing, fully based upon Quantum Mechanical phenomenons. While Quantum Computing might seem confusing at first and not make sense at all to you, do not worry. As you get into this field, you will realise that it gets much worse, but also, much more fun :D

In this PS, you will be tasked with creating a mathematical simulation representing qubits and the gates upon which they are applied.

## Introduction to Mathematical Qubits

We can represent a qubit mathematically in an extremely simplified way, that is, with matrices. At this time, it is a good idea to refer to a few resources and understand basic linear algebra and Qubit Mathematics. You may refer to the Resources Section for those, and from here onwards, it is presumed that you understand the basics of qubit mathematics.

Presuming every Single or Multi-Qubit system to be a Column Matrix, the application of gates upon them can be represented by matrix multiplication.

By Definition, since a Quantum Circuit is just a set of Gates applied upon multiple qubits, by representing multiple qubit systems by tensor products of individual qubit system, and layering gates upon this state, we can create a mathematical representation of the entire circuit with just simple linear algebra.

## Your Task

Your task is to create a program that takes in values for the number of qubits, along with the Gates that are applied unto qubits of different indices, and internally apply the relevant Matrix Algebra, before returning the probability of each state occurring in the entire system.

Presume that there are no index errors, Gate calling errors, and all other type of input typing errors during the input, and only valid gates are provided in the array, with valid parameters.

## Specification

Your Program must be capable of:

1. Taking in the value `N` as the number of qubits defined in the circuit.

2. Taking in an array of any length `[Arr]`.
   - The Array will be populated with elements representing gates and their parameters.
   - `A(n)` represents a single-qubit gate `A` applied to qubit `n`.
   - `n` being the indice of the qubit for the application of the Gate. Indicing starts from `0`, and ends at `N - 1`.
   - It is permitted to have more parameters for special Gates.
   - An example being `RZ(n,Theta)` or `SWAP(n,m)`.
   - `Theta` is in radians in decimal format.
   - `CNOT(control,target)`.
   - `TOFFOLI(control1,control2,target)`.
   - `SWAP(qubit1,qubit2)`.
   - Gates must be applied in the order in which they appear in the array.

3. Initialize all qubits in the `|0⟩` state.

4. Internally implement the Matrix Algebra.

5. Return an Array of `2^N` elements with:
   - The nth index corresponding to the probability of measuring the computational basis state represented by the binary representation of that index.
   - The sum of all elements adding up to `1`, up to normal floating-point precision.

6. You are currently only required to implement basic gates such as:
   - **H** — Hadamard
   - **X, Y, Z** — Pauli gates
   - **RX, RY, RZ** — Rotation gates
   - **CNOT**
   - **TOFFOLI**
   - **SWAP**

   You may implement some more, but document them and their calling functions carefully.

### Gate Conventions

- Qubit indices start at `0` and end at `N - 1`.
- The first qubit, qubit `0`, is the leftmost bit when displaying a computational basis state.
- `CNOT(control,target)` applies a NOT operation to the target qubit when the control qubit is in state `|1⟩`.
- `TOFFOLI(control1,control2,target)` applies a NOT operation to the target qubit when both control qubits are in state `|1⟩`.
- `SWAP(qubit1,qubit2)` exchanges the states of the specified qubits.
- `RX(qubit,Theta)`, `RY(qubit,Theta)`, and `RZ(qubit,Theta)` apply rotations around their respective axes by the angle `Theta`, measured in radians.

### Measurement Probabilities

The final state of an `N`-qubit system contains `2^N` probability amplitudes, one for each computational basis state.

The probability of measuring a particular state is the squared magnitude of its corresponding amplitude.

For a valid quantum state, the sum of all measurement probabilities must equal `1`, up to normal floating-point precision.

## Rules

- Any Programming Language may be used.
- Single File containing the Function, mentioned clearly (Helper Function Allowed).
- Capable of being able to run in your terminal.
- You may utilize external libraries only for the  purpose ofmathematical efficiency (Do not utilize dedicated qubit simulation libraries, but for instance, you may utilize numpy in python to make calculation more efficient)

## Input Format

The input consists of two elements separated by a single space.

1. An Integer `N`.
2. An Array of Gates (non-spaced).
   - In the exact same format.
   - Square brackets and all.
   - Seriously, it needs to look exactly like this.

### Example Input

```text
2 [H(0),CNOT(0,1)]
```

This represents a circuit with two qubits. A Hadamard gate is applied to qubit `0`, followed by a CNOT gate with qubit `0` as the control and qubit `1` as the target.

### Input Syntax

Single-qubit gates:

```text
H(0)
X(1)
Y(0)
Z(1)
```

Rotation gates:

```text
RX(0,1.570796)
RY(1,3.141593)
RZ(0,0.785398)
```

Multi-qubit gates:

```text
CNOT(0,1)
TOFFOLI(0,1,2)
SWAP(0,1)
```

Multiple gates must be separated by commas inside the square brackets, with no spaces between the gates or their parameters.

The gate names shown above are case-sensitive.

## Output Format

The output must contain exactly `2^N` probabilities, one for each computational basis state.

The states must be displayed in ascending order of their corresponding integer indices, from `0` to `2^N - 1`.

Qubit `0` is the leftmost bit in the displayed computational basis states.

### Example Output

For the input:

```text
2 [H(0),CNOT(0,1)]
```

The output should be:

```text
Probability of state |00>: 0.500000
Probability of state |01>: 0.000000
Probability of state |10>: 0.000000
Probability of state |11>: 0.500000
```

The output must display probabilities, not probability amplitudes.

## 📚 Resources

### 1. Basics of Quantum Information (IBM)

[IBM Quantum Learning — Basics of Quantum Information](https://quantum.cloud.ibm.com/learning/en/courses/basics-of-quantum-information)

### 2. Linear Algebra — 3Blue1Brown

Only Basics for visualisation, no need to watch through everything. Just watch the first 4 videos.

[3Blue1Brown — Essence of Linear Algebra](https://youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)

## Closing Remarks

As stated before, Quantum Computing is nothing too complicated if we look at it mathematically. We hope this problem serves as a solid foundation and sparks your interest in further exploring quantum information systems.
