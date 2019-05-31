import sys
# sys.setrecursionlimit(200000)


def find_elem(tree, elem, root):
    if root is not None:
        if elem == tree[root][0]:
            answ = True, root
        else:
            if elem < tree[root][0]:
                if tree[root][2] is None:
                    answ = False, None
                else:
                    answ = find_elem(tree, elem, tree[root][2])
            else:
                if tree[root][3] is None:
                    answ = False, None
                else:
                    answ = find_elem(tree, elem, tree[root][3])
    else:
        answ = False, None
    return answ


def small_left_turn(tree, alpha):
    beta = tree[alpha][2]
    b = tree[beta][3]
    root = tree[alpha][1]
    if root is not None:                     # alpha это не корень
        if tree[root][2] == alpha:             # соответствующую ссылку в root надо поменять на новую вершину бета
            tree[root][2] = beta
        else:
            tree[root][3] = beta
    tree[beta][3] = alpha
    tree[beta][1] = root
    if b is not None:
        tree[b][1] = alpha
    tree[alpha][1] = beta
    tree[alpha][2] = b
    r_ch_alpha = tree[alpha][3]
    h_alpha_left, m_alpha_left = (tree[b][5], tree[b][4]) if b else (0, 0)
    h_alpha_right, m_alpha_right = (0, 0) if r_ch_alpha is None else (tree[r_ch_alpha][5], tree[r_ch_alpha][4])
    tree[alpha][5] = max(h_alpha_left, h_alpha_right) + 1
    tree[alpha][4] = tree[alpha][0] + m_alpha_left + m_alpha_right
    return tree


def great_left_turn(tree, alpha):
    beta = tree[alpha][2]                    # left child alpha
    gamma = tree[beta][3]                    # right child beta
    root = tree[alpha][1]                    # вышестоящий корень дерева
    b = tree[gamma][2]                       # left sub-tree gamma
    c = tree[gamma][3]                       # right sub-tree gamma
    if root is not None:                    # если есть вышестоящий корень
        if tree[root][2] == alpha:           # меняем в нем левую или правую ссылку
            tree[root][2] = gamma
        else:
            tree[root][3] = gamma
    tree[beta][1] = gamma
    tree[beta][3] = b
    if b is not None:
        tree[b][1] = beta
    tree[gamma][1] = root
    tree[gamma][2] = beta
    tree[gamma][3] = alpha
    tree[alpha][2] = c
    if c is not None:
        tree[c][1] = alpha
        tree[alpha][5] = max(tree[c][5], tree[tree[alpha][3]][5]) + 1
        tree[alpha][4] = tree[alpha][0] + tree[c][4] + tree[tree[alpha][3]][4]
    else:
        if tree[alpha][3] is None:
            tree[alpha][5] = 1
            tree[alpha][4] = tree[alpha][1]
        else:
            tree[alpha][5] = tree[tree[alpha][3]][5] + 1
            tree[alpha][4] = tree[alpha][0] + tree[tree[alpha][3]][4]
    tree[alpha][1] = gamma
    h_beta_left_child = 0 if tree[beta][2] is None else tree[tree[beta][2]][5]
    h_beta_right_child = 0 if b is None else tree[b][5]
    tree[beta][5] = max(h_beta_left_child, h_beta_right_child) + 1
    m_beta_left_child = 0 if tree[beta][2] is None else tree[tree[beta][2]][4]
    m_beta_right_child = 0 if b is None else tree[b][4]
    tree[beta][4] = tree[beta][0] + m_beta_left_child + m_beta_right_child
    tree[gamma][5] = max(tree[beta][5], tree[alpha][5]) + 1
    return tree


def small_right_turn(tree, alpha):
    root = tree[alpha][1]
    beta = tree[alpha][3]
    b = tree[beta][2]
    if root is not None:                     # alpha это не корень
        if tree[root][2] == alpha:           # соответствующую ссылку в root надо поменять на новую вершину бета
            tree[root][2] = beta
        else:
            tree[root][3] = beta
    tree[alpha][1] = beta
    tree[alpha][3] = b
    if b is not None:
        tree[b][1] = alpha
    tree[beta][1] = root
    tree[beta][2] = alpha
    l_ch_alpha = tree[alpha][2]
    h_alpha_left, m_alpha_left = (0, 0) if l_ch_alpha is None else (tree[l_ch_alpha][5], tree[l_ch_alpha][4])
    h_alpha_right, m_alpha_right = (tree[b][5], tree[b][4]) if b else (0, 0)
    tree[alpha][5] = max(h_alpha_left, h_alpha_right if b else 0) + 1
    tree[alpha][4] = tree[alpha][0] + m_alpha_left + m_alpha_right
    return tree


