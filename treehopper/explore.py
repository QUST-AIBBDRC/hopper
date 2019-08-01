import scanpy as sc
import numpy as np
from collections import Counter


def compress(adata, hopper, vc_name = 'vcell', wt_name='wt'):
    '''given voronoi cells, make weighted dataset'''

    vcells = hopper.vcells
    path = hopper.path

    #add voronoi info to original data
    adata.obs[vc_name] = vcells

    #compute counts in each cell
    counter = Counter(vcells)
    wts = [counter[x] for x in path]

    result = adata[path,:]
    result.obs[wt_name] = wts

    return(result)


def expand(smalldata, fulldata, vc_name = 'vcell'):
    '''given a small dataset with compression info, expand to full points'''

    smallcells = list(smalldata.obs[vc_name])
    fullcells = list(fulldata.obs[vc_name])
    print(smallcells)
    print(fullcells)

    idx = np.where([x in smallcells for x in fullcells])[0]
    result = fulldata[idx,:]

    return(result)

def filter(adata, obs_key, obs_values):
    obs_vals = list(adata.obs[obs_key])

    idx = np.where([x in obs_values for x in obs_vals])[0]

    return(adata[idx,:])
