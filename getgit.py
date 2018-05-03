import os, argparse

PURPLE = '\x1b[1;35m%s\x1b[0m'

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--token')
parser.add_argument('repo')
args = parser.parse_args()
repo = args.repo

print (PURPLE % "archiving: %s" % repo)

print (PURPLE % "retrieving repo")
cmd = "git clone git@github.com:hiqlabs/%s.git" % repo
print (cmd)
os.system(cmd)

os.chdir(repo)
cmd = """git branch -r | grep -v '\->' | while read remote; do git branch --track "${remote#origin/}" "$remote"; done"""
print (cmd)
os.system(cmd)
cmd = "git fetch --all"
print (cmd)
os.system(cmd)
cmd = "git pull --all"
print (cmd)
os.system(cmd)

os.chdir("..")

print (PURPLE % "retrieving issues")
cmd = "curl https://api.github.com/repos/hiqlabs/%s/issues?access_token=%s > %s_issues.json" % (repo, args.token, repo)
print (cmd)
os.system(cmd)

print (PURPLE % "retrieving wiki")
cmd = "git clone git@github.com:hiqlabs/%s.wiki" % repo
print (cmd)
os.system(cmd)

print (PURPLE % "coalescing")
cmd = "mv %s.wiki %s" % (repo, repo)
print (cmd)
os.system(cmd)

cmd = "mv %s_issues.json %s" % (repo, repo)
print (cmd)
os.system(cmd)

print (PURPLE % "done")