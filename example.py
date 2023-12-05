from modeller import *
from modeller.automodel import *

env = Environ()
#env.io.atom_files_directory = ['.', './atom_files']
# a = AutoModel(env, alnfile='data/examp2.ali',
#               knowns=('5fd1', '1fdn', '1fxd'), sequence='1fdx')

a = AutoModel(env, alnfile='Modeling-3D-Structure\\alignment.fasta',
              knowns=('1CTP','3J4Q','6F14','6Y05'), sequence='my_sequence')
a.starting_model = 1
a.ending_model = 5
a.make()
a.write("model.pdb")

# 4ae6_A