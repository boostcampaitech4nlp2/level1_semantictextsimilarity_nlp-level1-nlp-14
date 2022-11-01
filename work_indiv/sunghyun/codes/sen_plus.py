import pandas as pd

if __name__ == '__main__':

    train_data = pd.read_csv('../../../../data/train.csv')
    reverse_data = train_data.copy(deep=True)
    reverse_data['sentence_1']=train_data['sentence_2']
    reverse_data['sentence_2']=train_data['sentence_1']
    full_data = pd.concat([train_data,reverse_data], axis=0).reset_index(drop=True)

    full_data.to_csv('../../../../data/ftrain.csv')
    