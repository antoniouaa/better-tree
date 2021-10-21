$RootColor = "Yellow"
$PathColor = "Red"
$DirBgColor = "DarkRed"
$DirFgColor = "White" 
$LeafColor = "Green"

function Get-Tree {
    [CmdletBinding()]
    param (
        [Parameter(Mandatory = $true)]
        [String]
        $Path,

        [Parameter(Mandatory = $false)]
        [String]
        $Pattern
    )

    begin {}

    process {
        $rootDepth = (Get-Location).Path.ToString().Split("\").Count
        $rawTree = Get-ChildItem -Path (Convert-Path $Path) -Recurse
        Write-Host "." -ForegroundColor $RootColor
        Write-Host "└" -NoNewline
        $counter = 0
        foreach ($line in $rawTree) {
            $pass = Test-Path $line
            if (-not $pass) {
                continue
            }
            
            $color = $LeafColor
            $name = $line.FullName
            $displayName = $line.Name

            $isDir = Test-Path $line -PathType Container
            if ($isDir) {
                $color = $DirFgColor
            }
            Write-Host "─" -NoNewline
            Write-Host " $displayName" -ForegroundColor $color
            $counter += 1
            if ($counter -ne $rawTree.Count) {
                Write-Host "└" -NoNewline
            }
            # $depth = $line.FullName.Split("\").Count - $rootDepth
            # Write-Host $depth
        }
    }
}



Export-ModuleMember -Function Get-Tree