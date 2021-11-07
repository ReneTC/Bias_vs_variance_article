# The Bias-Variance tradeoff - why being too smart is dumb.
So maybe the title is a little clickbaity, I'm sorry - but the concept is important if you ever want to do something useful in machine learning.

## Supervised learning
Right so I said it was important in machine learning, so let's just discuss machine learning for one second before moving on with the bias versus variance trade-off.

When doing supervised learning the idea is to learn to take some input, and predict the correct output.

<p align="center"><img src="src/2_mnist/input_output.gif"></p>

One example of this task is to take a handwritten image of a number and then get the machine to recognize what number it is.

<p align="center"><img src="src/2_mnist/input_output_number.gif"></p>

You must prepare sufficient data examples for the computer to learn. One data point (represented below with a gray cube) is the input and the output. The dataset must contains multiple examples of this, for a good machine learning model.

<p align="center"><img src="src/2_mnist/dataset/dataset149.png"></p>

So you're giving the computer the thing to learn and the answer.

You then train the model by continuously feeding the machine learning these data points and just keep on tweaking the parameters in the machine learning model until it can correctly take an image and classify it correctly.

<p align="center"><img src="src/2_mnist/feed_dataset.gif"></p>

This is kind of like a teacher to student scenario where the teacher is providing examples and the corresponding correct answer.

<p align="center"><img src="src/class.png"></p>

After we are done tweaking the machine, we take the data points and measure how good it is. In other words, we measure how often the model correctly classify an image - it turns out, if you have given enough data examples and the model is sufficiently complex the error will go to absolutely zero.

<p align="center"><img src="src/9_pol_example/train_error_graph_theory.gif"></p>

This mean, the model will never classify an image wrong! This seems all well and good, right?  The error is zero, so we should be done, right? .. Well no .. It's not good actually, we have used the same training examples for training and testing and that's kind of like student going to an exam where the students are already seen the question and the answers.

So the machine learning model could have just remembered the answers and not learned anything at all.

Therefore, we must go back, and the take the data set and then we split it up.

<p align="center"><img src="src/2_mnist/data_set_split.gif"></p>

We only use one set the "training set" for training the algorithm and then we use the other set for testing it, the so-called "test-set" - it should be called an exam set!

This test-set we will check how well it performs once we are done training the model. So this error on the unseen test-set is the golden measurement for checking our machine learning model. And it turns, if we adjust the complexity this time, the error on the test set will suddenly increase again after dropping. It looks like this:

<p align="center"><img src="src/9_pol_example/train_error_graph_theory.gif"></p>

You can see there exists some optimal balance between model complexity and low error on the test set. It turns out model complexity is related to bias and variance. We will see that soon too! It is related to the bias and variance.

## Bias and variance decomposition
The error can be decomposed into three things the bias the variance and the noise.

$$ \text{Error} = \text{Bias}(\hat{y})^2 + \text{Var}(\hat{y}) + \text{Noise}$$

But we can't get rid of the noise so let's ignore that.

Let's see why  can you decompose the error into bias and variance let me give you an example

Let's make an algorithm which goal is just to learn to output the number 10 yeah right so that's really really easy. The number 10 is the called the target function $y$


<p align="center"><img src="src/3_bias_variance_decompose/intro.gif"></p>

Now comes in one try of estimating $y$ and that's called $ \hat{y} $.
It turns out this current estimate is that it is always systematically of off the target and that's called the bias.

$$\operatorname{Bias}(\hat{y})=y-E[\hat{y}]$$

It is the true value minus the expectation value and it measures how often we are consistently wrong right so that was one bad estimation of hitting the number 10.

Now comes in another approximation and this approximations guesses is spread everywhere around the target and this is of course the variance!

<p align="center"><img src="src/3_bias_variance_decompose/thrower_var/thrower_var069.png"></p>

this is the equation for the variance:
$$
\operatorname{Var}(\hat{y})=E\left[(E[\hat{y}]-\hat{y})^{2}\right]
$$

it doesn't take into account the actual answer it just measures how spread out the data points are relative to each other.

So that was the two examples where one exam was really biased and one example was highly variant and so an actual attempt would consist of both errors so there will be some spread in the position and there will be some bias.

<p align="center"><img src="src/3_bias_variance_decompose/thrower_both.gif"></p>

