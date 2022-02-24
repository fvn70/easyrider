import json
import re


def check(k, v):
    if k in ('bus_id', 'stop_id', 'next_stop'):
        return type(v) is int
    if k == 'stop_name':
        if v == '' or type(v) != type('a'):
            return False
        # sn = v.split()
        # rez = len(sn) > 1 and sn[0][0].isupper() and sn[-1] in suff
        # return rez
    if k == 'stop_type':
        rez = type(v) == type('a') and v == '' or v in ['S', 'O', 'F']
        return rez
    if k == 'a_time':
        return type(v) == type('a') and re.match(r'[0-2][0-9]:\d\d', v) != None
    return True


suff = 'Avenue Boulevard Road Street'
errs = {"bus_id": 0, "stop_id": 0, "stop_name": 0, "next_stop": 0, "stop_type": 0, "a_time": 0}


def main():
    json_str = input()
    dics = json.loads(json_str)
    cnt = 0
    for el in dics:
        for k, v in el.items():
            if not check(k, v):
                errs[k] += 1
                cnt += 1
    print(f"Type and required field validation: {cnt} errors")
    for k in errs:
        print(f"{k}: {errs[k]}")


if __name__ == '__main__':
    main()