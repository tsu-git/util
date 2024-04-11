set scrolloff=0
set hlsearch
set expandtab
set tabstop=4
set shiftwidth=4
set autoindent
set smartindent
set showmatch
set number
set ignorecase
"vimの内部文字コード
" kaoriyaのgvimを使う場合、encoding=cp932としておく。
" メニューが文字化けしてしまう。
set encoding=utf-8
"読み込み時の文字コード
" 左から順番に試す。成功した文字コードはそのバッファのfileencodingとなる。
" ただし、通常は設定不要。
"set fileencodings=utf-8,cp932,iso-2022-jp,iso-2022-jp-2,euc-jp,sjis,utf-16
set tags=/c/Users/tsusu/.tags
set exrc
ab rl -r ~/.ruler
ab sugi sugimototb@pm.nttdata.co.jp
map \d :r !date +\%Y/\%m/\%d "年月日文字列

"数値参照文字列の変換。CRが含まれる場合は削除してエラー回避する。
map \c :.co.:.!char_ref `cat` 1

"計算。CRが含まれる場合は削除してエラー回避する。
"map \b :.co.:.!tr -d '\015' \| bc
"map \b :.co.:.!bc
map \b :.co.:.!bc ~/.bcenv

"文字コードダンプ
map \o :.w !od -Ad -tx2c
map -s :%!nkf -s
map -e :%!nkf -e
"source ~/.vim/str2htmlentity.vim
"vmap <silent> sx :Str2HtmlEntity<cr>
"vmap <silent> sr :Entity2HtmlString<cr>
