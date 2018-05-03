import os, argparse

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--token')
parser.add_argument('repo')
args = parser.parse_args()
repo = args.repo

print ("archiving:", repo)

print ("retrieving issues")
cmd = "curl https://api.github.com/repos/hiqlabs/%s/issues?access_token=%s > %s" % (repo, args.token, repo+"_issues.json")
print (cmd)
os.system(cmd)