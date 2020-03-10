# git add
for i in $(git status | cut -d$'\n' -f7- | grep -v "^\n");do echo $i; done

http://stackoverflow.com/questions/5237605/how-can-i-run-git-status-and-just-get-the-filenames
        git status --porcelain | grep M | sed s/M//g
        git status -s | grep M | cut -c4-


for i in $(git status -s | cut -c4-); do echo $i; git add $i; done

Before creating a new branch, pull the changes from upstream. Your master needs to be up to date.

$ git pull

Create the branch on your local machine and switch in this branch :

$ git checkout -b [name_of_your_new_branch]

Push the branch on github :

$ git push origin [name_of_your_new_branch]

When you want to commit something in your branch, be sure to be in your branch. Add -u parameter to set-upstream.

You can see all the branches created by using :

$ git branch -a

