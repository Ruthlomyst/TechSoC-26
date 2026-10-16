# Decision Tree from Scratch

**Difficulty:** Beginner to Intermediate  
**Language:** Python  
**Reference video:** [Watch the Decision Tree tutorial](https://youtu.be/Okn4QkyTxe4?si=uaM11PdbearoHKZh)

## 1. Problem Overview

Decision Trees classify data by learning a sequence of feature-based decisions. In this challenge, you will build a Decision Tree classifier **from scratch** to understand how the algorithm selects splits, constructs a tree, and makes predictions.

Use the reference video to learn the concepts, but implement the required algorithm yourself.

## 2. Objectives

Your implementation must:

1. Calculate **entropy** to measure class-label impurity.
2. Calculate **information gain** for candidate feature splits.
3. Select the best feature at each node.
4. Build the tree recursively.
5. Include stopping conditions, such as pure nodes, no remaining features, and a configurable maximum depth.
6. Predict labels for unseen examples, including a documented fallback for an unseen branch.
7. Evaluate the model on a held-out test set.

## 3. Implementation Rules

**Allowed:** Python 3, NumPy, Pandas, Matplotlib, and standard Python libraries.

**Not allowed:** `sklearn.tree.DecisionTreeClassifier` or any other ready-made Decision Tree training or prediction implementation.

Entropy, information gain, feature selection, tree construction, and prediction must be implemented by you. Do not hard-code dataset-specific rules or predictions.

The core task may use categorical features. Support for continuous numerical features is an optional extension unless specified otherwise by the organizers.

## 4. Optional Extensions

Participants who finish the core task may implement one or more of the following:

- Support continuous features using threshold-based splits.
- Compare entropy with Gini impurity.
- Implement pruning to reduce overfitting.

## 5. Goal

Build a Decision Tree classifier that you can explain from its first entropy calculation to its final prediction. The focus is not only on achieving good accuracy, but also on understanding how the model makes decisions and how it generalizes to unseen data.


