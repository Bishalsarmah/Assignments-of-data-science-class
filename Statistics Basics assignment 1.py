#!/usr/bin/env python
# coding: utf-8

# ### Statistics Basics 1

# #### 1. What is statistics?

# #### Ans- The practice or science of collecting and analysing numerical data in large quantities, especially for the purpose of inferring proportions in a whole from those in a representative sample.

# #### 2. Define the different types of statistics and give an example of when each type might be used.

# #### Ans- There are two main types of statistics: descriptive statistics and inferential statistics.
# 
# #### 1)Descriptive Statistics: 
# Descriptive statistics is the branch of statistics that deals with the collection, presentation, and summarization of data. It includes measures of central tendency, measures of variability, and measures of shape. Descriptive statistics are used to describe and summarize a dataset, which can help researchers understand the characteristics of the data.
# #### Example:
# A researcher might use descriptive statistics to describe the average income of a population or the frequency distribution of a categorical variable such as gender or education level.
# 
# #### 2)Inferential Statistics: 
# Inferential statistics is the branch of statistics that deals with making inferences about a population based on a sample of data. Inferential statistics are used to test hypotheses and make predictions about the population.
# #### Example: 
# A researcher might use inferential statistics to test whether there is a significant difference in average income between two groups, such as men and women, or to determine whether a treatment is effective in improving health outcomes.

# #### 3.What are the different types of data and how do they differ from each other? Provide an example of
# #### each type of data.

# #### Ans-There are four main types of data: nominal, ordinal, interval, and ratio data.
# 
# #### Nominal Data: 
# Nominal data is data that is categorized or named without any order or ranking. It is the simplest form of data and is often used to represent categories or groups. Nominal data can be in the form of words, symbols, or numbers.
# #### Example:
# Examples of nominal data include gender (male or female), hair color (blonde, brunette, red), and eye color (blue, green, brown).
# 
# #### Ordinal Data: 
# Ordinal data is data that has a ranking or order to it. The categories or groups in ordinal data have a natural order, but the differences between the categories cannot be measured or compared.
# #### Example: 
# Examples of ordinal data include education level (high school, some college, bachelor's degree), income level (low, medium, high), and customer satisfaction ratings (poor, fair, good, excellent).
# 
# #### Interval Data: 
# Interval data is data that has a fixed unit of measurement and equal intervals between each data point. Unlike ordinal data, the differences between the categories in interval data can be measured and compared, but there is no true zero point.
# #### Example: 
# Examples of interval data include temperature (measured in degrees Fahrenheit or Celsius), time (measured in seconds, minutes, hours), and IQ scores.
# 
# #### Ratio Data: 
# Ratio data is data that has a fixed unit of measurement, equal intervals between each data point, and a true zero point. The zero point in ratio data means that there is a complete absence of the thing being measured.
# #### Example: 
# Examples of ratio data include height (measured in inches or centimeters), weight (measured in pounds or kilograms), and income (measured in dollars).
# 
# #### In summary, nominal data is unordered categorical data, ordinal data has a natural order or ranking, interval data has equal intervals between data points but no true zero point, and ratio data has equal intervals between data points and a true zero point.

# #### 4.Categorise the following datasets with respect to quantitative and qualitative data types:
# #### (i) Grading in exam: A+, A, B+, B, C+, C, D, E
# #### (ii) Colour of mangoes: yellow, green, orange, red
# #### (iii) Height data of a class: [178.9, 179, 179.5, 176, 177.2, 178.3, 175.8,...]
# #### (iv) Number of mangoes exported by a farm: [500, 600, 478, 672, ...]

# #### 4.Ans-
# (i) Grading in exam: This is a categorical variable, hence it is qualitative data.
# 
# (ii) Colour of mangoes: This is also a categorical variable, hence it is qualitative data.
# 
# (iii) Height data of a class: This is a continuous variable, hence it is quantitative data.
# 
# (iv) Number of mangoes exported by a farm: This is a discrete variable, hence it is quantitative data.

# #### 5.Explain the concept of levels of measurement and give an example of a variable for each level.

# #### 5.ans-
# The levels of measurement, also known as scales of measurement, are a way of categorizing variables based on the type of data they produce and the statistical analysis methods that are appropriate for each level. There are four levels of measurement: nominal, ordinal, interval, and ratio.
# 
# #### Nominal Level of Measurement: 
# Nominal level variables are used to categorize data into distinct groups or categories. Nominal variables have no inherent order or numerical value associated with them. Nominal level data can be represented using labels, words, or numbers. Some common examples of nominal level variables include:
# 
# Gender: Male, Female
# 
# Race/Ethnicity: Caucasian, African American, Hispanic, Asian
# 
# Marital Status: Married, Single, Divorced, Widowed
# 
# #### Ordinal Level of Measurement:
# Ordinal level variables have a natural order or ranking, but the differences between each value are not equal or cannot be measured. Ordinal data can be represented using numbers or words. Some common examples of ordinal level variables include:
# 
# Educational attainment: High School, Some College, Bachelor's Degree, Master's Degree, Doctorate
# 
# Income: Low, Medium, High
# 
# Satisfaction Ratings: Poor, Fair, Good, Excellent
# 
# #### Interval Level of Measurement: 
# Interval level variables have equal intervals between values, but they do not have a true zero point. This means that the absence of a value does not necessarily indicate a complete absence of the thing being measured. Interval data can be represented using numerical values. Some common examples of interval level variables include:
# 
# Temperature: Celsius or Fahrenheit
# 
# Time: Hours, Minutes, Seconds
# 
# IQ Scores: 80, 90, 100, 110, 120, etc.
# 
# #### Ratio Level of Measurement:
# Ratio level variables have equal intervals between values and a true zero point. This means that a value of zero indicates a complete absence of the thing being measured. Ratio data can be represented using numerical values. Some common examples of ratio level variables include:
# 
# Height: Inches or centimeters
# 
# Weight: Pounds or kilograms
# 
# Distance: Meters or miles

