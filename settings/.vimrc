map <F8> :setlocal spell! spelllang=en_gb<CR>
set tabstop=8 shiftwidth=8
set autoindent
set smartindent
set cindent
syntax enable
set number
set list listchars=nbsp:¬,tab:»·,trail:·,extends:>
syntax on
set undofile
colorscheme sublimemonokai
set undodir=/tmp
inoremap <C-H> <C-W>

"you can delete above commands but make sure to include this one here are mandatory

let g:ale_linters = {'c':['betty-style', 'betty-doc', 'gcc']} "add betty to ale linters
"Call Vim-plug
call plug#begin('~/.vim/plugged')
	Plug 'dense-analysis/ale'|          "to install ALE
	Plug 'bstevary/betty-in-vim'|       "to install the script
call plug#end()