def great_right_turn(tree, alpha):
    root = tree[alpha][1]                    # вышестоящий корень дерева
    beta = tree[alpha][3]                    # right child alpha
    gamma = tree[beta][2]                    # left child beta
    b = tree[gamma][2]                       # left sub-tree gamma
    c = tree[gamma][3]                       # right sub-tree gamma
    if root is not None:                    # если есть вышестоящий корень
        if tree[root][2] == alpha:           # меняем в нем левую или правую ссылку
            tree[root][2] = gamma
        else:
            tree[root][3] = gamma
    tree[alpha][1] = gamma
    tree[alpha][3] = b
    if b is not None:
        tree[b][1] = alpha
    tree[gamma][1] = root
    tree[gamma][2] = alpha
    tree[gamma][3] = beta
    tree[beta][2] = c
    if c is not None:
        tree[c][1] = beta
        tree[beta][5] = max(tree[c][5], tree[tree[beta][3]][5]) + 1
        tree[beta][4] = tree[beta][0] + tree[c][4] + tree[tree[beta][3]][4]
    else:
        if tree[beta][3] is None:
            tree[beta][5] = 1
            tree[beta][4] = tree[beta][0]
        else:
            tree[beta][5] = tree[tree[beta][3]][5] + 1
            tree[beta][4] = tree[beta][0] + tree[tree[beta][3]][4]
    tree[beta][1] = gamma
    h_alpha_left_child = 0 if tree[alpha][2] is None else tree[tree[alpha][2]][5]
    h_alpha_right_child = 0 if b is None else tree[b][5]
    tree[alpha][5] = max(h_alpha_left_child, h_alpha_right_child) + 1
    m_alpha_left_child = 0 if tree[alpha][2] is None else tree[tree[alpha][2]][4]
    m_alpha_right_child = 0 if b is None else tree[b][4]
    tree[alpha][4] = tree[alpha][0] + m_alpha_left_child + m_alpha_right_child
    tree[gamma][5] = max(tree[alpha][5], tree[beta][5]) + 1
    return tree


def balance(tree, el):
    if el is None:
        return tree, el
    while True:                                                       # while not root
        krit_l = tree[el][2] is None
        hl = 0 if krit_l else tree[tree[el][2]][5]                    # left_child = tree[el[2]
        krit_r = tree[el][3] is None
        hr = 0 if krit_r else tree[tree[el][3]][5]                    # right_child = tree[el][3]
        if abs(hl - hr) > 1:                                          # need rotation?
            if hl > hr:                                               # left rotation
                left_grandson = 0 if tree[tree[el][2]][2] is None else tree[tree[tree[el][2]][2]][5]
                if left_grandson > hr:                       # tree[tree[el][2]][2] and left grandson is very grate
                    tree = small_left_turn(tree, el)
                else:
                    tree = great_left_turn(tree, el)
            else:                                                                      # right rotation
                right_grandson = 0 if tree[tree[el][3]][3] is None else tree[tree[tree[el][3]][3]][5]
                if right_grandson > hl:                      # tree[tree[el][3]][3] and right grandson is very grate
                    tree = small_right_turn(tree, el)
                else:
                    tree = great_right_turn(tree, el)
            ml, hl = (0, 0) if tree[el][2] is None else (tree[tree[el][2]][4], tree[tree[el][2]][5])
            mr, hr = (0, 0) if tree[el][3] is None else (tree[tree[el][3]][4], tree[tree[el][3]][5])
            tree[el][4] = ml + mr + tree[el][0]
            tree[el][5] = max(hl, hr) + 1
        else:
            ml = 0 if tree[el][2] is None else tree[tree[el][2]][4]
            mr = 0 if tree[el][3] is None else tree[tree[el][3]][4]
            tree[el][4] = ml + mr + tree[el][0]
            tree[el][5] = max(hl, hr) + 1
        if tree[el][1] is None:
            return tree, el
        el = tree[el][1]