# #### 6.Why is it important to understand the level of measurement when analyzing data? Provide an
# #### example to illustrate your answer. 

# #### 6.Ans- It is important to understand the level of measurement when analyzing data because different statistical analyses are appropriate for different levels of measurement. Using an inappropriate statistical test or analysis can lead to inaccurate or misleading results.
# 
# For example, suppose we want to compare the average income of two groups of people: those with a Bachelor's degree and those with a Master's degree. We collect data on the income of a sample of people in each group and use a t-test to compare the means. However, we fail to recognize that educational attainment is an ordinal variable, not an interval or ratio variable. In this case, using a t-test would be inappropriate because it assumes that the intervals between values are equal, which is not the case with ordinal data.
# 
# A better approach in this situation would be to use a non-parametric test, such as the Mann-Whitney U test, which is appropriate for ordinal data. By using the appropriate statistical test, we can be more confident in the accuracy and validity of our results.
# 
# In summary, understanding the level of measurement of variables is crucial when analyzing data because it determines the appropriate statistical analysis methods to be used. Using the wrong analysis method can lead to incorrect or misleading conclusions.

# #### 7.How nominal data type is different from ordinal data type.

# #### 7.Ans- Nominal data are used to categorize data into distinct groups or categories, where there is no inherent order or numerical value associated with them, while ordinal data have a natural order or ranking, but the differences between each value are not equal or cannot be measured.

# #### 8.Which type of plot can be used to display data in terms of range?

# #### Ans- Histogram

# #### 9.Describe the difference between descriptive and inferential statistics. Give an example of each
# #### type of statistics and explain how they are used.

# #### 9.Ans-
# Descriptive statistics and inferential statistics are two branches of statistics that are used to analyze and summarize data in different ways.
# 
# Descriptive statistics refer to the collection, analysis, and presentation of data in order to describe or summarize a set of observations. Descriptive statistics are used to describe the basic features of the data in question, such as measures of central tendency (mean, median, and mode), measures of dispersion (variance and standard deviation), and graphical displays such as histograms and scatter plots. Descriptive statistics are used in various fields, such as psychology, social sciences, and market research.
# 
# An example of descriptive statistics is the mean, median, and mode of a set of exam scores for a class of students. The mean gives an idea of the average performance of the class, while the median and mode give information about the central tendency of the scores.
# 
# On the other hand, inferential statistics are used to make inferences or draw conclusions about a population based on a sample of data. Inferential statistics involve the use of probability theory and hypothesis testing to determine the likelihood that the results observed in a sample could be generalized to the larger population. Inferential statistics are used to test hypotheses, compare groups, and make predictions about future events.
# 
# An example of inferential statistics is a hypothesis test to determine whether there is a significant difference in the exam scores of two different classes of students. By collecting and analyzing data from a sample of students from each class, inferential statistics can be used to determine whether the observed difference in scores is significant and can be generalized to the larger population.
# 
# In summary, descriptive statistics are used to describe and summarize data, while inferential statistics are used to make inferences and draw conclusions about a population based on a sample of data. Both descriptive and inferential statistics are important tools in data analysis and are used in various fields of study.

# #### 10. What are some common measures of central tendency and variability used in statistics? Explain
# #### how each measure can be used to describe a dataset.

# #### 10.Ans- Measures of central tendency and variability are important statistical tools used to summarize and describe data.
# 
# Measures of central tendency are used to describe the typical value or center of a distribution. There are three common measures of central tendency: mean, median, and mode.
# 
# #### Mean: 
# The mean is calculated by summing up all the values in a dataset and then dividing by the total number of values. It is the most commonly used measure of central tendency and is used to describe the average value of the dataset. It is sensitive to outliers, meaning that extreme values can have a significant impact on the mean.
# 
# #### Median:
# The median is the middle value in a dataset when it is ordered from lowest to highest. It is less sensitive to outliers than the mean and is used when the dataset is skewed or has extreme values.
# 
# #### Mode:
# The mode is the most frequent value in a dataset. It is used when a dataset has a large number of repeated values.
# 
# Measures of variability are used to describe the spread or dispersion of data around the central tendency. There are three common measures of variability: range, variance, and standard deviation.
# 
# #### Range:
# The range is the difference between the highest and lowest values in a dataset. It is a simple measure of variability but is highly affected by extreme values.
# 
# #### Variance:
# The variance is a measure of the spread of data around the mean. It is calculated by finding the average of the squared differences between each value and the mean. It is used when we need to understand how much the data deviates from the mean.
# 
# #### Standard deviation:
# The standard deviation is the square root of the variance. It is used to describe the spread of data around the mean and is a more commonly used measure of variability. It is preferred over variance as it is in the same units as the data.
# 
# In summary, measures of central tendency and variability are important tools for describing and summarizing data. The choice of measure depends on the distribution of the data and the research question. Mean and standard deviation are used when data is normally distributed, and median and range are used when data is skewed or has outliers.

# In[ ]:




