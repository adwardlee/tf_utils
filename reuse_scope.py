import tensorflow as tf

    with tf.variable_scope(scope_name) as scope:
        try:
            v = tf.get_variable(var, shape)
        except ValueError:
            scope.reuse_variables()
            v = tf.get_variable(var)
