import pandas as pd
from pathlib import Path

path = Path("database")

def show_result():
    df=pd.read_csv(path/'cand_list.csv')
    df=df[['Sign','Name','VoteCount']]
    v_cnt = {}
    for index, row in df.iterrows():
        v_cnt[df['Sign'].iloc[index]] = df['VoteCount'].iloc[index]
    
    return v_cnt

def verify(vid,passw):
    df=pd.read_csv(path/'voterList.csv')
    df=df[['voter_id','Passw','hasVoted']]
    for index, row in df.iterrows():
        if df['voter_id'].iloc[index]==vid and df['Passw'].iloc[index]==passw:
            return True
    return False

def isEligible(vid):
    df=pd.read_csv(path/'voterList.csv')
    df=df[['voter_id','Name','Gender','Zone','City','Passw','hasVoted']]
    for index, row in df.iterrows():
        if df['voter_id'].iloc[index]==vid and df['hasVoted'].iloc[index]==0:
            return True
    return False

def vote_update(st,vid):
    if isEligible(vid):
        df=pd.read_csv (path/'cand_list.csv')
        df=df[['Sign','Name','VoteCount']]
        for index, row in df.iterrows():
            if df['Sign'].iloc[index]==st:
                df['VoteCount'].iloc[index]+=1

        df.to_csv (path/'cand_list.csv')

        df=pd.read_csv(path/'voterList.csv')
        df=df[['voter_id','Name','Gender','Zone','City','Passw','hasVoted']]
        for index, row in df.iterrows():
            if df['voter_id'].iloc[index]==vid:
                df['hasVoted'].iloc[index]=1

        df.to_csv(path/'voterList.csv')

        return True
    return False

def taking_data_voter(name,gender,zone,city,passw):
    print('1')
    df=pd.read_csv(path/'voterList.csv')
    print('2')
    df=df[['voter_id','Name','Gender','Zone','City','Passw','hasVoted']]
    row,col=df.shape
    if row==0:
        vid = 10001
        df = pd.DataFrame({"voter_id":[vid],
                    "Name":[name],
                    "Gender":[gender],
                    "Zone":[zone],
                    "City":[city],
                    "Passw":[passw],
                    "hasVoted":[0]},)
    else:
        vid=df['voter_id'].iloc[-1]+1
        df1 = pd.DataFrame({"voter_id":[vid],
                    "Name":[name],
                    "Gender":[gender],
                    "Zone":[zone],
                    "City":[city],
                    "Passw":[passw],
                    "hasVoted":[0]},)

        df=df.append(df1,ignore_index=True)

    df.to_csv(path/'voterList.csv')

    return vid
