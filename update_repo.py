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

# check upstream
if "upstream" not in remotes:
    new_url_header, new_url_link = url.split(':')
    new_url = new_url_header + username + new_url_link.splot("/")[1]
    Remote.create(repo, "upstream", url.split(''))


class MyProgressPrinter(RemoteProgress):
    def update(self, op_code, cur_count, max_count=None, message=''):
        print(op_code, cur_count, max_count, cur_count / (max_count or 100.0), message or "NO MESSAGE")


# fetch
for fetch_info in remotes.origin.fetch(progress=MyProgressPrinter()):
    print("Updated %s to %s" % (fetch_info.ref, fetch_info.commit))
