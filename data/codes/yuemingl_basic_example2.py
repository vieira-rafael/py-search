# This example shows the matrix multiplicationimport tensorflow as tf
# Launch a sessionsess = tf.Session()
#1x2 matrixm1=tf.constant([[3.,3.]])#2x1 matrixm2=tf.constant([[1.],[2.]])
print sess.run(m1)#[[ 3.  3.]]print sess.run(m2)#[[ 1.]# [ 2.]]print sess.run(tf.matmul(m1,m2))#[[ 9.]]print sess.run(tf.matmul(m2,m1))#[[ 3.  3.]# [ 6.  6.]]
# The operator overloading is not correctly supported now.# The follow will return the same resultprint sess.run(m1*m2)print sess.run(m2*m1)#[[ 3.  3.]# [ 6.  6.]]