When you make a machine learning model you must try to balance how much bias you have and how much variance you have and somewhere in between there is an optimal balance.

Blue is the bias and purple is the variance. Adjusting each other leads to an optimal balance and up to the lowest error.

<p align="center"><img src="src/9_pol_example/train_error_graph_theory_val_vb.gif"></p>

But up until now i haven't shown you what model complexity is and how it relates to bias and variance let's do that with yet another example.

## Complexity trade-off

To show you the complexity trade-off with an example, imagine that we are  trying to learn hours in the sun and the corresponding cell damage on the skin with machine learning. Imagine below the true function we would like to find looks like this:

<p align="center"><img src="src/9_pol_example/draw_true_fuction.gif"></p>

Off course this is a dream scenario to know a true function we are trying to find - in reality we never know this. Let's pretend it is a second degree polynomial with these values.

$$ f(x) = 0.2 x^2 + 1.5x + 1$$

Where $f(x)$ is cell damage and $x$ is hours in the sun. Let's use machine learning to learn/estimate this function. We team up with a doctor that measures some patients and get these data points.

The data points can be exactly on the true line because of noise and randomness. But at least we got some data points.

<p align="center"><img src="src/9_pol_example/draw_data_points/draw_data_points000.png"></p>

So this is our data set as I said earlier we'll split the data set into a training set and a test set.

<p align="center"><img src="src/9_pol_example/draw_data_points/draw_data_points069.png"></p>

So now I'll try to fit this with two different polynomials first a zero degree polynomial $f(x) = a_0$ so just a number. Let's mark the fit with blue. I'll also fit a  5th degree polynomial $f(x) =  a_5 x^5 + a_4 x^4 + a_3 x^3 + a_2 x^2 + a_1 x + a_0$ marked as purple. This is the result.

<p align="center"><img src="src/9_pol_example/fitting_2_poly.gif"></p>

Let's have a look on the bias and variance of these different fits, with respect of the test set (green points).

<p align="center"><img src="src/9_pol_example/over_under3.png"></p>

It turns out the 0th degree polynomial is highly highly biased. and this means that this machine learning model has underfit it was not able to capture the patterns in the data. And the fifth degree polynomial was highly highly variant it fitted too well on the noise the data, therefore the prediction are highly spread. The model is over-fit.

So somewhere between a 0 degree fit, and a 5'fth degree fit mut be a better function to generalize. Below i will interpolate from 0 to 5 degree polynomial and fit:

<p align="center"><img src="src/9_pol_example/train_error_02.gif"></p>

Let's see the Variance, Bias and total error for all these fits:

<p align="center"><img src="src/9_pol_example/yes.png"></p>

It turns out the best model to generalize was with a complexity around 0.5. You can see where Bias and variance meet, the total error is lowest. The model did not find the true function, $ f(x) = 0.2 x^2 + 1.5x + 1$, but our test and train sample is also very low.

You can see we must control the bias and the variance in order to make a good machine learning model, which corresponds to adjusting the complexity of a model. Adjust the complexity also adjusts the models tendency to overfit vs underfit. Overfit means you have a low error on the training set but a high error on the test set. Underfit means you have a high error on the training set and a high error on the test set as well.

# Other examples

It sounds weird we'll need to control or maybe even introduce some bias or some variance in order to get a low generalization error.

If the model is not sophisticated enough it doesn't have high enough complexity / enough learnable parameters, and the model will underfit.

If the model is too clever too complex it has too many learnable parameters it's going to see all the noise in the data set and it will find the wrong patterns, i.e overfit.

Somewhere in between overfit and underfit here is some good balance between being too dumb and too smart.

Making a model dumber is called regularization and i showed you that by reducing the polynomial degrees in a polynomial fit.

When using regularization in a neural network it's called dropout or optimizing via brain damage where we just simply remove connections between neurons to make it dumber.

<p align="center"><img src="src/0_draw/nerual.png"></p>

You can also regularize a decision tree by pruning the connections.


<p align="center"><img src="src/0_draw/tree.png"></p>

There you have it a mathematical relationship showing you why it is a good idea to find a balance between under-thinking and overthinking! And now you can make a better machine learning model.

Help me produce more science content by becoming my patreon or explore my science gifs that are aviable as NFT's. Thank you!
