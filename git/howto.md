# git add
for i in $(git status | cut -d$'\n' -f7- | grep -v "^\n");do echo $i; done

http://stackoverflow.com/questions/5237605/how-can-i-run-git-status-and-just-get-the-filenames
        git status --porcelain | grep M | sed s/M//g
        git status -s | grep M | cut -c4-


for i in $(git status -s | cut -c4-); do echo $i; git add $i; done
