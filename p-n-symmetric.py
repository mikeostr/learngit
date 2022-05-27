import time
import numpy as np
import ssgetpy
from scipy.io import mmread
id = int(input('id='))
matrix = ssgetpy.search(id)[0]
file_path = matrix.download(extract=True)[0] + "/" + matrix.name + ".mtx"
mtx = mmread(file_path)
print(id, mtx.shape)


def naiv(mtx):
    start = time.time()
    a = mtx.toarray()
    len_a = int(a.size ** 0.5 + 0.2)
    p_sym, n_sym, nzoffdiag = 0, 0, 0
    # error = (0, 0, 0)
    # count = 0
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
                # count += 1
                # print(i,'    ', j,'    ', a[i][j],'    ', a[j][i])
                # if max(abs(a[i][j]), abs(a[j][i])) > error[2]:
                #     error = (i, j, max(abs(a[i][j]), abs(a[j][i])))
                nzoffdiag += 1
    # print(error, count)
    # print(a[error[0]][error[1]], a[error[1]][error[0]])
    if nzoffdiag == 0:
        p_sym, n_sym = 1, 1
    else:
        p_sym /= nzoffdiag
        n_sym /= nzoffdiag
    end = time.time()
    return p_sym, n_sym, end - start


def numpe_alg(mtx):
    start = time.time()
    a = mtx.toarray()
    np.fill_diagonal(a, 0)
    nzoffdiag = np.count_nonzero(a)
    a_trans = a.transpose()
    p_sym = np.count_nonzero(np.multiply(a, a_trans)) / nzoffdiag

    n_sym = np.count_nonzero(np.equal(a, a_trans))
    duo_zero = a.size - np.count_nonzero(np.absolute(a) + np.absolute(a_trans))
    n_sym = (n_sym - duo_zero) / nzoffdiag

    end = time.time()
    return p_sym, n_sym, end - start


def scipy_alg(a):
    start = time.time()
    size = a.shape
    a.setdiag(0)
    nzoffdiag = a.count_nonzero()
    a_csr = a.tocsr()
    a_t_csr = a_csr.transpose()
    p_sym = a_csr.multiply(a_t_csr).count_nonzero() / nzoffdiag

    n_sym = size[0] * size[1] - (a_csr - a_t_csr).count_nonzero()
    double_zero = size[0] * size[1] - (a_csr.multiply(a_csr) + a_t_csr.multiply(a_t_csr)).count_nonzero()
    n_sym = (n_sym - double_zero) / nzoffdiag

    end = time.time()
    return p_sym, n_sym, end - start


print(*naiv(mtx))
print(*numpe_alg(mtx))
print(*scipy_alg(mtx))

