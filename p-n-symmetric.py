import time
import numpy as np
import ssgetpy
from scipy.io import mmread
id = int(input('id='))
matrix = ssgetpy.search(id)[0]
file_path = matrix.download(extract=True)[0] + "/" + matrix.name + ".mtx"
mtx = mmread(file_path)
a = mtx.toarray()
print(id, a.shape)


def naiv(a):
    start = time.time()
    len_a = int(a.size ** 0.5 + 0.2)
    p_sym, n_sym, nzoffdiag = 0, 0, 0
    for i in range(len_a):
        for j in range(i + 1, len_a):
            if a[i][j] != 0 and a[j][i] != 0 and a[i][j] == a[j][i]:
                p_sym += 2
                n_sym += 2
                nzoffdiag += 2
            elif a[i][j] != 0 and a[j][i] != 0:
                p_sym += 2
                nzoffdiag += 2
            elif a[i][j] != 0 or a[j][i] != 0:
                nzoffdiag += 1
    if nzoffdiag == 0:
        p_sym, n_sym = 1, 1
    else:
        p_sym /= nzoffdiag
        n_sym /= nzoffdiag
    end = time.time()
    return p_sym, n_sym, end - start


def numpe_alg(a):
    start = time.time()
    np.fill_diagonal(a, 0)
    nzoffdiag = np.count_nonzero(a)
    a_trans = a.transpose()
    p_sym = np.count_nonzero(np.multiply(a, a_trans)) / nzoffdiag

    n_sym = np.count_nonzero(np.equal(a, a_trans))
    duo_zero = a.size - np.count_nonzero(np.absolute(a) + np.absolute(a_trans))
    n_sym = (n_sym - duo_zero) / nzoffdiag

    end = time.time()
    return p_sym, n_sym, end - start


print(*naiv(a))
print(*numpe_alg(a))

