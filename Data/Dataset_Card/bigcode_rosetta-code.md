---
license: cc-by-sa-4.0
language: code
---

# Dataset Card for the Rosetta Code Dataset

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Dataset Creation](#dataset-creation)
  - [Curation Rationale](#curation-rationale)
  - [Source Data](#source-data)
  - [Annotations](#annotations)
  - [Personal and Sensitive Information](#personal-and-sensitive-information)
- [Considerations for Using the Data](#considerations-for-using-the-data)
  - [Social Impact of Dataset](#social-impact-of-dataset)
  - [Discussion of Biases](#discussion-of-biases)
  - [Other Known Limitations](#other-known-limitations)
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions)

## Dataset Description

- **Homepage:**
- **Repository:**
- **Paper:**
- **Leaderboard:**
- **Point of Contact:**

### Dataset Summary

> Rosetta Code is a programming chrestomathy site. The idea is to present solutions to the same task in as many different languages as possible, to demonstrate how languages are similar and different, and to aid a person with a grounding in one approach to a problem in learning another. Rosetta Code currently has 1,203 tasks, 389 draft tasks, and is aware of 883 languages, though we do not (and cannot) have solutions to every task in every language.

### Supported Tasks and Leaderboards

[More Information Needed]

### Languages

```
['ALGOL 68', 'Arturo', 'AWK', 'F#', 'Factor', 'Go', 'J', 'jq', 'Julia', 'Lua', 'Mathematica/Wolfram Language',
 'Perl', 'Phix', 'Picat', 'Python', 'Quackery', 'Raku', 'Ring', 'Sidef', 'Vlang', 'Wren', 'XPL0', '11l',
 '68000 Assembly', '8th', 'AArch64 Assembly', 'ABAP', 'ACL2', 'Action!', 'ActionScript', 'Ada', 'Aime', 'ALGOL W',
 'Amazing Hopper', 'AntLang', 'Apex', 'APL', 'AppleScript', 'ARM Assembly', 'ATS', 'AutoHotkey', 'AutoIt', 'Avail',
 'Babel', 'bash', 'BASIC', 'BASIC256', 'BQN', 'Bracmat', 'Burlesque', 'C', 'C#', 'C++', 'Ceylon', 'Clojure', 'COBOL',
 'CoffeeScript', 'Common Lisp', 'Component Pascal', 'Crystal', 'D', 'Delphi', 'Dyalect', 'E', 'EasyLang', 'EchoLisp',
 'ECL', 'Efene', 'EGL', 'Ela', 'Elena', 'Elixir', 'Elm', 'Emacs Lisp', 'Erlang', 'ERRE', 'Euphoria', 'Fantom', 'FBSL',
 'Forth', 'Fortran', 'Free Pascal', 'FreeBASIC', 'Frink', 'FunL', 'Futhark', 'FutureBasic', 'Gambas', 'GAP', 'Genie',
 'GLSL', 'Gosu', 'Groovy', 'Haskell', 'HicEst', 'Hy', 'i', 'Icon and Unicon', 'IDL', 'Idris', 'Inform 7', 'Ioke', 'Java',
 'JavaScript', 'K', 'Klingphix', 'Klong', 'Kotlin', 'LabVIEW', 'Lambdatalk', 'Lang5', 'langur', 'Lasso', 'LFE', 'Liberty BASIC',
 'LIL', 'Limbo', 'Lingo', 'Little', 'Logo', 'M2000 Interpreter', 'Maple', 'Mathcad', 'Mathematica / Wolfram Language',
 'MATLAB / Octave', 'Maxima', 'Mercury', 'min', 'MiniScript', 'Nanoquery', 'Neko', 'Nemerle', 'NetRexx', 'NewLISP', 'Nial',
 'Nim', 'Oberon-2', 'Objeck', 'Objective-C', 'OCaml', 'Oforth', 'Onyx', 'ooRexx', 'Order', 'OxygenBasic', 'Oz', 'PARI/GP',
 'Pascal', 'Phixmonti', 'PHP', 'PicoLisp', 'Pike', 'PL/I', 'Pony', 'PostScript', 'PowerShell', 'Processing', 'Prolog',
 'PureBasic', 'Q', 'QBasic', 'QB64', 'R', 'Racket', 'RapidQ', 'REBOL', 'Red', 'ReScript', 'Retro', 'REXX', 'RLaB', 'Ruby',
 'Rust', 'S-lang', 'SASL', 'Scala', 'Scheme', 'Seed7', 'SenseTalk', 'SETL', 'Simula', '360 Assembly', '6502 Assembly', 'Slate',
 'Smalltalk', 'Ol', 'SNOBOL4', 'Standard ML', 'Stata', 'Swift', 'Tailspin', 'Tcl', 'TI-89 BASIC', 'Trith', 'UNIX Shell',
 'Ursa', 'Vala', 'VBA', 'VBScript', 'Visual Basic .NET', 'Wart', 'BaCon', 'Bash', 'Yabasic', 'Yacas', 'Batch File', 'Yorick',
 'Z80 Assembly', 'BBC BASIC', 'Brat', 'zkl', 'zonnon', 'Zsh', 'ZX Spectrum Basic', 'Clipper/XBase++', 'ColdFusion', 'Dart',
 'DataWeave', 'Dragon', 'FurryScript', 'Fōrmulæ', 'Harbour', 'hexiscript', 'Hoon', 'Janet', '0815', 'Jsish', 'Latitude', 'LiveCode',
 'Aikido', 'AmigaE', 'MiniZinc', 'Asymptote', 'NGS', 'bc', 'Befunge', 'Plorth', 'Potion', 'Chef', 'Clipper', 'Relation', 'Robotic',
 'dc', 'DCL', 'DWScript', 'Shen', 'SPL', 'SQL', 'Eiffel', 'Symsyn', 'Emojicode', 'TI-83 BASIC', 'Transd', 'Excel', 'Visual Basic',
 'FALSE', 'WDTE', 'Fermat', 'XLISP', 'Zig', 'friendly interactive shell', 'Zoea', 'Zoea Visual', 'GEORGE', 'Haxe', 'HolyC', 'LSE64',
 'M4', 'MAXScript', 'Metafont', 'МК-61/52', 'ML/I', 'Modula-2', 'Modula-3', 'MUMPS', 'NSIS', 'Openscad', 'Panda', 'PHL', 'Piet',
 'Plain English', 'Pop11', 'ProDOS', '8051 Assembly', 'Python 3.x Long Form', 'Raven', 'ALGOL 60', 'Run BASIC', 'Sass/SCSS', 'App Inventor',
 'smart BASIC', 'SNUSP', 'Arendelle', 'SSEM', 'Argile', 'Toka', 'TUSCRIPT', '4DOS Batch', '8080 Assembly', 'Vedit macro language',
 '8086 Assembly', 'Axe', 'Elisa', 'Verilog', 'Vim Script', 'x86 Assembly', 'Euler Math Toolbox', 'Acurity Architect', 'XSLT', 'BML',
 'Agena', 'Boo', 'Brainf***', 'LLVM', 'FOCAL', 'Frege', 'ALGOL-M', 'ChucK', 'Arbre', 'Clean', 'Hare', 'MATLAB', 'Astro', 'Applesoft BASIC',
 'OOC', 'Bc', 'Computer/zero Assembly', 'SAS', 'Axiom', 'B', 'Dao', 'Caché ObjectScript', 'CLU', 'Scilab', 'DBL', 'Commodore BASIC', 'Diego',
 'Dc', 'BCPL', 'Alore', 'Blade', 'Déjà Vu', 'Octave', 'Cowgol', 'BlitzMax', 'Falcon', 'BlooP', 'SequenceL', 'Sinclair ZX81 BASIC', 'GW-BASIC',
 'Lobster', 'C1R', 'Explore', 'Clarion', 'Locomotive Basic', 'GUISS', 'Clio', 'TXR', 'Ursala', 'CLIPS', 'Microsoft Small Basic', 'Golfscript',
 'Beads', 'Coco', 'Little Man Computer', 'Chapel', 'Comal', 'Curry', 'GML', 'NewLisp', 'Coq', 'Gastona', 'uBasic/4tH', 'Pyret', 'Dhall',
 'Plain TeX', 'Halon', 'Wortel', 'FormulaOne', 'Dafny', 'Ksh', 'Eero', 'Fan', 'Draco', 'DUP', 'Io', 'Metapost', 'Logtalk', 'Dylan', 'TI-83_BASIC',
 'Sather', 'Rascal', 'SIMPOL', 'IS-BASIC', 'KonsolScript', 'Pari/Gp', 'Genyris', 'EDSAC order code', 'Egel', 'Joy', 'lang5', 'XProc', 'XQuery',
 'POV-Ray', 'Kitten', 'Lisaac', 'LOLCODE', 'SVG', 'MANOOL', 'LSL', 'Moonscript', 'Fhidwfe', 'Inspired by Rascal', 'Fish', 'MIPS Assembly',
 'Monte', 'FUZE BASIC', 'NS-HUBASIC', 'Qi', 'GDScript', 'Glee', 'SuperCollider', 'Verbexx', 'Huginn', 'I', 'Informix 4GL', 'Isabelle', 'KQL',
 'lambdatalk', 'RPG', 'Lhogho', 'Lily', 'xTalk', 'Scratch', 'Self', 'MAD', 'RATFOR', 'OpenEdge/Progress', 'Xtend', 'Suneido', 'Mirah',
 'mIRC Scripting Language', 'ContextFree', 'Tern', 'MMIX', 'AmigaBASIC', 'AurelBasic', 'TorqueScript', 'MontiLang', 'MOO', 'MoonScript',
 'Unicon', 'fermat', 'q', 'Myrddin', 'உயிர்/Uyir', 'MySQL', 'newLISP', 'VHDL', 'Oberon', 'Wee Basic', 'OpenEdge ABL/Progress 4GL', 'X86 Assembly',
 'XBS', 'KAP', 'Perl5i', 'Peloton', 'PL/M', 'PL/SQL', 'Pointless', 'Polyglot:PL/I and PL/M', 'ToffeeScript', 'TMG', 'TPP', 'Pure', 'Pure Data',
 'Xidel', 'S-BASIC', 'Salmon', 'SheerPower 4GL', 'Sparkling', 'Spin', 'SQL PL', 'Transact-SQL', 'True BASIC', 'TSE SAL', 'Tiny BASIC', 'TypeScript',
 'Uniface', 'Unison', 'UTFool', 'VAX Assembly', 'VTL-2', 'Wrapl', 'XBasic', 'Xojo', 'XSLT 1.0', 'XSLT 2.0', 'MACRO-10', 'ANSI Standard BASIC',
 'UnixPipes', 'REALbasic', 'Golo', 'DM', 'X86-64 Assembly', 'GlovePIE', 'PowerBASIC', 'LotusScript', 'TIScript', 'Kite', 'V', 'Powershell', 'Vorpal',
 'Never', 'Set lang', '80386 Assembly', 'Furor', 'Input conversion with Error Handling', 'Guile', 'ASIC', 'Autolisp', 'Agda', 'Swift Playground',
 'Nascom BASIC', 'NetLogo', 'CFEngine', 'OASYS Assembler', 'Fennel', 'Object Pascal', 'Shale', 'GFA Basic', 'LDPL', 'Ezhil', 'SMEQL', 'tr', 'WinBatch',
 'XPath 2.0', 'Quite BASIC', 'Gema', '6800 Assembly', 'Applescript', 'beeswax', 'gnuplot', 'ECMAScript', 'Snobol4', 'Blast', 'C/C++', 'Whitespace',
 'Blue', 'C / C++', 'Apache Derby', 'Lychen', 'Oracle', 'Alternative version', 'PHP+SQLite', 'PILOT', 'PostgreSQL', 'PowerShell+SQLite', 'PureBasic+SQLite',
 'Python+SQLite', 'SQLite', 'Tcl+SQLite', 'Transact-SQL (MSSQL)', 'Visual FoxPro', 'SmileBASIC', 'Datalog', 'SystemVerilog', 'Smart BASIC', 'Snobol', 'Terraform',
 'ML', 'SQL/PostgreSQL', '4D', 'ArnoldC', 'ANSI BASIC', 'Delphi/Pascal', 'ooREXX', 'Dylan.NET', 'CMake', 'Lucid', 'XProfan', 'sed', 'Gnuplot', 'RPN (HP-15c)',
 'Sed', 'JudoScript', 'ScriptBasic', 'Unix shell', 'Niue', 'Powerbuilder', 'C Shell', 'Zoomscript', 'MelonBasic', 'ScratchScript', 'SimpleCode', 'OASYS',
 'HTML', 'tbas', 'LaTeX', 'Lilypond', 'MBS', 'B4X', 'Progress', 'SPARK / Ada', 'Arc', 'Icon', 'AutoHotkey_L', 'LSE', 'N/t/roff', 'Fexl', 'Ra', 'Koka',
 'Maclisp', 'Mond', 'Nix', 'ZED', 'Inform 6', 'Visual Objects', 'Cind', 'm4', 'g-fu', 'pascal', 'Jinja', 'Mathprog', 'Rhope', 'Delphi and Pascal', 'Epoxy',
 'SPARK', 'B4J', 'DIBOL-11', 'JavaFX Script', 'Pixilang', 'BASH (feat. sed & tr)', 'zig', 'Web 68', 'Shiny', 'Egison', 'OS X sha256sum', 'AsciiDots',
 'FileMaker', 'Unlambda', 'eC', 'GLBasic', 'JOVIAL', 'haskell', 'Atari BASIC', 'ANTLR', 'Cubescript', 'OoRexx', 'WebAssembly', 'Woma', 'Intercal', 'Malbolge',
 'LiveScript', 'Fancy', 'Detailed Description of Programming Task', 'Lean', 'GeneXus', 'CafeOBJ', 'TechBASIC', 'blz', 'MIRC Scripting Language', 'Oxygene',
 'zsh', 'Make', 'Whenever', 'Sage', 'L++', 'Tosh', 'LC3 Assembly', 'SETL4', 'Pari/GP', 'OxygenBasic x86 Assembler', 'Pharo', 'Binary Lambda Calculus', 'Bob',
 'bootBASIC', 'Turing', 'Ultimate++', 'Gabuzomeu', 'HQ9+', 'INTERCAL', 'Lisp', 'NASM', 'SPWN', 'Turbo Pascal', 'Nickle', 'SPAD', 'Mozart/Oz', 'Batch file',
 'SAC', 'C and C++', 'vbscript', 'OPL', 'Wollok', 'Pascal / Delphi / Free Pascal', 'GNU make', 'Recursive', 'C3', 'Picolisp', 'Note 1', 'Note 2', 'Visual Prolog',
 'ivy', 'k', 'clojure', 'Unix Shell', 'Basic09', 'S-Basic', 'FreePascal', 'Wolframalpha', 'c_sharp', 'LiveCode Builder', 'Heron', 'SPSS', 'LibreOffice Basic',
 'PDP-11 Assembly', 'Solution with recursion', 'Lua/Torch', 'tsql', 'Transact SQL', 'X++', 'Xanadu', 'GDL', 'C_sharp', 'TutorialD', 'Glagol', 'Basic', 'Brace',
 'Cixl', 'ELLA', 'Lox', 'Node.js', 'Generic', 'Hope', 'Snap!', 'TSQL', 'MathCortex', 'Mathmap', 'TI-83 BASIC, TI-89 BASIC', 'ZPL', 'LuaTeX', 'AmbientTalk',
 'Alternate version to handle 64 and 128 bit integers.', 'Crack', 'Corescript', 'Fortress', 'GB BASIC', 'IWBASIC', 'RPL', 'DMS', 'dodo0', 'MIXAL', 'Occam',
 'Morfa', 'Snabel', 'ObjectIcon', 'Panoramic', 'PeopleCode', 'Monicelli', 'gecho', 'Hack', 'JSON', 'Swym', 'ReasonML', 'make', 'TOML', 'WEB', 'SkookumScript',
 'Batch', 'TransFORTH', 'Assembly', 'Iterative', 'LC-3', 'Quick Basic/QBASIC/PDS 7.1/VB-DOS', 'Turbo-Basic XL', 'GNU APL', 'OOCalc', 'QUACKASM', 'VB-DOS',
 'Typescript', 'x86-64 Assembly', 'FORTRAN', 'Furryscript', 'Gridscript', 'Necromantus', 'HyperTalk', 'Biferno', 'AspectJ', 'SuperTalk', 'Rockstar', 'NMAKE.EXE',
 'Opa', 'Algae', 'Anyways', 'Apricot', 'AutoLISP', 'Battlestar', 'Bird', 'Luck', 'Brlcad', 'C++/CLI', 'C2', 'Casio BASIC', 'Cat', 'Cduce', 'Clay', 'Cobra',
 'Comefrom0x10', 'Creative Basic', 'Integer BASIC', 'DDNC', 'DeviousYarn', 'DIV Games Studio', 'Wisp', 'AMPL', 'Pare', 'PepsiScript', 'Installing Processing',
 'Writing your first program', 'batari Basic', 'Jack', 'elastiC', 'TI-83 Hex Assembly', 'Extended BrainF***', '1C', 'PASM', 'Pict', 'ferite', 'Bori', 'RASEL',
 'Echolisp', 'XPath', 'MLite', 'HPPPL', 'Gentee', 'JSE', 'Just Basic', 'Global Script', 'Nyquist', 'HLA', 'Teradata Stored Procedure', 'HTML5', 'Portugol',
 'UBASIC', 'NOWUT', 'Inko', 'Jacquard Loom', 'JCL', 'Supernova', 'Small Basic', 'Kabap', 'Kaya', 'Kdf9 Usercode', 'Keg', 'KSI', 'Gecho', 'Gri', 'VBA Excel',
 'Luna', 'MACRO-11', 'MINIL', 'Maude', 'MDL', 'Mosaic', 'Purity', 'MUF', 'MyDef', 'MyrtleScript', 'Mythryl', 'Neat', 'ThinBASIC', 'Nit', 'NLP++', 'Odin', 'OpenLisp',
 'PDP-1 Assembly', 'Peylang', 'Pikachu', 'NESL', 'PIR', 'Plan', 'Programming Language', 'PROMAL', 'PSQL', 'Quill', 'xEec', 'RED', 'Risc-V', 'RTL/2', 'Sing', 'Sisal',
 'SoneKing Assembly', 'SPARC Assembly', 'Swahili', 'Teco', 'Terra', 'TestML', 'Viua VM assembly', 'Whiley', 'Wolfram Language', 'X10', 'Quack', 'K4', 'XL', 'MyHDL',
 'JAMES II/Rule-based Cellular Automata', 'APEX', 'QuickBASIC 4.5', 'BrightScript (for Roku)', 'Coconut', 'CSS', 'MapBasic', 'Gleam', 'AdvPL', 'Iptscrae', 'Kamailio Script',
 'KL1', 'MEL', 'NATURAL', 'NewtonScript', 'PDP-8 Assembly', 'FRISC Assembly', 'Amstrad CPC Locomotive BASIC', 'Ruby with RSpec', 'php', 'Small', 'Lush', 'Squirrel',
 'PL/pgSQL', 'XMIDAS', 'Rebol', 'embedded C for AVR MCU', 'FPr', 'Softbridge BASIC', 'StreamIt', 'jsish', 'JScript.NET', 'MS-DOS', 'Beeswax', 'eSQL', 'QL SuperBASIC',
 'Rapira', 'Jq', 'scheme', 'oberon-2', '{{header|Vlang}', 'XUL', 'Soar', 'Befunge 93', 'Bash Shell', 'JacaScript', 'Xfractint', 'JoCaml', 'JotaCode', 'Atari Basic',
 'Stretch 1', 'CFScript', 'Stretch 2', 'RPGIV', 'Shell', 'Felix', 'Flex', 'kotlin', 'Deluge', 'ksh', 'OCTAVE', 'vbScript', 'Javascript/NodeJS', 'Coffeescript',
 'MS SmallBasic', 'Setl4', 'Overview', '1. Grid structure functions', '2. Calendar data functions', '3. Output configuration', 'WYLBUR', 'Mathematica/ Wolfram Language',
 'Commodore Basic', 'Wolfram Language/Mathematica', 'Korn Shell', 'PARIGP', 'Metal', 'VBA (Visual Basic for Application)', 'Lolcode', 'mLite', 'z/Arch Assembler',
 "G'MIC", 'C# and Visual Basic .NET', 'Run Basic', 'FP', 'XEmacs Lisp', 'Mathematica//Wolfram Language', 'RPL/2', 'Ya', 'JavaScript + HTML', 'JavaScript + SVG',
 'Quick BASIC', 'MatLab', 'Pascal and Object Pascal', 'Apache Ant', 'rust', 'VBA/Visual Basic', 'Go!', 'Lambda Prolog', 'Monkey']
```

## Dataset Structure

### Data Instances

First row:
```
{'task_url': 'http://rosettacode.org/wiki/Ascending_primes',
 'task_name': 'Ascending primes',
 'task_description': "Generate and show all primes with strictly ascending decimal digits.\n\nAside: Try solving without peeking at existing solutions. I had a weird idea for generating\na prime sieve faster, which needless to say didn't pan out. The solution may be p(r)etty trivial\nbut generating them quickly is at least mildly interesting.\nTip: filtering all 7,027,260 primes below 123,456,789 probably won't kill you, but there is\nat least one significantly better and much faster way, needing a mere 511 odd/prime tests.\n\n\n\nSee also\n OEIS:A052015 - Primes with distinct digits in ascending order\n\n\nRelated\n\nPrimes with digits in nondecreasing order (infinite series allowing duplicate digits, whereas this isn't and doesn't)\nPandigital prime (whereas this is the smallest, with gaps in the used digits being permitted)\n\n",
 'language_url': '#ALGOL_68',
 'language_name': 'ALGOL 68'}
```
Code:
```
BEGIN # find all primes with strictly increasing digits                      #
    PR read "primes.incl.a68" PR                   # include prime utilities #
    PR read "rows.incl.a68"   PR                   # include array utilities #
    [ 1 : 512 ]INT primes;         # there will be at most 512 (2^9) primes  #
    INT p count := 0;                        # number of primes found so far #
    FOR d1 FROM 0 TO 1 DO
        INT n1 = d1;
        FOR d2 FROM 0 TO 1 DO
            INT n2 = IF d2 = 1 THEN ( n1 * 10 ) + 2 ELSE n1 FI;
            FOR d3 FROM 0 TO 1 DO
                INT n3 = IF d3 = 1 THEN ( n2 * 10 ) + 3 ELSE n2 FI;
                FOR d4 FROM 0 TO 1 DO
                    INT n4 = IF d4 = 1 THEN ( n3 * 10 ) + 4 ELSE n3 FI;
                    FOR d5 FROM 0 TO 1 DO
                        INT n5 = IF d5 = 1 THEN ( n4 * 10 ) + 5 ELSE n4 FI;
                        FOR d6 FROM 0 TO 1 DO
                            INT n6 = IF d6 = 1 THEN ( n5 * 10 ) + 6 ELSE n5 FI;
                            FOR d7 FROM 0 TO 1 DO
                                INT n7 = IF d7 = 1 THEN ( n6 * 10 ) + 7 ELSE n6 FI;
                                FOR d8 FROM 0 TO 1 DO
                                    INT n8 = IF d8 = 1 THEN ( n7 * 10 ) + 8 ELSE n7 FI;
                                    FOR d9 FROM 0 TO 1 DO
                                        INT n9 = IF d9 = 1 THEN ( n8 * 10 ) + 9 ELSE n8 FI;
                                        IF n9 > 0 THEN
                                            IF is probably prime( n9 ) THEN
                                                # have a prime with strictly ascending digits #
                                                primes[ p count +:= 1 ] := n9
                                            FI
                                        FI
                                    OD
                                OD
                            OD
                        OD
                    OD
                OD
            OD
        OD
    OD;
    QUICKSORT primes FROMELEMENT 1 TOELEMENT p count;     # sort the primes #
    FOR i TO p count DO                                # display the primes #
        print( ( "  ", whole( primes[ i ], -8 ) ) );
        IF i MOD 10 = 0 THEN print( ( newline ) ) FI
    OD
END
```

### Data Fields

```
Dataset({
    features: ['task_url', 'task_name', 'task_description', 'language_url', 'language_name', 'code'],
    num_rows: 79013
})
```

### Data Splits

The dataset only contains one split, namely the "train" split.

## Dataset Creation

### Curation Rationale

[More Information Needed]

### Source Data

#### Initial Data Collection and Normalization

[More Information Needed]

#### Who are the source language producers?

[More Information Needed]

### Annotations

#### Annotation process

[More Information Needed]

#### Who are the annotators?

[More Information Needed]

### Personal and Sensitive Information

[More Information Needed]

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

[More Information Needed]

## Additional Information

### Dataset Curators

[More Information Needed]

### Licensing Information

[More Information Needed]

### Citation Information

To cite the Rosetta Code webiste you can use the following bibtex entry:

```json
 @misc{rosetta-code,
   author = "Rosetta Code",
   title = "Rosetta Code --- Rosetta Code{,} ",
   year = "2022",
   url = "https://rosettacode.org/w/index.php?title=Rosetta_Code&oldid=322370",
   note = "[Online; accessed 8-December-2022]"
 }
```

### Contributions

Thanks to [@christopher](https://twitter.com/christopher) for adding this dataset.