# Nucleosynthesis in a crude stellar model

## 1. Model
A star is represented by a pair of random matrices: proton number `z`
and neutron number `n`. The resultant mass number matrix `a = z + n`
serves well for most of the computation. Its initial chemical
composition is that of Hydrogen and Deuterium, similar to a protostar.

**The square matrix dimensions are determined by** `dim` **in main.py.**

## 2. Gravitation
The Newtonian gravitational force vector is computed for every element
in the mass number matrix. The components are normalised as weighted
probabilities of movement in that particular direction.

## 3. Nuclear fusion
Once the core temperature exceeds the threshold, fusion begins. For
every element in the mass number matrix, a neighbouring element is
selected at random. All possible nuclear reactions between the two
elements are identified and, based on their Q values, normalised as
weighted probabilities.

## 4. Probabilistic nature
The code implements movement of elements under gravity and the selection
of nuclear reactions through the generation of random numbers amongst
the weighted probabilities, lending a heavily statistical approach to
the evolution of the star.

## 5. Output
When the main module is first executed, a log.txt file and an images
directory will be created. The iterated chemical compositions will be
written to the former, while the graphical results will be stored in
the latter. The console only counts the iterations and logs the stellar
fuel remaining so that the user may intuit the program execution time.
