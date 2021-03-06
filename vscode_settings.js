{
    "python.formatting.provider": "yapf",
    "editor.mouseWheelZoom": true,
    "update.enableWindowsBackgroundUpdates": true,
    "glassit.alpha": 239, //Window的透明度，0到255
    "workbench.colorTheme": "SynthWave '84",
    "synthwave84.disableGlow": true,
    "vscode_custom_css.imports": [
        "file:///C:/Users/Administrator/.vscode/stylus/vscode-vibrancy-style.css",
        "file:///C:/Users/Administrator/.vscode/stylus/synthwave84.css",
        //"file:///C:/Users/Administrator/.vscode/stylus/synthwave84-noglow.css",
        "file:///C:/Users/Administrator/.vscode/stylus/toolbar.css",
        "file:///C:/Users/Administrator/.vscode/stylus/terminal.css",
        "file:///C:/Users/Administrator/.vscode/stylus/enable-electron-vibrancy.js"
    ],
    "code-runner.clearPreviousOutput": true,
    //"code-runner.runInTerminal": true,
    "code-runner.executorMap": {
        "javascript": "node",
        "java": "cd $dir && javac $fileName && java $fileNameWithoutExt",
        "c": "cd $dir && gcc $fileName -o $fileNameWithoutExt && $dir$fileNameWithoutExt",
        "cpp": "cd $dir && g++ $fileName -o $fileNameWithoutExt && $dir$fileNameWithoutExt",
        "objective-c": "cd $dir && gcc -framework Cocoa $fileName -o $fileNameWithoutExt && $dir$fileNameWithoutExt",
        "php": "php",
        "python": "set PYTHONIOENCODING=utf8 && python",
        "perl": "perl",
        "perl6": "perl6",
        "ruby": "ruby",
        "go": "go run",
        "lua": "lua",
        "groovy": "groovy",
        "powershell": "powershell -ExecutionPolicy ByPass -File",
        "bat": "cmd /c",
        "shellscript": "bash",
        "fsharp": "fsi",
        "csharp": "scriptcs",
        "vbscript": "cscript //Nologo",
        "typescript": "ts-node",
        "coffeescript": "coffee",
        "scala": "scala",
        "swift": "swift",
        "julia": "julia",
        "crystal": "crystal",
        "ocaml": "ocaml",
        "r": "Rscript",
        "applescript": "osascript",
        "clojure": "lein exec",
        "haxe": "haxe --cwd $dirWithoutTrailingSlash --run $fileNameWithoutExt",
        "rust": "cd $dir && rustc $fileName && $dir$fileNameWithoutExt",
        "racket": "racket",
        "scheme": "csi -script",
        "ahk": "autohotkey",
        "autoit": "autoit3",
        "dart": "dart",
        "pascal": "cd $dir && fpc $fileName && $dir$fileNameWithoutExt",
        "d": "cd $dir && dmd $fileName && $dir$fileNameWithoutExt",
        "haskell": "runhaskell",
        "nim": "nim compile --verbosity:0 --hints:off --run",
        "lisp": "sbcl --script",
        "kit": "kitc --run",
        "v": "v run",
        "sass": "sass --style expanded",
        "scss": "scss --style expanded",
        "less": "cd $dir && lessc $fileName $fileNameWithoutExt.css"
    }
}