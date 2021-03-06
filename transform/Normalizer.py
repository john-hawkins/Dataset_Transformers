# ###################################################################################################
# FUNCTIONS FOR NORMALISING COLUMNS OF A PANDAS DATA FRAME
#
#
# ###################################################################################################
import yaml
import io

def create_normalization_config(df):
    std_vector = df.std()
    mean_vector = df.mean()
    min_vector = df.min()
    max_vector = df.max()
    return {'stds':std_vector, 'means':mean_vector, 'mins':min_vector, 'maxs':max_vector}


def create_padded_normalization_config(df, padding):
    std_vector = df.std()
    mean_vector = df.mean()
    min_vector = df.min()
    max_vector = df.max()
    spread_vector = max_vector - min_vector
    pad_vector = spread_vector * padding
    min_vector = min_vector - pad_vector
    max_vector = max_vector + pad_vector
    return {'stds':std_vector, 'means':mean_vector, 'mins':min_vector, 'maxs':max_vector}


def standardize(df, config, excluded):
   rez = (df - config['means'])/config['stds']
   rez = rez.fillna(0)
   for index in excluded:
      rez[index] = df[index]
   return rez

def normalize(df, config, excluded):
   features = df.columns
   rez = (df - config['mins']) / (config['maxs']-config['mins'])
   rez = rez.fillna(0.5)
   rez = rez.loc[:,features]
   for index in excluded:
      rez[index] = df[index]
   return rez


def normalize_padded(df, config, excluded, padded):
   rez = (df - config['mins']) / (config['maxs']-config['mins'])
   spread = (config['maxs']-config['mins'])
   pad = (df - config['mins'] + (spread*0.05) ) / (spread * 1.1)
   rez = rez.fillna(0.5)
   pad = pad.fillna(0.5)
   for index in excluded:
      rez[index] = df[index]
   for index in padded:
      rez[index] = pad[index]
   return rez

def de_normalize(df, config, excluded):
   rez = ( df * (config['maxs']-config['mins']) ) + config['mins']
   for index in excluded:
      rez[index] = df[index]
   return rez

def de_normalize_col(df, config, col):
   rez = df.copy()
   rez[col] = ( df[col] * (config['max']-config['min']) ) + config['min']
   return rez

def de_normalize_all(df, config):
   rez = df.copy()
   rez = ( df * (config['max']-config['min']) ) + config['min']
   return rez



# ###################################################################################################
#  READ AND WRITE THE CONFIG FILE 
#  THIS ALLOWS YOU TO APPLY THE TRANSFORMATION TO NEW DATA
# ###################################################################################################
def write_normalization_config( cfg, filepath ):
    # Write TO A YAML file
    with io.open(filepath, 'w', encoding='utf8') as outfile:
        yaml.dump(cfg, outfile, default_flow_style=False, allow_unicode=True)

def read_normalization_config( filepath ):
    with open(filepath, 'r') as stream:
        data_loaded = yaml.load(stream)
    return data_loaded

def write_field_config( cfg, target_column_name, filepath ) :
    data = {'mean':float(cfg['means'][target_column_name]), 
            'min':float(cfg['mins'][target_column_name]),
            'max':float(cfg['maxs'][target_column_name]),
            'std':float(cfg['stds'][target_column_name]) }    
    with io.open(filepath, 'w', encoding='utf8') as outfile:
        yaml.dump(data, outfile) #, default_flow_style=False, allow_unicode=True)

