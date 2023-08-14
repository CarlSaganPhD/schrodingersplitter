![Quantum Decision Logo](static/assets/logodisplay.png)

Schrodingers Splitter interfaces with the Australian National University's quantum computer to assign an 'even' or 'odd' value, derived from its output, to a pair of choices you provide. By leveraging this quantum output, you've theoretically initiated a branching in the universe that aligns with your two options.

View demo: https://schrodingersplitter-1d82971d4b97.herokuapp.com/

## Instructions

1. Clone the repository and create a new virtual environment

2. Install the required libraries using the requirements.txt file

   ```
   pip install -r requirements.txt
   ```

4. Run the backend using:

   ```
   flask run
   ```

5. Visit ```127.0.0.1:5000``` on your browser

## About

Quantum systems can exist in a superposition of states, and when measured, they "collapse" to one of the possible states. The outcome isn't just difficult to predict; it's inherently unpredictable. See also: the famous [Double Slit Experiment](https://en.wikipedia.org/wiki/Double-slit_experiment)

### Qubits & Quantum Measurement:
At the heart of a quantum computer is the 'qubit', which is somewhat analogous to the 'bit' in classical computers but with superposition capabilities. In our case, the photon's polarization states can be thought of as representing a qubit. When a qubit is measured, it collapses to one of its base states, producing an output of either 0 or 1 with a certain probability.

### Generating Multiple Bits:
To generate a number between 0 and 255, we'd need an 8-bit number (since 2^8 = 256 possibilities ranging from 00000000 to 11111111 in binary, or 0 to 255 in decimal). This means we'd need to measure 8 qubits. If each qubit is represented by a photon's polarization state, we'd be measuring the state of 8 photons. Each photon provides one bit of information: 0 or 1.
From Bits to Numbers:

Once you have the 8 bits, you can concatenate them to form an 8-bit binary number. For example, you might end up with something like 01011010.
This binary sequence can be converted to a decimal number using standard binary to decimal conversion. For 01011010, the converted number is 90.

### Physical Realization:
The details of how the photons are produced, polarized, and measured depend on the specific quantum computer's architecture and technology. For instance, some quantum computers use trapped ions, others use superconducting circuits, and others, like the one we're referring to, might use photon polarization.
The photon's polarization states can be manipulated using optical components like polarizing beam splitters, wave plates, and detectors. When a photon passes through these components and reaches a detector, its state is 'measured', collapsing the superposition and giving us either a 0 or a 1.
