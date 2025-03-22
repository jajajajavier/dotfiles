# Exports
export PATH=$PATH:$HOME/.npm-global/bin:$HOME/.cargo/bin
export STARSHIP_CONFIG=~/.config/starship/starship.toml
export NPM_CONFIG_PREFIX=~/.npm-global
export HISTFILE=$HOME/.cache/zsh/zsh_history
export TERM="xterm-256color"

[ -f "/home/javier/.ghcup/env" ] && . "/home/javier/.ghcup/env" # ghcup-env

# define editor
if [[ -n $SSH_CONNECTION ]]; then
  export EDITOR='nvim --clean'
  alias nvim="/usr/bin/nvim --clean"
else
  export EDITOR='nvim'
fi

# Completion
autoload -Uz compinit
compinit

# Aliases
alias py='python3'
alias yt='yt-dlp'

alias l='ls --color=always'
alias ll='ls --color=always -lh'
alias la='ls --color=always -a'
alias lla='ls --color=always -lha'

# Plugins
source $HOME/.config/zsh_plugins/sudo.plugin.zsh

# Starship prompt
eval "$(starship init zsh)"
source ~/.config/starship/transient.zsh
