# Exports
export PATH=$PATH:$HOME/.npm-global/bin:$HOME/.cargo/bin
export STARSHIP_CONFIG=~/.config/starship/starship.toml
export NPM_CONFIG_PREFIX=~/.npm-global
export HISTFILE=$HOME/.cache/zsh/zsh_history
export TERM="xterm-256color"

# define editor
if [[ -n $SSH_CONNECTION ]]; then
  export EDITOR='nvim --clean'
  alias nvim="/usr/bin/nvim --clean"
else
  export EDITOR='nvim'
fi

# Aliases
alias manga-cli="/usr/local/bin/manga-cli -o 'zathura -c ~/.config/zathura/light/zathurarc'"
alias py='python'

source $HOME/.config/zsh_plugins/sudo.plugin.zsh

[ -f "/home/javier/.ghcup/env" ] && . "/home/javier/.ghcup/env" # ghcup-env

# Starship prompt
eval "$(starship init zsh)"
source ~/.config/starship/transient.zsh
