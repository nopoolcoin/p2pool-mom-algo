from p2pool.bitcoin import networks
from p2pool.util import math

# CHAIN_LENGTH = number of shares back client keeps
# REAL_CHAIN_LENGTH = maximum number of shares back client uses to compute payout
# REAL_CHAIN_LENGTH must always be <= CHAIN_LENGTH
# REAL_CHAIN_LENGTH must be changed in sync with all other clients
# changes can be done by changing one, then the other

nets = dict(
    memorycoin=math.Object(
        PARENT=networks.nets['nopoolcoin'],
        SHARE_PERIOD=60, # seconds
        CHAIN_LENGTH=24*60, # shares
        REAL_CHAIN_LENGTH=24*60, # shares
        TARGET_LOOKBEHIND=100, # shares
        SPREAD=3, # blocks
        IDENTIFIER='394c395fd32cfba2'.decode('hex'),
        PREFIX='8f75adc343013bbd'.decode('hex'),
        P2P_PORT=7654,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2 - 1, # 1/2 of generated hashes
        PERSIST=True,
        WORKER_PORT=10086,
        BOOTSTRAP_ADDRS='nopoolcoin.com'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool',
        VERSION_CHECK=lambda v: 50700 <= v < 60000 or 60010 <= v < 60100 or 60400 <= v,
        VERSION_WARNING=lambda v: 'Upgrade Memorycoin to >=0.8.5!' if v < 80500 else None,
    ),
    memorycoin_testnet=math.Object(
        PARENT=networks.nets['nopoolcoin_testnet'],
        SHARE_PERIOD=60, # seconds
        CHAIN_LENGTH=24*60, # shares
        REAL_CHAIN_LENGTH=24*60, # shares
        TARGET_LOOKBEHIND=100, # shares
        SPREAD=3, # blocks
        IDENTIFIER='393c395ff32cfba3'.decode('hex'),
        PREFIX='8f75adb343019bbe'.decode('hex'),
        P2P_PORT=17654,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2 - 1, # 1/2 of generated hashes
        PERSIST=True,
        WORKER_PORT=10010,
        BOOTSTRAP_ADDRS='nopoolcoin.com'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool',
        VERSION_CHECK=lambda v: 50700 <= v < 60000 or 60010 <= v < 60100 or 60400 <= v,
        VERSION_WARNING=lambda v: 'Upgrade Memorycoin to >=0.8.5!' if v < 80500 else None,
    ),
)
for net_name, net in nets.iteritems():
    net.NAME = net_name
