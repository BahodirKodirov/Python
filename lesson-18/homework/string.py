Homework 2:

df = pd.read_csv('task\\stackoverflow_qa.csv')
df.head()
id	creationdate	score	viewcount	title	answercount	commentcount	favoritecount	quest_name	quest_rep	ans_name	ans_rep
332289	2008-12-01 21:24:44	3184	5962784	How do I change the size of figures drawn with...	14	1	0.0	tatwright	37837.0	NaN	NaN
2051744	2010-01-12 19:31:47	420	587728	How to invert the x or y axis	10	3	0.0	DarkAnt	4211.0	Demitri	13369.0
2225995	2010-02-09 00:51:38	51	59922	How can I create stacked line graph?	4	0	0.0	David Underhill	15936.0	doug	69290.0
5486226	2011-03-30 12:26:50	7	6393	Rolling median in python	5	4	0.0	yueerhu	175.0	Mike Pennington	42288.0
5515021	2011-04-01 14:50:44	10	13744	Compute a compounded return series in Python	3	6	0.0	Jason Strimpel	14916.0	Mike Pennington	42288.0
Find all questions that were created before 2014
Find all questions with a score more than 50
Find all questions with a score between 50 and 100
Find all questions answered by Scott Boston
Find all questions answered by the following 5 users
Find all questions that were created between March, 2014 and October 2014 that were answered by Unutbu and have score less than 5.
Find all questions that have score between 5 and 10 or have a view count of greater than 10,000
Find all questions that are not answered by Scott Boston
Homework 3:

Titanic data set, stored as CSV. The data consists of the following data columns:

PassengerId: Id of every passenger.
Survived: Indication whether passenger survived. 0 for yes and 1 for no.
Pclass: One out of the 3 ticket classes: Class 1, Class 2 and Class 3.
Name: Name of passenger.
Sex: Gender of passenger.
Age: Age of passenger in years.
SibSp: Number of siblings or spouses aboard.
Parch: Number of parents or children aboard.
Ticket: Ticket number of passenger.
Fare: Indicating the fare.
Cabin: Cabin number of passenger.
Embarked: Port of embarkation.
titanic_df = pd.read_csv("task\\titanic.csv")
titanic_df.head()
PassengerId	Survived	Pclass	Name	Sex	Age	SibSp	Parch	Ticket	Fare	Cabin	Embarked
1	0	3	Braund, Mr. Owen Harris	male	22.0	1	0	A/5 21171	7.2500	NaN	S
2	1	1	Cumings, Mrs. John Bradley (Florence Briggs Th.)	female	38.0	1	0	PC 17599	71.2833	C85	C
3	1	3	Heikkinen, Miss. Laina	female	26.0	0	0	STON/O2. 3101282	7.9250	NaN	S
4	1	1	Futrelle, Mrs. Jacques Heath (Lily May Peel)	female	35.0	1	0	113803	53.1000	C123	S
5	0	3	Allen, Mr. William Henry	male	35.0	0	0	373450	8.0500	NaN	S
Select Female Passengers in Class 1 with Ages between 20 and 30: Extract a DataFrame containing female passengers in Class 1 with ages between 20 and 30.

Filter Passengers Who Paid More than $100: Create a DataFrame with passengers who paid a fare greater than $100.

Select Passengers Who Survived and Were Alone: Filter passengers who survived and were traveling alone (no siblings, spouses, parents, or children).

Filter Passengers Embarked from 'C' and Paid More Than $50: Create a DataFrame with passengers who embarked from 'C' and paid more than $50.

Select Passengers with Siblings or Spouses and Parents or Children: Extract passengers who had both siblings or spouses aboard and parents or children aboard.

Filter Passengers Aged 15 or Younger Who Didn't Survive: Create a DataFrame with passengers aged 15 or younger who did not survive.

Select Passengers with Cabins and Fare Greater Than $200: Extract passengers with known cabin numbers and a fare greater than $200.

Filter Passengers with Odd-Numbered Passenger IDs: Create a DataFrame with passengers whose PassengerId is an odd number.

Select Passengers with Unique Ticket Numbers: Extract a DataFrame with passengers having unique ticket numbers.

Filter Passengers with 'Miss' in Their Name and Were in Class 1: Create a DataFrame with female passengers having 'Miss' in their name and were in Class 1.


import pandas as pd

# Load the CSV into a DataFrame
df = pd.read_csv('task\\stackoverflow_qa.csv')

# Convert the 'creationdate' column to datetime format for easier manipulation
df['creationdate'] = pd.to_datetime(df['creationdate'])

# 1. Find all questions that were created before 2014
questions_before_2014 = df[df['creationdate'] < '2014-01-01']
print("Questions created before 2014:")
print(questions_before_2014)

# 2. Find all questions with a score more than 50
questions_score_more_than_50 = df[df['score'] > 50]
print("\nQuestions with a score greater than 50:")
print(questions_score_more_than_50)

# 3. Find all questions with a score between 50 and 100
questions_score_50_to_100 = df[(df['score'] > 50) & (df['score'] <= 100)]
print("\nQuestions with a score between 50 and 100:")
print(questions_score_50_to_100)

