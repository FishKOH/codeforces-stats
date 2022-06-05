#!/bin/python3
# This Python file uses the following encoding: utf-8
import requests
import time


def hash(problem):
    res = "-1" if "contestId" not in problem else str(problem['contestId'])
    res += problem['index'] + problem['name']
    return res


if __name__ == "__main__":
    handles = input().split(',')
    handles = [h.replace(' ', '') for h in handles]
    for h in handles:
        r = requests.get('https://codeforces.com/api/user.status?handle='+str(h))
#        print(r.status_code)
        # TODO: handle r.status_code except 400 and 200
        parsed_json = r.json()
        if parsed_json['status'] == 'OK':
            all_problems = [hash(attempt['problem']) for attempt in parsed_json['result']]
            print(h, "try to solve", len(set(all_problems)), "problems")
        time.sleep(2)
