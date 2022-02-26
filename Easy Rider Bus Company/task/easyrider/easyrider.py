import json
from datetime import datetime


def check_stops(data):
    lines = {line['bus_id'] for line in data}
    stops = {s['stop_id']: s['stop_name'] for s in data}
    start = set()
    finish = set()
    for line in lines:
        stop_s = [s['stop_name'] for s in data if s['bus_id'] == line and s['stop_type'] == 'S']
        stop_f = [s['stop_name'] for s in data if s['bus_id'] == line and s['stop_type'] == 'F']
        if len(stop_s) == 0 or len(stop_f) == 0:
            print(f'There is no start or end stop for the line: {line}.')
            return
        start.add(stop_s[0])
        finish.add(stop_f[0])
    sd = {}
    for d in data:
        sd.setdefault(d['stop_id'], []).append(d['bus_id'])
    trans = [stops[s] for s in sd if len(sd[s]) > 1]
    print(f'Start stops: {len(start)} {sorted(list(start))}')
    print(f'Transfer stops: {len(trans)} {sorted(list(trans))}')
    print(f'Finish  stops: {len(finish)} {sorted(list(finish))}')


def check_time(data):
    lines = {line['bus_id'] for line in data}
    print('Arrival time test:')
    cnt = 0
    for line in lines:
        stops = {s['stop_id']: [s['stop_name'], s['a_time'], s['stop_type']] for s in data if s['bus_id'] == line}
        n_start = [s for s in stops if stops[s][2] == 'S'][0]
        n_finish = [s for s in stops if stops[s][2] == 'F'][0]
        t_prev = None
        for k in sorted(stops, reverse=(n_start > n_finish)):
            t = datetime.strptime(stops[k][1], '%H:%M').time()
            if t_prev and t <= t_prev:
                cnt += 1
                print(f'bus_id line {line}: wrong time on station {stops[k][0]}')
                break
            t_prev = t
    if cnt == 0:
        print('OK')


def main():
    json_str = input()
    data = json.loads(json_str)
    check_time(data)


if __name__ == '__main__':
    main()
