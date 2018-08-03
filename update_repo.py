from git import Repo, Remote, RemoteProgress

# get repository
repo = Repo(".")


# check if loaded correctly
if repo.bare:
    print("Couldn't load repository.")
    exit(-1)


username = "ai-vithink"
# list of remotes
remotes = repo.remotes
url = remotes.origin.url


def has_upstream(iterable):
    for item in iterable:
        if str(item) == "upstream":
            return True
    return False


# check upstream
if has_upstream(remotes):
    new_url_header, new_url_link = url.split(':')
    new_url = new_url_header + username + new_url_link.splot("/")[1]
    Remote.create(repo, "upstream", new_url)


remotes.origin.pull()