# 4. Find all questions answered by Scott Boston
questions_by_scott_boston = df[df['ans_name'] == 'Scott Boston']
print("\nQuestions answered by Scott Boston:")
print(questions_by_scott_boston)

# 5. Find all questions answered by the following 5 users
users = ['Scott Boston', 'Tatwright', 'Jason Strimpel', 'Mike Pennington', 'David Underhill']
questions_by_users = df[df['ans_name'].isin(users)]
print("\nQuestions answered by specific users:")
print(questions_by_users)

# 6. Find all questions that were created between March, 2014 and October 2014, answered by Unutbu, and have score less than 5
questions_march_to_oct_2014 = df[
    (df['creationdate'] >= '2014-03-01') & 
    (df['creationdate'] <= '2014-10-31') & 
    (df['ans_name'] == 'Unutbu') & 
    (df['score'] < 5)
]
print("\nQuestions created between March 2014 and October 2014, answered by Unutbu with score < 5:")
print(questions_march_to_oct_2014)

# 7. Find all questions that have score between 5 and 10 or have a view count of greater than 10,000
questions_score_between_5_and_10_or_viewcount_gt_10000 = df[
    ((df['score'] >= 5) & (df['score'] <= 10)) | (df['viewcount'] > 10000)
]
print("\nQuestions with score between 5 and 10 or view count > 10,000:")
print(questions_score_between_5_and_10_or_viewcount_gt_10000)

# 8. Find all questions that are not answered by Scott Boston
questions_not_answered_by_scott_boston = df[df['ans_name'] != 'Scott Boston']
print("\nQuestions not answered by Scott Boston:")
print(questions_not_answered_by_scott_boston)


import pandas as pd

# Load the Titanic CSV into a DataFrame
titanic_df = pd.read_csv("task\\titanic.csv")

# 1. Select Female Passengers in Class 1 with Ages between 20 and 30
female_class_1_ages_20_30 = titanic_df[
    (titanic_df['Sex'] == 'female') & 
    (titanic_df['Pclass'] == 1) & 
    (titanic_df['Age'] >= 20) & 
    (titanic_df['Age'] <= 30)
]
print("Female passengers in Class 1 with ages between 20 and 30:")
print(female_class_1_ages_20_30)

# 2. Filter Passengers Who Paid More than $100
paid_more_than_100 = titanic_df[titanic_df['Fare'] > 100]
print("\nPassengers who paid more than $100:")
print(paid_more_than_100)

# 3. Select Passengers Who Survived and Were Alone
survived_and_alone = titanic_df[
    (titanic_df['Survived'] == 1) & 
    (titanic_df['SibSp'] == 0) & 
    (titanic_df['Parch'] == 0)
]
print("\nPassengers who survived and were alone:")
print(survived_and_alone)

# 4. Filter Passengers Embarked from 'C' and Paid More Than $50
embarked_from_C_paid_more_than_50 = titanic_df[
    (titanic_df['Embarked'] == 'C') & 
    (titanic_df['Fare'] > 50)
]
print("\nPassengers who embarked from 'C' and paid more than $50:")
print(embarked_from_C_paid_more_than_50)

# 5. Select Passengers with Siblings or Spouses and Parents or Children
siblings_spouses_parents_children = titanic_df[
    (titanic_df['SibSp'] > 0) & 
    (titanic_df['Parch'] > 0)
]
print("\nPassengers with both siblings or spouses and parents or children aboard:")
print(siblings_spouses_parents_children)

# 6. Filter Passengers Aged 15 or Younger Who Didn't Survive
aged_15_or_younger_not_survived = titanic_df[
    (titanic_df['Age'] <= 15) & 
    (titanic_df['Survived'] == 0)
]
print("\nPassengers aged 15 or younger who didn't survive:")
print(aged_15_or_younger_not_survived)

# 7. Select Passengers with Cabins and Fare Greater Than $200
with_cabin_and_fare_gt_200 = titanic_df[
    (titanic_df['Cabin'].notnull()) & 
    (titanic_df['Fare'] > 200)
]
print("\nPassengers with cabins and fare greater than $200:")
print(with_cabin_and_fare_gt_200)

# 8. Filter Passengers with Odd-Numbered Passenger IDs
odd_passenger_ids = titanic_df[titanic_df['PassengerId'] % 2 != 0]
print("\nPassengers with odd-numbered PassengerId:")
print(odd_passenger_ids)

# 9. Select Passengers with Unique Ticket Numbers
unique_ticket_numbers = titanic_df[titanic_df['Ticket'].duplicated(keep=False) == False]
print("\nPassengers with unique ticket numbers:")
print(unique_ticket_numbers)

# 10. Filter Passengers with 'Miss' in Their Name and Were in Class 1
miss_class_1 = titanic_df[
    (titanic_df['Name'].str.contains('Miss')) & 
    (titanic_df['Pclass'] == 1)
]
print("\nFemale passengers with 'Miss' in their name and were in Class 1:")
print(miss_class_1)

