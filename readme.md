# Political Speech Word Counter

## About

This project started with the aim of trawling through lots of political speeches
and pulling out the top 10 words used by any given speaker or party. After I had
done that I expanded it to do some analysis on the top 10 lists. As a result the 
program now compares the top results of all archived speeches and returns 
information on the similarities and differences of words used. 

I have populated an SQLite database with archived political speeches. My program
processes these, finds the most common words in the speech and compares speeches
with one another. The comparison can either be made by political party or by
speaker. This means, for example, that you can see which two political parties
have the most top 10 words in common.

## Technologies used

- Python 3.8
- SQLite 3.11.2


## Results
Some of the results based on an analysis of the top 10 words in the archived
political speeches are below:

The parties with the most top 10 words in common are Labour / Liberal Democrat
with 7 out of 10 words in common

The parties with the least top 10 words in common are
Conservative / SDP-Liberal Alliance with 4 out of 10 words in common

The speakers with the most top 10 words in common are
Neil Kinnock / Ed Miliband with 9 out of 10 words in common

The speakers with the least top 10 words in common are
Earl of Rosebery / Winston Churchill with 0 out of 10 words in common
