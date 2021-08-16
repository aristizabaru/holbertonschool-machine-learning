#!/usr/bin/env python3
"""returns two placeholders"""
import tensorflow as tf


def create_placeholders(nx, classes):
    x = tf.placeholder(tf.float32, shape=(None, nx), name='x')
    y = tf.placeholder(tf.float32, shape=(None, classes), name='y')
    return (x, y)
