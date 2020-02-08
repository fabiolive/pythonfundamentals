#%%
print('Esse é o print')


#%%
'''Esse é um comentário'''


#%%
import pandas as pd


#%%
df = pd.read_csv('/home/developer/pythonfundamentals/Aulas/dados/campeonato-brasileiro-full.csv',encoding='utf-8', sep=',',usecols=['Data','Clube 1','Clube 2','Vencedor'],nrows=15)


#%%
df


#%%
df = pd.read_csv('/home/developer/pythonfundamentals/Aulas/dados/campeonato-brasileiro-full.csv')


#%%
df.shape # .SHAPE QUANTAS LINHA / COLUNAS


#%%
df.head(100) # QUANTIDADE DE LINHAS DEFINIDA


#%%
df2 = df


#%%
df2.drop([0,15]) #remove linhas pelo index


#%%
df2.drop('Horário', axis=1)


#%%
df2.index


#%%
df2.count()


#%%
df['Quantidade de Gols'] = df['Clube 1 Gols'] + df['Clube 2 Gols']


#%%
df


#%%
df.apply(lambda x: x.replace('Palmeiras', 'Palmeiras -SP'))


#%%



