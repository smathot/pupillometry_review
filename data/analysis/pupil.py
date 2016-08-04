# coding=utf-8

"""
This file is part of P0005.1.

P0005.1 is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

P0005.1 is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with P0005.1.  If not, see <http://www.gnu.org/licenses/>.
"""

from datamatrix import series as srs
from datamatrix import operations as ops
from datamatrix.colors.tango import *
from datamatrix import plot
from matplotlib import pyplot as plt
import numpy as np


def preprocess(dm):

	"""
	desc:
		Performs pupil preprocessing, and removes trials where pupil size was
		unrealistic.
	"""

	dm.ptrace_stimon = srs.blinkreconstruct(dm.ptrace_stimon)
	dm.ptrace_stimoff = srs.blinkreconstruct(dm.ptrace_stimoff)
	dm.ptrace_stimon.depth = 10000
	dm.ptrace_stimoff.depth = 20000
	dm.ptrace_stimon = srs.baseline(dm.ptrace_stimon, dm.ptrace_adaptation)
	dm.ptrace_stimoff = srs.baseline(dm.ptrace_stimoff, dm.ptrace_adaptation)
	return dm


def plot_trials(dm):

	dm = dm.condition == 'sound'
	for row in dm:
		plt.title('condition %s' % row.condition)
		x = np.linspace(0, 10, len(row.ptrace_stimon))
		plt.plot(x, row.ptrace_stimon)
		x = np.linspace(10, 20, len(row.ptrace_stimoff))
		plt.plot(x, row.ptrace_stimoff)
		plt.show()


def plot_lightresponse(dm):

	plot.new(size=(8,4))
	plt.ylim(0.3,1.1)
	dm = dm.condition == 'lightresponse'
	for stimcolor, _dm in ops.split(dm.stimcolor):
		if stimcolor == 'rgb(0%,0%,100%)':
			color = blue[1]
		else:
			color = red[1]
		x = np.linspace(0, 10, 10000)
		plot.trace(_dm.ptrace_stimon, x=x, color=color)
		x = np.linspace(10, 30, 20000)
		plot.trace(_dm.ptrace_stimoff, x=x, color=color)
	plt.axvline(10, color='black', linestyle=':')
	plt.ylabel('Pupil size (norm)')
	plt.xlabel('Time since stimulus onset (s)')
	plot.save('lightresponse')


def plot_nearresponse(dm):

	plot.new(size=(8,4))
	plt.ylim(0.3,1.1)
	dm = dm.condition == 'nearresponse'
	x = np.linspace(0, 10, 10000)
	plot.trace(dm.ptrace_stimon, x=x)
	x = np.linspace(10, 30, 20000)
	plot.trace(dm.ptrace_stimoff, x=x)
	plt.axvline(10, color='black', linestyle=':')
	plt.ylabel('Pupil size (norm)')
	plt.xlabel('Time since cue (s)')
	plot.save('nearresponse')


def plot_sound(dm):

	plot.new(size=(8,4))
	plt.ylim(0.3,1.1)
	dm = dm.condition == 'sound'
	x = np.linspace(0, 1, 1000)
	dm.ptrace_stimon.depth = 1000
	plot.trace(dm.ptrace_stimon, x=x)
	x = np.linspace(1, 10, 9000)
	dm.ptrace_stimoff.depth = 9000
	plot.trace(dm.ptrace_stimoff, x=x)
	plt.ylabel('Pupil size (norm)')
	plt.xlabel('Time since stimulus onset (s)')
	plot.save('sound')
