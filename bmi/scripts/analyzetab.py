import pandas as pd
import re
import glob
import matplotlib.pyplot as plt

test = {}
#From Gabi's Jupyter Notebook
def read_tab_file(filename):
    '''
    The output of the MTP shotgun pipeline includes a '.tab' file which lists the abundances and the taxonomies. 
    This method parses it to a dict
    '''
    out = {} # will be organized by level (kingdom / phylum / species etc)
    with open(filename, 'r') as f:
        for line in f:
            if line.startswith(">>>"):
                name = line.split(' ')[1]
                out[name] = {}
                #check if the line starts with a letter
            elif re.findall('^[a-zA-Z]+', line[0]):
                try:
                    taxon, cg_reads, abud, taxonomy = line.rstrip().split('\t')
                except ValueError:
                    #Kingdom line doesn't have a taxonomy list since it's the first
                    taxon, cg_reads, abud = line.rstrip().split('\t')
                    taxonomy = ''
                out[name][taxon] = [int(cg_reads), float(abud), taxonomy]
    return out

#From Gabi's Jupyter Notebook
def get_count_df(tabpath, taxonomy_info={}):
    samp_name = tabpath.split('/')[-1].split('.')[0]
    level_dict = read_tab_file(tabpath)
    species_dict = level_dict['Species']

    if not species_dict:
        print(f'No results for {samp_name}')
        return None, taxonomy_info

    species_df = pd.DataFrame.from_dict(species_dict, orient='index')
    species_df.columns = ['Core Gene Reads', 'Abundance', 'Taxonomy']

    #prep the individual cg and ab dfs for this sample to concat later
    cg_df = species_df[['Core Gene Reads']]
    #cg_df = species_df[['Abundance']]
    cg_df.columns = [samp_name]
    
    return cg_df

#From Gabi's Jupyter Notebook
def make_df(files):
    counts = []
    for file in files:
        count_df = get_count_df(file, {})
        counts.append(count_df)
    return pd.concat(counts, axis=1).fillna(0)

ovw_files = glob.glob('../ovw/*/*.tab')
nor_files = glob.glob('../nor/*/*.tab')

ovw_df = make_df(ovw_files)
nor_df = make_df(nor_files)
ovw_df = ovw_df.sum(axis=1)
nor_df = nor_df.sum(axis=1)
ovw_df = ovw_df.sort_values(ascending=False)
nor_df = nor_df.sort_values(ascending=False)

ovw_set = set(ovw_df.index)
nor_set = set(nor_df.index)
exc_ovw_set = ovw_set - nor_set
exc_nor_set = nor_set - ovw_set
exc_ovw_df = ovw_df[list(exc_ovw_set)] #passing uncasted set is deprecated
exc_nor_df = nor_df[list(exc_nor_set)]
exc_ovw_df = exc_ovw_df.sort_values(ascending=False)
exc_nor_df = exc_nor_df.sort_values(ascending=False)
