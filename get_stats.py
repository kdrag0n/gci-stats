#!/usr/bin/env python3

import sys

import graphyte
import requests

def get_orgs():
    with requests.get("https://codein.withgoogle.com/api/program/current/organization/") as resp:
        if resp.status_code != 200:
            print(f"Received status code {resp.status_code}: {resp.text}")
            exit(1)

        return resp.json()["results"]

def report_graphite(orgs):
    for org in orgs:
        name_base = f"gci.{org['program_year']}.{org['slug']}"
        count = org["completed_task_instance_count"]

        graphyte.send(f"{name_base}.tasks_completed", count)

def report_console(orgs):
    counts = ((org["name"], org["completed_task_instance_count"]) for org in orgs)

    # Sort and print by descending order of tasks completed
    counts = sorted(counts, key=lambda x: x[1], reverse=True)
    for org, count in counts:
        print(f"{org}: {count}")

def main():
    orgs = get_orgs()
    report_console(orgs)

    if len(sys.argv) > 1:
        graphyte.init(sys.argv[1])
        report_graphite(orgs)

if __name__ == '__main__':
    main()
