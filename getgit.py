import os, argparse

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--token')
parser.add_argument('repo')
args = parser.parse_args()
repo = args.repo

print ("archiving:", repo)

print ("retrieving issues")
cmd = "curl https://api.github.com/repos/hiqlabs/%s/issues?access_token=%s > %s_issues.json" % (repo, args.token, repo)
print (cmd)
os.system(cmd)

print ("retrieving wiki")
cmd = "git clone git@github.com:hiqlabs/%s.wiki" % repo
print (cmd)
os.system(cmd)

print ("retrieving repo")
cmd = "git clone git@github.com:hiqlabs/%s.git" % repo
print (cmd)
os.system(cmd)
