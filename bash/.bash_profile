#
# ~/.bash_profile
#

[[ -f ~/.bashrc ]] && . ~/.bashrc

CLASSPATH="."

export GOPATH=~/go
export CLASSPATH
export PTOOLSPATH=/mnt/working/tmp/phalcon-devtools/
export PATH=$PATH:/mnt/working/tmp/phalcon-devtools

[[ -s "$HOME/.rvm/scripts/rvm" ]] && source "$HOME/.rvm/scripts/rvm" # Load RVM into a shell session *as a function*
