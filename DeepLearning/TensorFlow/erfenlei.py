import tensorflow as tf

from numpy.random import RandomState

#定义训练数据batch的大小
batch_size = 8

#定义神经网络的参数
w1 = tf.Variable(tf.random_normal([2, 3], stddev = 1, seed = 1))
w2 = tf.Variable(tf.random_normal([3,1],stddev=1,seed=1))

#在shape的一个维度上使用None可以方便使用不大的batch大小，在训练时需要把数据分成
#比较小的batch，但是在测试时，可以一次性使用全部的数据