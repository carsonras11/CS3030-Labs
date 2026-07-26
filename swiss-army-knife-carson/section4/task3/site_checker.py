import requests


sites = [
    "https://www.google.com",
    "https://github.com",
    "https://example.com/not-a-real-page"
]


for site in sites:
    try:
        response = requests.get(site)

        if response.status_code == 200:
            print(site, "- SITE UP")
        else:
            print(site, "- SITE DOWN")

    except requests.RequestException:
        print(site, "- SITE DOWN")
