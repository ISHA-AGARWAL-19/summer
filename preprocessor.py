import pandas as pd

def preprocess(df,region_df):
    df = df.merge(region_df, on='NOC', how='left')
    df.drop_duplicates(inplace=True)
    df = pd.concat([df, pd.get_dummies(df['Medal'])], axis=1)
    return df

def preprocess_s(df1, df2 , region):
    df= pd.concat([df1,df2])
    df = df.merge(region, on='NOC', how='left')
    df.drop_duplicates(inplace=True)
    df = pd.concat([df, pd.get_dummies(df['Medal'])], axis=1)
    return df

