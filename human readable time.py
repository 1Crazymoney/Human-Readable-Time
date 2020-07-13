def make_readable(seconds):
    hh = seconds // 3600
    mm = (seconds % 3600) // 60
    ss = (seconds % 3600) % 60
    h = ""
    m = ""
    s = ""
    if (len(str(hh))) < 2:
        h = "0" + str(hh)
    else:
        h = str(hh)
    if (len(str(mm))) < 2:
        m = "0" + str(mm)
    else:
        m = str(mm)
    if (len(str(ss))) < 2:
        s = "0" + str(ss)
    else:
        s = str(ss)

    time = h + ":" + m + ":" + s
    return time

