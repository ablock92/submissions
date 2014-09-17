##Project Description
A movie studio has approached me with the goal of predicting the success of sequels. They own the rights to many different franchises and want to be able to analyze their current and future movie portfolio to help them more effectively choose whether or not to proceed with a sequel.

**Note:** For purposes of this project, we will judge the 'success' of a movie to be the box office gross of the movie.

##Exploratory Data Analysis:
I began by plotting a histogram of the box office numbers for both the previous movies and the sequels.

![](./img/BoxOffice_hist.png)

The two plots have relatively similar shapes to their distribution. This most likely suggests a correlation that we will explore later on.

##Linear Regression Models

The current best performing model contains the following attributes:

1. Box Office of previous movie
2. Percentage of Top 10 billed actors for previous movie that appear in sequel
3. The number of the movie in the series
4. The budget of the movie
  * This can be included because typically a studio will have a projected budget in mind when choosing whether or not to make a sequel

The plot of actual values and values predicted by the model is below:

![](./img/Regression_all_factors.png)

**Residual Analysis**
This led to a few interesting points that need to be studied further

1. There is far less variance in the residuals for movies that had a lower box office showing
2. The model generally overpredicted for movies with a low box office and underpredicted for movies with a large box office.
 * For some of the high box office movies, the model was off by almost $600,000,000!
 
 The residual plot is below:
 
 ![](./img/Residual_plot.png)
