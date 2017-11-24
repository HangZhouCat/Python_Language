import tensorflow as tf

#定义两个向量a和b
a = tf.constant([1.0,2.0],name='a')
b = tf.constant([2.0,3.0],name='b')

#这里a和b定义为了两个常量，一个为[1.0,2.0],另一个为[2.0,3.0]
#然后相加
result = a + b

sess = tf.Session()
print(sess.run(result))