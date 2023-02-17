# Model for Predicting Brownlow Medal Winner using Linear Regression
**Author: `Lang (Ron) Chen` 2021.12-2022.1**


**Report**
Methods and outcomes can be found in `Report for Predicting Brownlow Medal Winner using Linear Regression.pdf`

**Abstract**
The Brownlow Medal is the AFL’s highest individual honour award. After each game the adjudicating
umpire would award 3 votes, 2 votes and 1 vote to the top three performing players in their opinion,
and the highest polling player of the whole season would be declared winner.
As the performance of AFL players are generally considered well represented by game statistics, the
idea of training a Predictor with the goal of predicting the winner of the Brownlow Medal based on
the data of all games that season came into existence.
There were four motivations for this project:
1. As an AFL enthusiast, the author hoped to train a Predictor which could to the best degree predict the Brownlow Medallist of 2022 and beyond.
2. Put the predictor training skills and theoretical knowledge learnt at University to test on a real world scenario.
3. Investigate how different choices made during predictor training (including some new innovative variations to traditional models) would affect performance statistically and empirically, so to aid future study and projects.
4. The Australian sports-betting industry is lucrative and the statistical/data science aspects of it is exciting; it is hoped a successful outcome could open the door to this industry for the author

The project was successful, and the resulting predictors can be found in M1.ipynb, M2.ipynb and
M3.ipynb and the 


**Table of Contents**
- `BrownlowMedalTools` directories contains self-written functions used in .ipynb
- `Data` directory contains raw and manipulated data
- `Experiment Results` directory contain experiment ipynbs and scripts
- `Models` directory contains final models and PREDICTOR.ipynb which allows for prediction
- `# series ipynb` are scripts that crawl and manipulate data during the initial stages of the project
- `PoC series ipynb` are Proof of Concepts for several models
- `Scripts series ipynb` are scripts used for mass training of data
- `M series ipynb` are scripts for training the final model
- `Report pdf` is the full report of this project
- `Prepared Data` directory contains KFold Train-Test splitted data for scripts [Could not be uploaded due to size. Reproduce from `6_.ipynb`]


*Note: some the file system has been restructured, so may need to re-create folders/move around files before running a script.*


**BIBLIOGRAPHY**

Data Source

- AFLTables.com. 2022. Brownlow Votes Round by Round. [online] Available at: <https://afltables.com/afl/brownlow/brownlow_idx.html> [Accessed 26 January 2022].

- Footywire.com. 2022. AFL Fixture. [online] Available at: <https://www.footywire.com/afl/footy/ft_match_list> [Accessed 26 January 2022].
