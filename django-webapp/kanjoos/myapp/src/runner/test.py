import tensorflow as tf
import numpy as np
import os,glob,cv2
import sys,argparse



dir_path = os.path.dirname(os.path.realpath(__file__))
image_path=sys.argv[1]
filename = image_path
print(filename)
image_size=300
num_channels=3
images = []
image = cv2.imread(filename)
image = cv2.resize(image, (image_size, image_size), cv2.INTER_LINEAR)
cv2.imshow('output',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
images.append(image)
images = np.array(images, dtype=np.uint8)
images = images.astype('float32')
images = np.multiply(images, 1.0/255.0)
cv2.imshow('output',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
x_batch = images.reshape(1, image_size,image_size,num_channels)
sess = tf.Session()

saver = tf.train.import_meta_graph('/home/vijayaganesh/Desktop/Kanjoos/Logo Classifier.meta')

saver.restore(sess, tf.train.latest_checkpoint('./'))

graph = tf.get_default_graph()


y_pred = graph.get_tensor_by_name("y_pred:0")


x= graph.get_tensor_by_name("x:0")
y_true = graph.get_tensor_by_name("y_true:0")
y_test_images = np.zeros((1, 3))


feed_dict_testing = {x: x_batch, y_true: y_test_images}
result=sess.run(y_pred, feed_dict=feed_dict_testing)
print(result)
