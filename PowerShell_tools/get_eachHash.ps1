# get_eachHash.ps1
#   �w��̃f�B���N�g���z���̃t�@�C������n�b�V���l���擾����
#
#   �g�����F
#       get_eachHash.ps1 directory 
#
#           directory   �f�B���N�g�����w�肷��B�z���̃t�@�C������
#                       �n�b�V���l���擾����B
#           outfile     �ꗗ�̏o�͐�t�@�C�����w�肷��B�w������Ȃ��ꍇ
#                       �c�[���z�u�f�B���N�g���z���Ɏ��̖��O�ŏo�͂���B
#                       hash_list_YYYYMMDD_hh24miss.txt
#

# �����擾
Param([parameter(Mandatory=$true)][String]$dir,
      [parameter(Mandatory=$false)][String]$outfile)

# �����Ώۃf�B���N�g���`�F�b�N
$my_name = $Myinvocation.MyCommand.Name
if ($false -eq (Test-Path $dir -PathType container)) {
    echo "Usage: ${my_name} directory [outfile]"
    echo "${dir} is not found"
    exit
}

# �f�t�H���g�̏o�̓t�@�C�����𐶐�
if ($outfile -eq "") {
    $timestamp = Get-Date -format "yyyyMMdd_HHmmss"
    $outfile = ".\hash_list_$timestamp.txt"
}

# �t�@�C�������݂��Ȃ��ꍇ�͍쐬����
if ($false -eq (Test-Path $outfile -PathType leaf)) {
    New-Item $outfile | Out-Null
}

# �t�@�C���A�C�e�����擾����
$o_fileItem = Get-Item $outfile

# �����Ŏw�肳�ꂽ�f�B���N�g���Ɉړ�����
#   �h���C�u���قȂ�ꍇ�ł��擾�ł���悤�ɂ��邽�߁B
pushd $dir

# �w��̃f�B���N�g������t�@�C�����X�g���擾
$fileList = Get-ChildItem($dir) | Where-Object { ! $_.PSIsContainer }
$num_of_files = $fileList.Length
echo "Got ${num_of_files} files from ${dir}" | 
    Out-File -FilePath $o_fileItem -Encoding utf8

# �n�b�V���l�擾
foreach ($file in $fileList) {
    $fname = $file.Name
    $h_value = (Get-FileHash($file)).hash
    echo "${fname} ${h_value}" | Out-File -FilePath $o_fileItem -Encoding utf8 -append
}

# ���̃f�B���N�g���ɖ߂�
popd

echo "$my_name finished to output file hashes: "
echo ${o_fileItem}.FullName
