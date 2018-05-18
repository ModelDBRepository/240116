import params


import runsim
import odors
from math import sqrt

params.filename = 'bulb3dtest'
params.tstop = 1050
params.sniff_invl_min = params.sniff_invl_max = 500
params.training_exc = params.training_inh = True
from neuron import h
h('sigslope_AmpaNmda=5')
h('sigslope_FastInhib=5')
h('sigexp_AmpaNmda=4')
params.odor_sequence = [ ('Onion', 50, 1000, 1e+9) ]
runsim.build_part_model([5,37,32,78], [])
runsim.run()