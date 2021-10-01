# The Bias-Variance tradeoff - being too smart is dumb.
So maybe the title is a little bit clickbaity, I'm sorry but the concept is really important if you ever want to do something useful in machine learning.

## Supervised learning
Right so i said it was important in machine learning so let's just discuss machine learning for one second before moving on with the bias versus variance trade-off.

So when doing supervised learning the idea is to learn to take some input, and predict the correct output.

And one example of this is to take a handwritten image of a number and then get the machine to recognize what number it is - So learning to read numbers!

You must prepare sufficient data examples where one data point is an example of an input and the desired output.

So you're giving the computer the answers.

Let's represent a data set with a grey cube. You must prepare enough of those examples in the data set.

You then feed the machine learning these data points and just keep on tweaking the parameters in the machine learning model until it can correctly take an image and classify it correctly -kind of like a teacher to student scenario where the teacher is providing examples and the co responding correct answer.

So after we have done tweaking the machine we take the data points and measure how good it is - like how often do you correctly classify an image - it turns out if you have given enough data examples and the model is sufficiently complex the error will go to absolutely zero.

It will never classify an image wrong! This seems all well and good right?  The error is zero so we should be done right? .. well no .. it's not good actually, we have used the same training examples for training and testing and that's kind of like student going to an exam where the students are already seen the question and the answers.

So the machine learning model could have just remembered the answers and not learned anything at all.

Therefore we must go back and then we take this data set and then we split it up.

We only use one set the "training set" for training the algorithm and then we use the other set for testing it, the so-called "test-set" - it should be called an exam set!

This test-set we will check how well it performs once we are done training the model. So this error on the unseen test-set is the golden measurement for checking our machine learning model.

The theoretical value of the test set it is higher than the error of the training set. We will see why soon.

but there exists some optimal balance between model complexity and low error on the test set. It turns out model complexity is related to bias and variance. We will see that soon!

## Bias and variance decomposition
But first the error can be decomposed into three things the bias the variance and the noise but we can't get rid of the noise so let's ignore that why can you decompose the error into bias and variance let me give you an example

Let's make an algorithm which goal is just to learn to output the number 10 yeah right so that's really really easy. The number 10 is called the target function. So that's called y.

Now comes in one try of estimating y and that's called of course called y hat. So that's our estimate of the target function.  And it turns out this current estimate is that it is always kind of off the target and that's called the bias it is the true value minus the expectation value and it measures how often we are consistently wrong right so that was one bad estimation of hitting the number 10.

Now comes in another approximation and this approximations guesses is spread everywhere around the target and this is of course the variance! this is the equation for the variance it doesn't take into account the actual answer it just measures how spread out the data points are relative to each other.

So that was the two examples where one exam was really biased and one example was highly variant and so an actual attempt would consist of both errors so there will be some some spread in the position and there will be some bias.

When you make a machine learning model you must try to balance how much bias you have and how much variance you have and somewhere in between there is an optimal balance.

Blue is the bias and purple is the variance. Adjusting each other leads to an optimal balance and up to the lowest error but up until now i haven't shown you what model complexity is and how it relates to bias and variance let's do that with yet another example.

## Complexity trade-off

Okay here is an example that we could be trying to learn with machine learning say that this is an absolutely true function for hours in the sun and the corresponding cell damage on the skin.

Off course this is a dream scenario to know a true function like this - in reality we never know this relation, this black line here. Let's pretend it is a second degree polynomial with these values.

Let's use machine learning to learn/estimate this function. We team up with a doctor that measures some patients and get these data points. The data points can be exactly on the true line because of noise and randomness. But at least we got some data points.

So this is our data set as I said earlier we'll split the data set into a training set and a test set.

So now I'll try to fit this with two different polynomials first a zero degree polynomial so just a number and then a 5th degree polynomial and now it's time to measure how good we performed so we'll measure the error of the test set so that's the average distance to the test points it turns out the 0th degree polynomial is highly highly biased and this means that this machine learning model has underfit it was not able to capture the patterns and the 50 degree polynomial was highly highly variant it fitted too well on the noise the data is of course highly spread out like the variance is really really high the model is over fit it captured the noise in the data set we must control the bias and the variance so now we will try to vary the degree of the polynomial in order to vary the bias and the variance so you can also say that you model the complexity of the model the higher degree polynomials we have the more learnable parameters we have so this essentially what we're doing we are adjusting the complexity of the model in order to adjust the bias and variance by adjusting the complexity the polynomial degree so above I'm showing you the bias and the variance and the total error given by this equation turns out we have found an optimal value for the bias and variance right here that's the lowest error of the test set it wasn't able to find the correct second degree polynomial but we also had a very very small data set overfit means you have a low error on the training set but a high error on the test set underfit means you have a high error on the training set and a high error on the test set as well


## Weird example
it sounds so weird we'll need to control or maybe even introduce some fires or some variants in order to get a low generalization error if the model is not sophisticated enough it doesn't have enough complexity enough learnable parameters

seven

seven uh seven .. Ff the model is too clever too complex it has too many learnable parameters it's going to see all the noise in the data set and it will find the wrong patterns. hmm wait a minute this paper is slightly bent over here this is a clearly indication that the answer cannot be 4 this must be 5 perhaps somewhere in between there is some good balance between being too dumb and too smart. it's 10. making a model dumber is called regularization and i showed you that by reducing the polynomial degrees when using regularization in a neural network it's called dropout or optimizing via brain damage so we just simply remove connections between neurons to make it dumber you can also regularize a decision tree by pruning there you have it a mathematical relationship showing you why it is a good idea to find a balance between underthinking and overthinking and now you can make a better machine learning model this video was brought to you by very generous patrons thank you very much for the help help me produce more science content and become my patreon or check out my science gifts they are available as nfts
