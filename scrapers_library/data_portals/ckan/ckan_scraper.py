import json
import sys

from ckanapi import RemoteCKAN



def ckan_package_search(base_url, query=None, **kwargs):
    remote = RemoteCKAN(base_url, get_only=True)
    packages = remote.action.package_search(q=query, rows=1000, start=1000, **kwargs)
    print(len(packages["results"]))
    print(packages["count"])
    for key in packages.keys():
        print(key)


if __name__ == "__main__":
    ckan_package_search(base_url="https://catalog.data.gov/", query="police")
