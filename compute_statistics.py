import numpy as np
import os
import hparams as hp
from utils.files import get_files

if __name__ == '__main__':
    min_e = []
    min_p = []
    max_e = []
    max_p = []
    nz_min_p = []
    nz_min_e = []

    energy_path = os.path.join(hp.data_dir, 'energy')
    pitch_path = os.path.join(hp.data_dir, 'pitch')
    mel_path = os.path.join(hp.data_dir, 'mels')
    energy_files = get_files(energy_path, extension='.npy')
    pitch_files = get_files(pitch_path, extension='.npy')
    mel_files = get_files(mel_path, extension='.npy')

    assert len(energy_files) == len(pitch_files) == len(mel_files)

    for f in energy_files:
        e = np.load(f)
        min_e.append(e.min())
        nz_min_e.append(e[e>0].min())
        max_e.append(e.max())

    for f in pitch_files:
        p = np.load(f)
        min_p.append(p.min())
        nz_min_p.append(p[p > 0].min())
        max_p.append(p.max())

    #print("Min Energy : {}".format(min(min_e)))
    print("Non zero Min Energy : {}".format(min(nz_min_e)))
    print("Max Energy : {}".format(max(max_e)))
    #print("Min Pitch : {}".format(min(min_p)))
    print("Non zero Min Pitch : {}".format(min(nz_min_p)))
    print("Max Pitch : {}".format(max(max_p)))