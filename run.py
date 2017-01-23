import tensorflow as tf
import gym

from rl import A3CAgent, track
from util import *
from midi_util import *
import midi
from music import target_compositions

target_compositions += load_melodies('data/edm/edm_c')

with tf.device('/cpu:0'), tf.Session() as sess:
    env = track(gym.make('music-gen-v0'))
    env.num_notes = 128
    agent = make_agent()
    agent.load(sess)
    agent.run(sess, env)
    print('Composition', env.composition)
    mf = midi_encode_melody(env.composition)
    midi.write_midifile('out/output.mid', mf)