'''Make sure git is installed on the OS to run this program efficiently.
   Also install gitpython module using the following command:
   pip3 install gitpython. '''

from git import Repo

#git_url is the url of git repo. e.g., https://github.com/rm-rfmukul/IAAS.git
git_url=input("Enter the git url: ")
# Path of the directory where the repo is to be cloned. The directory must be empty
repo_dir=input('Enter the path of the directory where to clone: ')

#cloning the repo 
Repo.clone_from(git_url, repo_dir)