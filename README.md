# Nucleosynthesis in a crude stellar model

The only preliminary is to create a directory named 'images'.

## 1. Model
A star is modelled as a pair of random matrices: proton number `z`
and neutron number `n`. The resultant mass number matrix `a = z + n`
serves well for most of the computation. Its initial chemical
composition is that of Hydrogen and Deuterium, similar to a protostar.

**The square matrix dimensions are determined by `dim` in main.py.**

## 2. Gravitation
The Newtonian gravitation force vector is computed for every element in
the mass number matrix. The components are normalised as weighted
probabilities of movement in that particular direction.

## 3. Nuclear fusion
For every element in the mass number matrix, a neighbouring element is
selected at random. All possible nuclear reactions between the two
elements are identified, and based on their Q values, normalised as
weighted probabilities.

## 4. Output
Data is written to a log.txt file, which will be created automatically
when the main module is first executed. The graphical results will be
saved in the images directory. The console only counts the iterations
and logs the fuel remaining so that the user may intuit the program
execution time.
