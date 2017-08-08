import tensorflow as tf
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "5"

vars_to_rename = {
     "s2vt/LSTM1/basic_lstm_cell/kernel": "s2vt/LSTM1/basic_lstm_cell/weights",
     "s2vt/LSTM1/basic_lstm_cell/bias": "s2vt/LSTM1/basic_lstm_cell/biases",
     "s2vt/LSTM2/basic_lstm_cell/kernel": "s2vt/LSTM2/basic_lstm_cell/weights",
     "s2vt/LSTM2/basic_lstm_cell/bias": "s2vt/LSTM2/basic_lstm_cell/biases",
}
new_checkpoint_vars = {}
reader = tf.train.NewCheckpointReader('/home/lijun/tensor_examples/res_models1/batch_size16model-12')
for old_name in reader.get_variable_to_shape_map():
  if old_name in vars_to_rename:
    new_name = vars_to_rename[old_name]
  else:
    new_name = old_name
  new_checkpoint_vars[new_name] = tf.Variable(reader.get_tensor(old_name))

init = tf.global_variables_initializer()
saver = tf.train.Saver(new_checkpoint_vars, write_version=1)

with tf.Session() as sess:
  sess.run(init)
  saver.save(sess, '/home/lijun/tensor_examples/res_models1/resnet_lstm')
