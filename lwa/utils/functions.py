#
def _certify(d, _format):
    if not _format:
        return tuple(d.values())
    op = ()
    for field in _format:
        try:
            op += (d[field],)
        except:
            op += ('NULL',)
    return op

def _include_list(ln, lp):
    if len(ln) > len(lp):
        return False
    for i in ln:
        if i in lp:
            continue
        return False
    return True

def _equal_list(ln, lp):
    return _include_list(ln, lp) and _include_list(lp, ln)


def _compare_l1(ln, lp):
    for i in ln:
        if not i in lp:
            return False
    return True
