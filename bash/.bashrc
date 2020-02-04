#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
PS1='[\u@\h \W]\$ '


export PATH="$PATH:$HOME/.rvm/bin" # Add RVM to PATH for scripting
export PATH="$PATH:$HOME/.local/bin" # Add RVM to PATH for scripting
# export PATH="$PATH:/usr/sbin/geckodriver"
. ~/.bashrc.local

#THIS MUST BE AT THE END OF THE FILE FOR SDKMAN TO WORK!!!
export SDKMAN_DIR="/home/username/.sdkman"
[[ -s "/home/username/.sdkman/bin/sdkman-init.sh" ]] && source "/home/username/.sdkman/bin/sdkman-init.sh"

export PATH="$PATH:$HOME/go/bin"
export PATH="$PATH:$HOME/.composer/vendor/bin"
export PATH=/home/username/.solc-select:$PATH

export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion

PATH="$PATH:$(ruby -e 'puts Gem.user_dir')/bin"
