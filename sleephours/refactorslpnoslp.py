import subprocess
import pandas as pd
import os

cwd = os.getcwd()
slpd = os.path.join(cwd, 'slp')
noslpd = os.path.join(cwd, 'noslp')

slp = os.listdir(slpd)
noslp = os.listdir(noslpd)

print('SLP')
for x in slp:
    if len(x) == 21:
        errname = x[:10]
        readno = x[11]
        newname = errname + '_R' + readno
        oldfile = os.path.join(slpd, x)
        fixfile = os.path.join(slpd, errname, newname + '.fastq.gz')
        print('renaming <{}> to <{}>'.format(oldfile, fixfile))
        if not os.path.exists(fixfile):
            print('done')
            os.renames(oldfile, fixfile)

print('NOSLP')
for x in noslp:
    if len(x) == 21:
        errname = x[:10]
        readno = x[11]
        newname = errname + '_R' + readno
        oldfile = os.path.join(noslpd, x)
        fixfile = os.path.join(noslpd, errname, newname + '.fastq.gz')
        print('renaming <{}> to <{}>'.format(oldfile, fixfile))
        if not os.path.exists(fixfile):
            print('done')
            os.renames(oldfile, fixfile)