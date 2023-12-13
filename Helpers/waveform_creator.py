import typing as t

import numpy as np
import pandas as pd
from pathlib import Path

from Helpers.waveform_functions import read_waveform_binary, create_waveform_x_coords, min_max_downsample_1d, \
    min_max_downsample_2d


class BinaryWaveformClass:

    def __init__(self, path: Path, compressed: bool = False):
        self.path = path
        self.compressed = compressed
        self.waveform = None

    def get_waveform(self):
        if self.waveform:
            return self.waveform
        else:
            self.waveform = read_waveform_binary(location=self.path, compressed=self.compressed)

    def create_1d_downsample(self, size: int = 1000):
        wf = self.get_waveform()
        downsample = min_max_downsample_1d(wf=wf, size=size)

    def create_2d_downsample(self, x_inc, x_start: float = 0, size: int = 1000):
        wf = self.get_waveform()
        #wf_x = np.arange(start=x_start, size)
        downsample = min_max_downsample_2d(wf_x=, wf_y=, size=size)
