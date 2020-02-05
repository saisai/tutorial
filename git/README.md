##Show git remote url
    git config --get remote.origin.url
    git remote show origin
    git remote -v

##Get origin master from remote
    git pull origin master

##Push origin master from local to remote
    git push -u origin master

##To list all branches
    git branch -a


##To commit edited files 
	git commit -am "edit something"
	
##To revert the edited files
    git checkout -- CONTRIBUTING.md

##To work on the other branch, need to create a local tracking branch:
    git checkout -b dev origin/dev

##Show working status tree
    git status

##To get git help
    man git
##To show each command of usage
    git help status
		
##To get lists of modified files
	git status | grep modified | tee modified.txt
	
##Error: e.g HEAD detached from 2c1f770
	nothing to commit, working directory clean	
	git checkout master
	git pull	

##Clone the repo and keep a script to update it regularly
>
>>		git clone --depth=1 --branch=STABLE https://github.com/phpmyadmin/phpmyadmin.git

##Script to run on CRON
	#!/bin/bash
	cd /home/sites/phpmyadmin/
	git pull -q origin STABLE

#“git status” and just get the filenames
	http://stackoverflow.com/questions/5237605/how-can-i-run-git-status-and-just-get-the-filenames
	git status --porcelain | grep M | sed s/M//g
	git status -s | grep M | cut -c4-
	git diff --name-only
	git diff --name-only HEAD
	
##CRON
		# Automatically upgrade PHPMyAdmin daily (5am)
		0 5 * * * /home/user/scripts/pma_update.sh >> /dev/null 2>&1
		
#Commit without setting user.email and user.name
>
>>		git -c user.name='Paul Draper' -c user.email='my@email.org' commit -m '...'

#Commit edited files only
        git commit -m "commit eidted files only" -- edited_file.md

##References:
	http://stackoverflow.com/questions/67699/clone-all-remote-branches-with-git
	http://gitready.com/intermediate/2009/02/13/list-remote-branches.html
	http://git-scm.com/book/en/v2
	http://www.raymonschouwenaar.nl/deploy-website-git-webhosting-webfaction-github-bitbucket/
	https://www.gitbook.com/@gitbookio
	https://githowto.com/cloningrepositories
	https://laracasts.com/discuss/channels/general-discussion/phpmyadmin-with-php7
	http://jonathannicol.com/blog/2013/11/19/automated-git-deployments-from-bitbucket/
	https://serverpilot.io/community/articles/how-to-automatically-deploy-a-git-repo-from-bitbucket.html
	http://symmetrycode.com/super-easy-deployment-with-git-and-bitbucket/
	https://gist.github.com/lucien144/6a44601d477784669aab
	http://stackoverflow.com/questions/22058041/commit-without-setting-user-email-and-user-name

