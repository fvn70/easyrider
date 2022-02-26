import json


def main():
    json_str = input()
    dics = json.loads(json_str)
    lines = {line['bus_id'] for line in dics}
    stops = {s['stop_id']: s['stop_name'] for s in dics}
    start = set()
    finish = set()
    for line in lines:
        stop_s = [s['stop_name'] for s in dics if s['bus_id'] == line and s['stop_type'] == 'S']
        stop_f = [s['stop_name'] for s in dics if s['bus_id'] == line and s['stop_type'] == 'F']
        if len(stop_s) == 0 or len(stop_f) == 0:
            print(f'There is no start or end stop for the line: {line}.')
            return
        start.add(stop_s[0])
        finish.add(stop_f[0])
    sd = {}
    for d in dics:
        sd.setdefault(d['stop_id'], []).append(d['bus_id'])
    trans = [stops[s] for s in sd if len(sd[s]) > 1]
    print(f'Start stops: {len(start)} {sorted(list(start))}')
    print(f'Transfer stops: {len(trans)} {sorted(list(trans))}')
    print(f'Finish  stops: {len(finish)} {sorted(list(finish))}')


if __name__ == '__main__':
    main()