def insert_tree(tree, elem, root):
    if root is None:                                                 # if tree is empty
        return [[elem, None, None, None, elem, 1]], 0
    root_old = root
    while elem != tree[root][0]:
        if elem < tree[root][0]:                                     # go left
            if tree[root][2] is None:
                if table_empty:
                    num = table_empty.pop()
                    tree[root][2] = num
                    tree[num] = [elem, root, None, None, elem, 1]
                else:
                    tree[root][2] = len(tree)
                    tree.append([elem, root, None, None, elem, 1])
                tree[root][5] = 2
                tree[root][4] += elem
                parent = tree[root][1]
                while not (parent is None):                         # пересчитываем массы и высоты до корня
                    m_par_r, h_par_r = (0, 0) if tree[parent][3] is None else \
                        (tree[tree[parent][3]][4], tree[tree[parent][3]][5])
                    m_par_l, h_par_l = (0, 0) if tree[parent][2] is None else \
                        (tree[tree[parent][2]][4], tree[tree[parent][2]][5])
                    tree[parent][5] = max(h_par_l, h_par_r) + 1
                    tree[parent][4] = m_par_l + tree[parent][0] + m_par_r
                    parent = tree[parent][1]
                return tree, root if tree[root][1] is None else tree[root][1]
            else:
                root = tree[root][2]                                 # идти есть куда - спускаемся влево
        else:                                                        # идем вправо
            if tree[root][3] is None:                                # но идти уже некуда, вставляем левого ребенка
                if table_empty:
                    num = table_empty.pop()
                    tree[root][3] = num
                    tree[num] = [elem, root, None, None, elem, 1]
                else:
                    tree[root][3] = len(tree)
                    tree.append([elem, root, None, None, elem, 1])
                tree[root][5] = 2
                tree[root][4] += elem
                parent = tree[root][1]
                while parent is not None:                            # пересчитываем массы и высоты до корня
                    m_par_r, h_par_r = (0, 0) if tree[parent][3] is None else \
                        (tree[tree[parent][3]][4], tree[tree[parent][3]][5])
                    m_par_l, h_par_l = (0, 0) if tree[parent][2] is None else \
                        (tree[tree[parent][2]][4], tree[tree[parent][2]][5])
                    tree[parent][5] = max(h_par_l, h_par_r) + 1
                    tree[parent][4] = m_par_l + tree[parent][0] + m_par_r
                    parent = tree[parent][1]
                return tree, root if tree[root][1] is None else tree[root][1]
            else:
                root = tree[root][3]                                 # идти есть куда - спускаемся вправо
    return tree, root_old                                            # нашелся такой же элемент, ничего не портим


def find_sum(tree, r, el):
    node = r
    found = False
    sum_l, sum_r = 0, 0
    while node is not None:
        if el < tree[node][0]:
            sum_r += tree[node][0]
            if tree[node][3] is not None:
                sum_r += tree[tree[node][3]][4]
            node = tree[node][2]
        elif el > tree[node][0]:
            sum_l += tree[node][0]
            if tree[node][2] is not None:
                sum_l += tree[tree[node][2]][4]
            node = tree[node][3]
        else:
            found = True
            break
    if found:
        if tree[node][2] is not None:
            sum_l += tree[tree[node][2]][4]
        if tree[node][3] is not None:
            sum_r += tree[tree[node][3]][4]
    return sum_l, sum_r


