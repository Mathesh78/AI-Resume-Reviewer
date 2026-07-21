import requests


def github_profile(username: str):

    url = f"https://api.github.com/users/{username}"

    response = requests.get(url)

    if response.status_code != 200:
        return "GitHub profile not found."

    data = response.json()

    return {
        "Name": data["name"],
        "Followers": data["followers"],
        "Following": data["following"],
        "Public Repositories": data["public_repos"],
        "Bio": data["bio"],
        "Profile": data["html_url"]
    } 