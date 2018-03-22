import numpy as np
from random import shuffle
from past.builtins import xrange

def softmax_loss_naive(W, X, y, reg):
  """
  Softmax loss function, naive implementation (with loops)

  Inputs have dimension D, there are C classes, and we operate on minibatches
  of N examples.

  Inputs:
  - W: A numpy array of shape (D, C) containing weights.
  - X: A numpy array of shape (N, D) containing a minibatch of data.
  - y: A numpy array of shape (N,) containing training labels; y[i] = c means
    that X[i] has label c, where 0 <= c < C.
  - reg: (float) regularization strength

  Returns a tuple of:
  - loss as single float
  - gradient with respect to weights W; an array of same shape as W
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)

  #############################################################################
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  num_train = X.shape[0]
  num_classes = W.shape[1]
  for i in range(0, num_train):
    scores = X[i].dot(W)
    C = np.max(scores)
    scores -= C
    correct_class_score = scores[y[i]]
    p = np.exp(correct_class_score) / np.sum(np.exp(scores))
    loss += -np.log(p)

    for j in range(0, num_classes):
      j_score = np.exp(scores[j]) / np.sum(np.exp(scores))
      dW[:, j] += (j_score - (j == y[i])) * X[i]

  # Right now the loss is a sum over all training examples, but we want it
  # to be an average instead so we divide by num_train.
  loss /= num_train
  dW /= num_train

  # Add regularization to the loss.
  loss += reg * np.sum(W * W)
  dW += 2 * reg * W
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW


def softmax_loss_vectorized(W, X, y, reg):
  """
  Softmax loss function, vectorized version.

  Inputs and outputs are the same as softmax_loss_naive.
  """
  # Initialize the loss and gradient to zero.

  #############################################################################
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################

  num_train = X.shape[0] #train
  num_classes = W.shape[1] # classes
  scores = X.dot(W)
  C = np.max(scores, axis=1)
  scores = (scores.T - C).T
  p = (np.exp(scores).T / np.sum(np.exp(scores), axis=1)).T
  y_i_p = p[np.arange(p.shape[0]), y]
  loss = np.sum(-np.log(y_i_p))

  y_mat = np.zeros(shape=(num_train, num_classes))
  y_mat[range(num_train), y] = 1
  dW = X.T.dot(p - y_mat)
  #dW -= X.T.dot(y_mat)

  # Right now the loss is a sum over all training examples, but we want it
  # to be an average instead so we divide by num_train.
  loss /= num_train
  dW /= num_train

  # Add regularization to the loss.
  loss += reg * np.sum(W * W)
  dW += 2 * reg * W
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW

