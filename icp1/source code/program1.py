#import tensorflow libraries
import tensorflow as tf

# creating a session
sess = tf.Session()

# Creating a constant matrix A
mA = tf.constant([1,0,2,3])
# Running the below statement using the session
print("matrix mA :",sess.run(mA))

# Creating a constant matrix B
mB = tf.constant([2,0,4,5])
# Running the below statement using the session
print("matrix mA :",sess.run(mB))

# Creating a constant matrix C
mC = tf.constant([3,1,0,4])
# Running the below statement using the session
print("matrix mA :",sess.run(mC))
print("\n")

# Finding the square of matrix mA
A2 = tf.pow(mA,2)
print("power of matrix mA : a^2")
# Running the below statement using the session
print(sess.run(A2))
print("\n")

# Adding the matrix A2 and matrix mB
A2B = tf.add(A2,mB)
print("adding the matrix A2 and mB : (a^2)+b")
# Running the below statement using the session
print(sess.run(A2B))
print("\n")

# multiplying the matrix A2B and mC
A2BC = tf.multiply(A2B,mC)
print("final output :((a^2)+b)*c")
# Running the below statement using the session
print(sess.run(A2BC))