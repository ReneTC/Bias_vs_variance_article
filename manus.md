# Bias vs variance why being too smart is dumb

This my my entry to 3blue1browns summer of mathematics education..


Okay maybe "being too smart is dumb" is a little clickbaity, sorry! But it is a very interesting topic in machine learning that is absolute essential if you ever want to do something useful in machine learning.

It's the bias variance trade-off, or under-fitting vs over-fitting. This concept is absolutely fundamental and  applies to all machine learning models.. For example a neural network, decision tree or simple polynomial regression .. everything!

Let's get to it!

## supervised machine learning
When doing the common "supervised machine learning", the goal is to learn to take input and predict the correct output.
<p align="center"><img src="vid_files/2_mnist/input_output/input_output.gif"></p>

For example to learn to classify handwritten digits.

<p align="center"><img src="vid_files/2_mnist/input_output_number/input_output_number.gif"></p>

To perform supervised learning Input and the desired output is a datapoint, and when you wish to perform supervised learning you must prepare sufficient data points in a dataset.

<p align="center"><img src="vid_files/2_mnist/dataset/dataset.gif"></p>


You then tweak the machine learning algorithm such that it can correctly predict the output, given the input.

<p align="center"><img src="vid_files/2_mnist/w3/w3.gif"></p>

It is kind of like a teacher explaining the correct answer, and the student is the machine that tries to tweak itself in order to give the correct output.

<p align="center"><img src="vid_files/2_mnist/classroom.png"></p>

## Explaining training and test set

Okay so if a student is infinitely clever, and the teacher provides enough training examples the student can learn anything. Same goes for machine learning; If a machine learning model is sufferably complex it can learn any pattern of the dataset and the error will go to zero! For This could for example be number of incorrectly classified digits:

<p align="center"><img src="vid_files/9_pol_example/train_error_graph/train_error_graph.gif"></p>


You would expect after you seeing the error going to zero of the dataset everything is good right?

Well No - because You cannot know if the algorithm has learned .. it could just have remembered the answers. You must test the machine from never before seen examples.

we therefore take the dataset and split it into a training set where the machine can do whatever, and when we think we are converged to an good machine, we test the machine on unseen data; the test-set!


<p align="center"><img src="vid_files/2_mnist/data_set_split/data_set_split.gif"></p>

Think of a student learning a topic. The student must go to a test, which consist of unseen material, in order to determine if the student has learned anything.

The same idea is applied to machine learning, It should be called exam set.

Our goal is to have low predection error on unseen data! Exam, so that's the golden measurement.

It turns out you can decompose this error into three terms; bias, variance and noise. The noise will never go away so let's just ignore this.

Let's start with an example first.

## Simpler example throwing rocks and introduce variable names
Okay say we are trying to use machine learning to predict an extremely easy target.. Just to output the number ten. Before we wanted to predict digits, now we just want to predict the number ten.

So that's the goal.


<p align="center"><img src="vid_files/3_bias_variance_decompose/intro/intro.gif"></p>

bias = consistent error
<p align="center"><img src="vid_files/3_bias_variance_decompose/thrower_bias/thrower_bias.gif"></p>

variance = the spread

<p align="center"><img src="vid_files/3_bias_variance_decompose/thrower_var/thrower_var.gif"></p>

So the error consists of some variance and some bias

<p align="center"><img src="vid_files/3_bias_variance_decompose/thrower_both/thrower_both.gif"></p>




## mathematics derivation
Okay so i wont derrive it but it is not too bad if you use the distance squared as a measurement. This can be expanded into this, which is the bias squared, variance and the irreduble error.


## Explaining bias and variance

<p align="center"><img src="vid_files/9_pol_example/over_under.png"></p>
Let me show you with a concrete example.

Underfit: high test error, high train error
Overfit: high test error, low train error
Som balance must exist..

<p align="center"><img src="vid_files/9_pol_example/math_example/math_example.gif"></p>
<p align="center"><img src="vid_files/9_pol_example/train_error_02/train_error_02.gif"></p>

<p align="center"><img src="vid_files/9_pol_example/train_error/train_error.gif"></p>


## introduce main example


## explanationpaper dumb clever example?
If the model is not sufciated enough, we don't have enough learnable parameter to learn the problem..


Sound weird we need to introduce some bias and variance to perform better.. but think of this way; of the model is too complex we will over-fit on the noise, outliers of the training data..

if the model is just right, not too much bias not too much variance it is able capture the important stuff wont catch the noise.

<p align="center"><img src="vid_files/9_pol_example/result.png"></p>

## Other examples to do this
Making a model dumber (less complex, lowering learnable parameters) is called regularization.

I showed you regularization with polynomials by dampepining higer polynomial terms.

As I said in the start, this concept applies to everthing.

Regulerstion on a nerual network could for example be "dropout" or optimziing via brain damage, where neruons are disconnected to reduce learnable parameters..

In a decition tree, you can prune the tree to make it less complex


## Outro

So there you have it! A mathematical relationship showing you why you need to find a good balance between underthinking and overthinkking. And how to make a better machine learnig model.


Help me produce more math/physics content by becoming my patreon supporter. Thank you very much for helping me producing this video.

You can also help out the channel by exporing NFT's of my science gifs.

<!-- https://askubuntu.com/questions/856460/using-a-digital-camera-canon-as-webcam

https://alexagv.github.io/Turn-any-camera-into-a-cross-platform-webcam/
sudo modprobe v4l2loopback exclusive_caps=1 max_buffers=2
gphoto2 --stdout --capture-movie | ffmpeg -i - -vcodec rawvideo -pix_fmt yuv420p -threads 0 -f v4l2 /dev/video2
 -->

<!-- https://towardsdatascience.com/mse-and-bias-variance-decomposition-77449dd2ff55 -->

<!-- http://rasbt.github.io/mlxtend/user_guide/evaluate/bias_variance_decomp/ -->
<!-- https://allenkunle.me/bias-variance-decomposition -->

<!-- https://people.eecs.berkeley.edu/~jrs/189s19/lec/12.pdf -->


Let's represent a dataset with this grey cube.


This is my contribituon to the Summer of math exposition 1.

2:21 - The green line is the the therotical value of the error of the test set.. it is higher than the error of the training set, and there exist some optimal balance theortical balance of the model complexity. It turns out model compleixty is related to bias and variance, but more importantly, the total error, the green line, can be decomposed into three things: bias, variance and noise-- we cant control the noise so ignore that.

4:03 - blue is the bias and blue is the variance. Controlling them leads to an optimal lowest error. But up until now i haven't really shown you what model complexity is and how it relates to bias and variance.. lets do that with another example

The results are in! We see for our datasetthe best underfit and overfit balance whas between polynmial 0 and 1. It was not able to capture the true seond degree polynmial but we also had a very very very smal datatst.

overfit means you have a low error of the test set, but high error on the test set. i mean look what happens if i fit the polymail example before with a 7 degree polynial - ZERO error on the test set.
underfit means you have a high error on the training set, but high error on the ttest set.

- - -
We team up with a doctor and he delivers som data points for us. off ocurse the poitns cannot be exactly on the true line, there are some noise and randomness.

but we got some data points out of it

so thats the average distance to these points.

This video was brought to you by very gernous patreons! Thank you. Help me out by joining in patreon or explore my science gifs - they are avalaible as NFT's

So above we are measuring the bias and the variance and the total error of the test set. we have found and optimal value of complexity here, where the error is lowest
