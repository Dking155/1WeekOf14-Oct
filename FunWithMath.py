#  Starting off
print(22 / 7)
print(355 / 113)
import math

print(9801 / (2206 * math.sqrt(2)))


def archimedes(numSides):
    innerAngleB = 360.0 / numSides
    halfAngleA = innerAngleB / 2
    oneHalfSideS = math.sin(math.radians(halfAngleA))
    sideS = oneHalfSideS * 2
    polygonCircumference = numSides * sideS
    pi = polygonCircumference / 2
    return pi


print(archimedes(8))
print(archimedes(16))

for sides in range(8, 100, 8):
    print(sides, archimedes(sides))

# experiment with the loop above alongside with the actual value of pi. How many
# side does it take to make the two close?
# Answer: It takes two sides

# Accumulators

acc = 0
for x in range(1, 6):
    acc = acc + x

print(acc)

# compute the sum of the first 100 even numbers
# compute the sum of the first 50 odd numbers
# compute the average of the first 100 odd numbers
# write a function that returns the average of the first N numbers, where
# N is a parameter
# write a function called factorial that computes the product of the first N
# numbers, where N is a parameter
# Each number in the fibonacci sequence is the sum of the previous two numbers
# the first two numbers ih the sequence are 1 and 1. Compute the 10th
# fibonacci number.
# Write a function to compute the Nth fibonacci number, where N is a parameter.
# you may assume that N will be greater than or equal to 3

acc = 0
for x in range(1, 100):
    acc = acc + x
print(acc)


acc = 0
for x in range(1, 50):
    acc = acc + x
    print(acc)

# A monte carlo simulation

import random

print(random.random())

# Boolean expressions
# > greater than
# >= greater or equal to
# < less than
# <= less than or equal to
# == the same as [equal to]
# != Not equal to
dogWeight = 25
print(dogWeight != 25)
catWeight = 15

# compound Boolean operators
# and
# or
# not

print(dogWeight > 30 or catWeight < 20)

# Decision making-- selection statements
a = 5
b = 10
c = 75

if a > b:
    c = 45

print(c)

if a > b:
    c = 45
    if b > c:
        a = 25
    else:
        a = -25
else:
    c = 1050

print(a, b, c)
