" Neovim config
" 
" By javier
" https://github.com/jajajajavier


" ---------------|Plugins|---------------
set nocompatible	" required
filetype off		" required
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin('~/.vim/plugged')


Plugin 'VundleVim/Vundle.vim'		" Vundle required

Plugin 'haishanh/night-owl.vim'		" Theme night-owl
Plugin 'vim-airline/vim-airline'	" Airline
Plugin 'vim-airline/vim-airline-themes' " Airline themes

Plugin 'scrooloose/nerdtree'		" Nerd Tree
Plugin 'ryanoasis/vim-devicons'		" Icons for vim :)
Plugin 'christoomey/vim-tmux-navigator'	" Tmux navigation
Plugin 'ap/vim-css-color'		" Preview css colors  
Plugin 'mattn/emmet-vim'		" html, css and js autocompletion
Plugin 'codota/tabnine-vim'		" Machine learning autocomplete 
" see https://tabnine.com/semantic for info of the semantic completion


call vundle#end()
filetype plugin indent on  


" -----------|Config|---------------
syntax enable
set number
set numberwidth=1
set mouse=a
set encoding=UTF-8
set sw=2
set cursorline
set noswapfile
set clipboard=unnamedplus 

" ---------------|Aparience|---------------
colorscheme night-owl
set termguicolors
let g:airline_theme='base16_snazzy'
let g:airline#extensions#tabline#enabled = 1
let g:airline_powerline_fonts = 1
let g:airline#extensions#tabline#formatter = 'unique_tail'

" -----------|IDE|---------------
let mapleader=" "  

" Save
nmap <C-s> :w<CR>
" Quit 
nmap <C-q> :q!<CR>

" Resize windows
nmap <M-h> :vertical resize -2<CR>
nmap <M-j> :resize +2<CR>
nmap <M-k> :resize -2<CR>
nmap <M-l> :vertical resize +2<CR>

" Nerd Tree 
nmap <leader>t :NERDTreeFind<CR>
let NERDTreeQuitOnOpen = 1
let g:NERDTreeWinSize = 38