def del_elem(tree, number):
    par = tree[number][1]
    if tree[number][2] is None and tree[number][3] is None:  # у искомого элемента нет детей, он внизу дерева
        table_empty.add(number)                                       # del tree[number]
        if par is not None:                                # убеждаемся, что это не корень, т.е. не последний элемент
            if tree[par][2] == number:                                   # if number is left child par
                tree[par][2] = None
                if tree[par][3] is None:
                    tree[par][5] = 1
                    tree[par][4] = tree[par][0]
                else:
                    tree[par][5] = 1 + tree[tree[par][3]][5]
                    tree[par][4] = tree[par][0] + tree[tree[par][3]][4]
            else:                                                        # if number is right child par
                tree[par][3] = None
                if tree[par][2] is None:
                    tree[par][5] = 1
                    tree[par][4] = tree[par][0]
                else:
                    tree[par][5] = 1 + tree[tree[par][2]][5]
                    tree[par][4] = tree[par][0] + tree[tree[par][2]][4]
            return tree, par
        else:
            table_empty.clear()
            return tree, None

    elif (tree[number][2] is None) or (tree[number][3] is None):          # у искомого элемента есть 1 дите.
        table_empty.add(number)                                        # del tree[number]
        if par is not None:                                               # и он не корень
            if tree[number][2] is None:                                   # is right child
                child = tree[number][3]
                tree[child][1] = par
                if tree[par][2] == number:
                    tree[par][2] = child
                else:
                    tree[par][3] = child
            else:                                                         # is left child
                child = tree[number][2]
                tree[child][1] = par
                if tree[par][2] == number:
                    tree[par][2] = child
                else:
                    tree[par][3] = child
            hl, ml = (0, 0) if tree[par][2] is None else (tree[tree[par][2]][5], tree[tree[par][2]][4])
            hr, mr = (0, 0) if tree[par][3] is None else (tree[tree[par][3]][5], tree[tree[par][3]][4])
            tree[par][5] = max(hl, hr) + 1
            tree[par][4] = tree[par][0] + ml + mr
            return tree, par
        else:                                                              # иксомый элемент корень и имеет 1 дитя
            child = tree[number][2] if tree[number][3] is None else tree[number][3]
            tree[child][1] = None
            return tree, child
    else:                                                        # у искомого элемента есть 2 дитя
        number1 = tree[number][2]                                # делаем шаг влево
        while tree[number1][3] is not None:                      # и идем до кона вправо
            number1 = tree[number1][3]                           # предварительно поместив его ключ в предыдущий корень
        par1 = tree[number1][1]                                  # отец найденного элемента
        if tree[number1][2] is not None:                         # if number1 have left child
            tree[tree[number1][2]][1] = number
        if par is not None:                                      # if number is NOT root
            if tree[par][2] == number:                           # find & replace reference in root
                tree[par][2] = number1
            else:
                tree[par][3] = number1
        tree[tree[number][3]][1] = number1
        tree[tree[number][2]][1] = number1
        if par1 == number:
            tree[number1][1] = par
            tree[number1][2], tree[number][2] = number, tree[number1][2]
            tree[number1][3] = tree[number][3]
            tree[number][1] = number1
            tree[number][3] = None
        else:
            tree[par1][3] = number
            tree[number][1], tree[number1][1] = par1, par            # number1 поднимаем вместо number
            tree[number1][2], tree[number][2] = tree[number][2], tree[number1][2]
            tree[number][3], tree[number1][3] = None, tree[number][3]
            tree[number][5], tree[number1][5] = tree[number1][5], tree[number][5]
        tree[par1][4] = tree[par1][4] - tree[number1][4] + tree[number][4]  # меняется его вес
        return del_elem(tree, number)


reader = sys.stdin
t = []  # key, parent, left_child, right_child, sum_tree, height_t
n = int(next(reader))
const = 1000000001
s = 0
kernel = None
table_empty = set()
for i in range(n):
    qwe = next(reader).split()
    if qwe[0] == "+":
        f = (int(qwe[1]) + s) % const
        t, point = insert_tree(t, f, kernel)
        t, kernel = balance(t, point)
    elif qwe[0] == "-":
        f = (int(qwe[1]) + s) % const
        a = find_elem(t, f, kernel)
        if a[0]:
            t, point = del_elem(t, a[1])
            t, kernel = balance(t, point)
    elif qwe[0] == "?":
        f = (int(qwe[1]) + s) % const
        st, st1 = find_elem(t, f, kernel)
        print("Found" if st else "Not found")
    else:
        fl = (int(qwe[1]) + s) % const
        fr = (int(qwe[2]) + s) % const
        left_sum_l, right_sum_l = find_sum(t, kernel, fl)
        left_sum_r, right_sum_r = find_sum(t, kernel,  fr)
        s = 0 if kernel is None else (t[kernel][4] - right_sum_r - left_sum_l)
        print(s)
