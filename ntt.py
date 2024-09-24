import numpy as np
import math

def forward_negacyclic_ntt(a, n, q, root):
    """Computes the forward negacyclic NTT of input array a."""
    res = [0]*n
    for j in range (n):
        for i in range(n):
            res[j] += root**(2*i*j+i)* a[i]
        res[j] = res[j] % q

    return res

def forward_negacyclic_fast_ntt(a, n, q, root):
    """Computes the forward negacyclic NTT of input array a."""
    res = [0]*n
    stage = math.log(n, 2)

    while stage>0:


        stage=stage-1

    return res

def inverse_negacyclic_ntt(a, n, q, root):
    """Computes the inverse negacyclic NTT of input array a."""
    res = [0]*n
    for j in range (n):
        for i in range(n):
            res[j] += pow(root, -2*i*j-j, q) * a[i] 
        res[j] = pow(n, -1, q) * res[j] % q

    return res

# def compute_twiddle_factors(psi, N, q):
#     return [pow(psi, i, q) for i in range(N)]

def reverse_bits(num, bit_size):
    reversed_num = 0
    for i in range(bit_size):
        reversed_num = (reversed_num << 1) | (num & 1)
        num >>= 1
    return reversed_num

def compute_twiddle_factors(psi, N, q):
    bit_size = N.bit_length() - 1  # Number of bits needed to represent indices from 0 to N-1
    twiddle_factors = [pow(psi, i, q) for i in range(N)]
    
    # Create a list with the twiddle factors in bit-reversed order
    return [twiddle_factors[reverse_bits(i, bit_size)] for i in range(N)]


def butterfly(x0, x1, td_f, q):
    return (x0+td_f*x1)%q, (x0-td_f*x1)%q

import math

# def fast_ntt(x, twiddles, N, q):
#     """
#     Compute the NTT of input x in stages using precomputed twiddle factors and butterfly function.
    
#     :param x: Input array of size N
#     :param twiddles: Precomputed list of twiddle factors (length depends on N)
#     :param N: Length of the input array (should be a power of 2)
#     :param q: Modulus for the field
#     :return: Transformed array (NTT of input x)
#     """
#     # Number of stages is log2(N)
#     stages = int(math.log2(N))
#     for stage in range(stages):
#         distance = 2 ** (stages - stage - 1)  
#         for i in range(0, N, 2 * distance):
#             for j in range(distance):   
#                 idx0 = i + j
#                 idx1 = i + j + distance
#                 print(2*idx1+1)
#                 x[idx0], x[idx1] = butterfly(x[idx0], x[idx1], twiddles[2], q)
#         print(x)

#     return x

def fast_ntt(a, twiddles, N, q):
    t=N
    m=1
    while m<N:
        t = t//2
        for i in range(m):
            j1 = 2*i*t
            j2 = j1+t-1

            S = twiddles[m+i]
            for j in range(j2+1):
                U = a[j]
                V = a[j+t]
                a[j] = U+V % q
                a[j+t] = U-V % q
        m = m * 2

    return a



# Parameters
n = 4  # Length of input, must be a power of 2
q = 7681  # A prime modulus such that q ≡ 1 (mod 2n)
psi = 1925  # Primitive 2n-th root of unity modulo q

# Input array (example)
a = [1, 2, 3, 4]
# b = [5, 6, 7, 8]

# Compute forward negacyclic NTT
# ntt_a = forward_negacyclic_ntt(a, n, q, root)
# print(compute_twiddle_factors(psi, n, q))
twiddle_factors = compute_twiddle_factors(psi, n, q)
print(twiddle_factors)
ntt_a = fast_ntt(a, twiddle_factors, n, q)
print(ntt_a)
# ntt_b = forward_negacyclic_ntt(b, n, q, root)

# ntt_c = np.multiply(ntt_a, ntt_b)


# Compute inverse negacyclic NTT
inverse_result = inverse_negacyclic_ntt(ntt_a.copy(), n, q, psi)
print("Inverse NTT Result:", inverse_result)
