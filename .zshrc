# Exports
export PATH=$PATH:$HOME/.npm-global/bin:$HOME/.cargo/bin
export ZSH="$HOME/.oh-my-zsh"
export STARSHIP_CONFIG=~/.config/starship/starship.toml
export HISTFILE=$HOME/.cache/zsh/zsh_history
export NPM_CONFIG_PREFIX=~/.npm-global


# define editor
if [[ -n $SSH_CONNECTION ]]; then
  export EDITOR='nvim --clean'
  alias nvim="/usr/bin/nvim --clean"
else
  export EDITOR='nvim'
fi

# custom file for compdump
if [ ! -d "$HOME/.cache/zsh" ]; then
    mkdir -p $HOME/.cache/zsh
fi
export ZSH_COMPDUMP="$HOME/.cache/zsh/zcompdump-$HOST-$ZSH_VERSION"

# Oh-my-zsh configs
zstyle ':omz:update' mode reminder
zstyle ':omz:update' frequency 7
CASE_SENSITIVE="true"
DISABLE_AUTO_TITLE="false"
HIST_STAMPS="dd.mm.yyyy"
plugins=(
	sudo
	git
	python
  copypath
)
source $ZSH/oh-my-zsh.sh

# Aliases

# Starship prompt
eval "$(starship init zsh)"
source ~/.config/starship/transient.zsh

# Start Window Manager
# if [ `tty` = "/dev/tty1" ]; then
# 	startx
# fi
