# My Iteration - FAI Iteration
Author: Muhammad Imran Riaz

## Problem
Simple Picard iteration v_{n+1} = K(v_n) does not always converge.
For K(v) = 1 - v, it keeps oscillating and never reaches p = 0.5.

## My Method - FAI Iteration
I made this iteration myself by breaking Picard into three steps:

l_n = K((1 - a_n)v_n + a_n*K(v_n))
z_n = K((1 - b_n)l_n + b_n*K(l_n))
v_{n+1} = K^2(z_n)

## My Result
My FAI iteration reached in 2-3 iterations.
Picard-SP took 8, P took 27, Noor took 24.

## What I learned
Breaking one step into three steps makes convergence faster.
This is my base method. I will use it for HIV model and Cryptography.
