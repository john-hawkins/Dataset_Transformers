# ###############################################################
# FUNCTIONS FOR NORMALISING COLUMNS OF A PANDAS DATA FRAME
#
#
# ###############################################################

def create_normalization_config(df):
    std_vector = df.std()
    mean_vector = df.mean()
    min_vector = df.min()
    max_vector = df.max()
    return {'stds':std_vector, 'means':mean_vector, 'mins':min_vector, 'maxs':max_vector}

def standardize(df, config, excluded):
   rez = (df - config['means'])/config['stds']
   rez = rez.fillna(0)
   for index in excluded:
      rez[index] = df[index]
   return rez

def normalize(df, config, excluded):
   rez = (df - config['mins']) / (config['maxs']-config['mins'])
   rez = rez.fillna(0.5)
   for index in excluded:
      rez[index] = df[index]
   return rez


# ################################################################
# Alternative Normalisation Approach
# 
def min_max_normalisz(indf, cols_to_norm):
   rez = indf.copy()
   rez[cols_to_norm] = rez[cols_to_norm].apply(lambda x: (x - x.min()) / (x.max() - x.min()))



