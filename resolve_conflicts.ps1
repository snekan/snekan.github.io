param (
    [string]$Directory = "."
)

# Get all target files
$files = Get-ChildItem -Path $Directory -Include *.html, *.css, *.js -Recurse -File

foreach ($file in $files) {
    $content = Get-Content -Path $file.FullName -Raw

    if ($content -match "<<<<<<< HEAD") {
        Write-Host "Fixing $($file.FullName)"
        
        # Regular expression to match conflict blocks and keep only the HEAD part.
        # (?s) makes . match newlines.
        $pattern = '(?s)<<<<<<< HEAD\r?\n(.*?)\r?\n=======\r?\n.*?\r?\n>>>>>>> [a-f0-9]+.*?\r?\n'
        
        $newContent = [regex]::Replace($content, $pattern, '$1' + [Environment]::NewLine)
        
        # If there are trailing marks because of EOF without newline
        $pattern2 = '(?s)<<<<<<< HEAD\r?\n(.*?)\r?\n=======\r?\n.*?\r?\n>>>>>>> [a-f0-9]+'
        $newContent = [regex]::Replace($newContent, $pattern2, '$1')

        Set-Content -Path $file.FullName -Value $newContent -NoNewline
    }
}
Write-Host "Done!"
