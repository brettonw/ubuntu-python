set -a

PS1="\! (\h) \W : ";
HISTCONTROL=ignoredups;
unset HISTFILE;

PATH=.:$PATH;

set +a

function ec {
    nano $*;
}

function python {
    python3.8 $*;
}
