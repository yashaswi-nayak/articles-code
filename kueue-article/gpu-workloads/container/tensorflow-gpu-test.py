import numpy as np
import tensorflow as tf
import datetime
import sys

# Processing Units logs
log_device_placement = True
tf.debugging.set_log_device_placement(log_device_placement)

# Num of multiplications to perform
n = 10

def run_multiplication(num: int):
    '''
    Example: compute A^n + B^n on GPUs
    '''
    # Create random large matrix
    A = np.random.rand(num, num).astype('float32')
    B = np.random.rand(num, num).astype('float32')

    @tf.function
    def matpow(M, n):
        if n < 1:
            return M
        else:
            return tf.matmul(M, matpow(M, n - 1))
    
    # Compute A^n and B^n using the GPU
    # tf.add takes a list of tensors and adds them
    @tf.function
    def compute_sum(A_tensor, B_tensor):
        c1 = matpow(A_tensor, n)
        c2 = matpow(B_tensor, n)
        return c1 + c2

    # Convert NumPy arrays to TensorFlow Tensors
    A_tensor = tf.convert_to_tensor(A)
    B_tensor = tf.convert_to_tensor(B)

    t1_1 = datetime.datetime.now()
    # The first call to the function will trace and compile the graph
    compute_sum(A_tensor, B_tensor)
    t2_1 = datetime.datetime.now()

    print("Single GPU computation time: " + str(t2_1 - t1_1))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script_name.py <matrix_size>")
        sys.exit(1)
        
    num = int(sys.argv[1])
    print("GPUS ::: ", tf.config.list_physical_devices('GPU'))
    print(f"Starting multiplication for {num}x{num} matrix...")
    run_multiplication(num=num)
    print("Multiplication completed.")