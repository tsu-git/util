# get_eachHash.ps1
#   指定のディレクトリ配下のファイルからハッシュ値を取得する
#
#   使い方：
#       get_eachHash.ps1 directory 
#
#           directory   ディレクトリを指定する。配下のファイルから
#                       ハッシュ値を取得する。
#           outfile     一覧の出力先ファイルを指定する。指定をしない場合
#                       ツール配置ディレクトリ配下に次の名前で出力する。
#                       hash_list_YYYYMMDD_hh24miss.txt
#

# 引数取得
Param([parameter(Mandatory=$true)][String]$dir,
      [parameter(Mandatory=$false)][String]$outfile)

# 調査対象ディレクトリチェック
$my_name = $Myinvocation.MyCommand.Name
if ($false -eq (Test-Path $dir -PathType container)) {
    echo "Usage: ${my_name} directory [outfile]"
    echo "${dir} is not found"
    exit
}

# デフォルトの出力ファイル名を生成
if ($outfile -eq "") {
    $timestamp = Get-Date -format "yyyyMMdd_HHmmss"
    $outfile = ".\hash_list_$timestamp.txt"
}

# ファイルが存在しない場合は作成する
if ($false -eq (Test-Path $outfile -PathType leaf)) {
    New-Item $outfile | Out-Null
}

# ファイルアイテムを取得する
$o_fileItem = Get-Item $outfile

# 引数で指定されたディレクトリに移動する
#   ドライブが異なる場合でも取得できるようにするため。
pushd $dir

# 指定のディレクトリからファイルリストを取得
$fileList = Get-ChildItem($dir) | Where-Object { ! $_.PSIsContainer }
$num_of_files = $fileList.Length
echo "Got ${num_of_files} files from ${dir}" | 
    Out-File -FilePath $o_fileItem -Encoding utf8

# ハッシュ値取得
foreach ($file in $fileList) {
    $fname = $file.Name
    $h_value = (Get-FileHash($file)).hash
    echo "${fname} ${h_value}" | Out-File -FilePath $o_fileItem -Encoding utf8 -append
}

# 元のディレクトリに戻る
popd

echo "$my_name finished to output file hashes: "
echo ${o_fileItem}.FullName
