def arrays(arr):
    import numpy as np
    arr.reverse()
    aj = list(map(float,arr))
    res = np.array(aj)
    return(res)