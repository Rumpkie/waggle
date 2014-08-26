#!/bin/sh
#
# Idea and implementation:  Koen Kooi
# Multiple patches support: Marcin Juszkiewicz
#
# This script will fetch an 'mbox' patch from patchwork and git am it
# usage: pw-am.sh <number>
# example: 'pw-am.sh 221' will get the patch from http://patchwork.openembedded.org/patch/221/

for patchnumber in $@;
do
    wget -nv http://patchwork.ozlabs.org/patch/$patchnumber/mbox/ -O patches/pw-am-$patchnumber.patch
    git am -s patches/pw-am-$patchnumber.patch
    rm patches/pw-am-$patchnumber.patch
done
