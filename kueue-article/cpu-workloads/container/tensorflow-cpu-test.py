import numpy as np
import tensorflow as tf
import datetime
import sys

tf.compat.v1.disable_eager_execution()

# Processing Units logs
log_device_placement = True

# Num of multiplications to perform
n = 10


def run_multiplication(num: int):
    '''
    Example: compute A^n + B^n on CPUs
    '''
    # Create random large matrix
    A = np.random.rand(num, num).astype('float32')
    B = np.random.rand(num, num).astype('float32')

    # Create a graph to store results
    c1 = []
    c2 = []

    def matpow(M, n):
        if n < 1: #Abstract cases where n < 1
            return M
        else:
            return tf.matmul(M, matpow(M, n-1))

    '''
    Single CPU computing
    '''
    with tf.device('/cpu:0'):
        a = tf.compat.v1.placeholder(tf.float32, [num, num])
        b = tf.compat.v1.placeholder(tf.float32, [num, num])
        # Compute A^n and B^n and store results in c1
        c1.append(matpow(a, n))
        c1.append(matpow(b, n))

    with tf.device('/cpu:0'):
        sum = tf.add_n(c1) #Addition of all elements in c1, i.e. A^n + B^n

    t1_1 = datetime.datetime.now()
    with tf.compat.v1.Session(config=tf.compat.v1.ConfigProto(log_device_placement=log_device_placement)) as sess:
        # Run the op.
        sess.run(sum, {a:A, b:B})
    t2_1 = datetime.datetime.now()

    print("Single CPU computation time: " + str(t2_1-t1_1))

if __name__ == "__main__":
    num = int(sys.argv[1])
    print(f"Starting multiplication for {num}x{num} matrix...")
    run_multiplication(num=num)
    print("Multiplication completed.")