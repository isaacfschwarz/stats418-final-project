# Data

This directory contains the raw data files used for training the model. The data is in its original, uncleaned form as obtained from the ClinicalTrials.gov API.

## Files

### `adverse_events_10k.csv`
Raw adverse events data for 10,000 clinical trials from the ClinicalTrials.gov database. This file contains:
- Summary information about adverse events reported during clinical trials
- Each record corresponds to adverse event information for a specific clinical trial

### `clinical_trial_summary_10k.csv`
Raw clinical trial summary data for 10,000 clinical trials from the ClinicalTrials.gov database. This file contains:
- General summary information about clinical trials
- Each record corresponds to a specific clinical trial in the database

## Data Integration

The final dataset used for model training was created by joining these two files using the `NCT_ID` column as the primary key. The `NCT_ID` serves as the unique identifier that links adverse event information to the corresponding clinical trial details.

## Data Source

All data was obtained from the ClinicalTrials.gov API, which provides public access to information about clinical studies conducted around the world.

## Note

This is raw, unprocessed data. Data cleaning, preprocessing, and feature engineering steps were performed separately before model training. Refer to the project notebooks or documentation for details on data preparation procedures.
