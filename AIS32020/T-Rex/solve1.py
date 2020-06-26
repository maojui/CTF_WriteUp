decoder = {'!!': 'U', '@!': 'E', '#!': 'K', '$!': 'N', '%!': 'X', '&!': '1', '!@': '6', '@@': 'C', '#@': 'R', '$@': 'H', '%@': 'Q', '&@': 'Y', '!#': 'P', '@#': '8', '##': '4', '$#': '0', '%#': 'L', '&#': '7', '!$': 'T', '@$': 'V', '#$': 'I', '$$': '9', '%$': 'D', '&$': '3', '!%': '2', '@%': 'A', '#%': 'J', '$%': 'M', '%%': 'O', '&%': 'Z', '!&': '5', '@&': 'G', '#&': 'S', '$&': 'B', '%&': 'F', '&&': 'W', '{' : '{', '}' : '}'}
dec = "@% #$ #& &$ { @@ !% &! $# #@ &@ !! $# %@ %& !# &! @$ %! $# %& %% $@ #& #! !! &% && %! &$ $% $$ %# %# %# $$ !@ #! #! @& !& %@ &$ $# !# &! #$ &$ #% &% !% &@ @# #@ @$ && !% %& @! &@ #$ &! @$ %@ #& %% #$ !@ !& ## %$ &@ $% #! @! $# &$ $# &$ $$ $! $& $! $@ &! @# %% &# %& #% #@ &$ &@ !! &@ &$ $! &$ @# @! !# && $! && #@ @! $@ #% $! !& @$ !$ &! @! !$ %# #& %! %$ %$ %! $$ %@ $$ %& %@ @# !& &@ #! #& #% %@ %$ $& %& %& %! #! $& #@ %& @% &! !@ !% @! !$ $@ $# &@ %! ## @@ !$ #@ $% @% !# %@ !$ %& &@ @$ $% %! &$ %$ #& #@ $% &# #$ %# $# &$ &# &$ %# @! #% $$ &$ $# %@ #$ %$ $! @# @@ !$ &@ $@ #! @% &$ #! #$ !@ #! %% !% %& #$ %% #% @@ !@ $! #! %@ #$ &@ &! @@ $# !& #@ $! ## !% %# $% %$ && %@ $! !$ #! !$ !! &@ #& @$ $$ #! $# %@ %! @# #& @$ &! %& %$ #$ $$ %& %$ !# $% @$ %& !@ #% %$ &% !# !& #! $! }"
print(''.join([decoder[c] for c in dec.split()]))