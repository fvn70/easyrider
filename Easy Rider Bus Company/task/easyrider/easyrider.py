import json


def check_o_stops(data):
    stops = {s['stop_id']: s['stop_name'] for s in data}
    start = [d['stop_id'] for d in data if d['stop_type'] == 'S']
    finish = [d['stop_id'] for d in data if d['stop_type'] == 'F']
    sd = {}
    for d in data:
        sd.setdefault(d['stop_id'], []).append(d['bus_id'])
    trans = [s for s in sd if len(sd[s]) > 1]
    demand = [d['stop_id'] for d in data if d['stop_type'] == 'O']
    print('On demand stops test:')
    err = []
    for d in demand:
        if d in set(start + finish + trans):
            err.append(stops[d])
    print(f'Wrong stop type: {sorted(err)}' if err else 'OK')


def main():
    json_str = input()
    data = json.loads(json_str)
    check_o_stops(data)


if __name__ == '__main__':
    main()
