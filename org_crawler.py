#!/usr/bin/env python3

import graphyte
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

# Initialize webdriver
opt = Options()
opt.headless = True
driver = webdriver.Firefox(options=opt)
driver.implicitly_wait(3)

# Initialize Graphite client
if len(sys.argv) > 1:
    print("Initializing Graphite client...")
    graphyte.init(sys.argv[1])
    report_graphite = True
else:
    report_graphite = False

# Find all organizations
org_urls = set()
print("Fetching organization list...")
driver.get("https://codein.withgoogle.com/organizations/")
for anchor in driver.find_elements_by_css_selector(
    'a[ui-sref="base.app.public.organizations.detail({slug: org.slug })"]'
):
    url = anchor.get_property("href")
    if url not in org_urls:
        org_urls.add(url)

# Get display name and tasks completed for each organization
orgs = []
for url in org_urls:
    print(f"Fetching {url}")
    driver.get(url)
    cnt = int(
        driver.find_element_by_css_selector(
            'div[ng-if="program.competition_open && org.completed_task_instance_count"]'
        ).text.split()[-1]
    )

    org_name = driver.find_element_by_css_selector("h2.org__name.md-headline").text
    orgs.append((org_name, cnt))

    # Get internal organization name from URL and report to Graphite
    if report_graphite:
        org_id = url.split("/")[-2]
        graphyte.send(f"gci.2019.{org_id}.tasks_completed", cnt)

print()

# Sort and print orgs by descending order of tasks completed
orgs = sorted(orgs, key=lambda x: x[1], reverse=True)
for org, count in orgs:
    print(f"{org}: {count}")

driver.quit()
