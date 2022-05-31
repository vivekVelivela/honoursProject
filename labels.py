# -*- coding: utf-8 -*-
# The below script is used to convert image string labels into binary format
import pandas as pd
import numpy as np
def main():
  df = pd.read_excel('path to the excel file with labels')

  column_1 = df.Genotype_1.unique()
  column_2 = df.Genotype_2.unique()
  column_3 = df.Genotype_3.unique()
  column_4 = df.UID.unique()

  d=np.concatenate((column_1, column_2,column_3), axis=None)

  new_df = pd.DataFrame(columns = d)
  new_df['UID'] = column_4
  new_df['UID_1'] = column_4
  new_df = new_df.set_index('UID')
  for ind in df.index:
    for ind1 in range(len(new_df.index)):
      if(df['UID'][ind] == new_df['UID_1'][ind1]):
        if(df['Genotype_1'][ind] in new_df.columns):
          out = np.argwhere(new_df.columns.isin([df['Genotype_1'][ind]])).ravel()
          new_df.loc[new_df['UID_1'][ind1],new_df.columns[out]] = 1
        if(df['Genotype_2'][ind] in new_df.columns):
          out = np.argwhere(new_df.columns.isin([df['Genotype_2'][ind]])).ravel()
          new_df.loc[new_df['UID_1'][ind1],new_df.columns[out]] = 1
        if(df['Genotype_3'][ind] in new_df.columns):
          out = np.argwhere(new_df.columns.isin([df['Genotype_3'][ind]])).ravel()
          new_df.loc[new_df['UID_1'][ind1],new_df.columns[out]] = 1

  new_df.to_excel('path to output the result')

if __name__ == '__main__':
  main()