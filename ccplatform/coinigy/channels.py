# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 10:22:16 2017

@author: paulj
"""

channels = ['TRADE-BTCE--BTC--EUR',
     'ORDER-BTCE--BTC--EUR',
     'TRADE-BTCE--BTC--RUR',
     'ORDER-BTCE--BTC--RUR',
     'TRADE-BTCE--BTC--USD',
     'ORDER-BTCE--BTC--USD',
     'TRADE-BTCE--DSH--BTC',
     'ORDER-BTCE--DSH--BTC',
     'TRADE-BTCE--DSH--ETH',
     'ORDER-BTCE--DSH--ETH',
     'TRADE-BTCE--DSH--EUR',
     'ORDER-BTCE--DSH--EUR',
     'TRADE-BTCE--DSH--LTC',
     'ORDER-BTCE--DSH--LTC',
     'TRADE-BTCE--DSH--RUR',
     'ORDER-BTCE--DSH--RUR',
     'TRADE-BTCE--DSH--USD',
     'ORDER-BTCE--DSH--USD',
     'TRADE-BTCE--ETH--BTC',
     'ORDER-BTCE--ETH--BTC',
     'TRADE-BTCE--ETH--EUR',
     'ORDER-BTCE--ETH--EUR',
     'TRADE-BTCE--ETH--LTC',
     'ORDER-BTCE--ETH--LTC',
     'TRADE-BTCE--ETH--RUR',
     'ORDER-BTCE--ETH--RUR',
     'TRADE-BTCE--ETH--USD',
     'ORDER-BTCE--ETH--USD',
     'TRADE-BTCE--EUR--RUR',
     'ORDER-BTCE--EUR--RUR',
     'TRADE-BTCE--EUR--USD',
     'ORDER-BTCE--EUR--USD',
     'TRADE-BTCE--LTC--BTC',
     'ORDER-BTCE--LTC--BTC',
     'TRADE-BTCE--LTC--EUR',
     'ORDER-BTCE--LTC--EUR',
     'TRADE-BTCE--LTC--RUR',
     'ORDER-BTCE--LTC--RUR',
     'TRADE-BTCE--LTC--USD',
     'ORDER-BTCE--LTC--USD',
     'TRADE-BTCE--NMC--BTC',
     'ORDER-BTCE--NMC--BTC',
     'TRADE-BTCE--NMC--USD',
     'ORDER-BTCE--NMC--USD',
     'TRADE-BTCE--NVC--BTC',
     'ORDER-BTCE--NVC--BTC',
     'TRADE-BTCE--NVC--USD',
     'ORDER-BTCE--NVC--USD',
     'TRADE-BTCE--PPC--BTC',
     'ORDER-BTCE--PPC--BTC',
     'TRADE-BTCE--PPC--USD',
     'ORDER-BTCE--PPC--USD',
     'TRADE-BTCE--USD--RUR',
     'TRADE-BITF--BCC--BTC',
     'ORDER-BITF--BCC--BTC',
     'TRADE-BITF--BCC--USD',
     'ORDER-BITF--BCC--USD',
     'TRADE-BITF--BCU--BTC',
     'ORDER-BITF--BCU--BTC',
     'TRADE-BITF--BCU--USD',
     'ORDER-BITF--BCU--USD',
     'TRADE-BITF--BTC--USD',
     'ORDER-BITF--BTC--USD',
     'TRADE-BITF--DSH--BTC',
     'ORDER-BITF--DSH--BTC',
     'TRADE-BITF--DSH--USD',
     'ORDER-BITF--DSH--USD',
     'TRADE-BITF--EOS--BTC',
     'ORDER-BITF--EOS--BTC',
     'TRADE-BITF--EOS--ETH',
     'ORDER-BITF--EOS--ETH',
     'TRADE-BITF--EOS--USD',
     'ORDER-BITF--EOS--USD',
     'TRADE-BITF--ETC--BTC',
     'ORDER-BITF--ETC--BTC',
     'TRADE-BITF--ETC--USD',
     'ORDER-BITF--ETC--USD',
     'TRADE-BITF--ETH--BTC',
     'ORDER-BITF--ETH--BTC',
     'TRADE-BITF--ETH--USD',
     'ORDER-BITF--ETH--USD',
     'TRADE-BITF--IOT--BTC',
     'ORDER-BITF--IOT--BTC',
     'TRADE-BITF--IOT--ETH',
     'ORDER-BITF--IOT--ETH',
     'TRADE-BITF--IOT--USD',
     'ORDER-BITF--IOT--USD',
     'TRADE-BITF--LTC--BTC',
     'ORDER-BITF--LTC--BTC',
     'TRADE-BITF--LTC--USD',
     'ORDER-BITF--LTC--USD',
     'TRADE-BITF--OMG--BTC',
     'ORDER-BITF--OMG--BTC',
     'TRADE-BITF--OMG--ETH',
     'ORDER-BITF--OMG--ETH',
     'TRADE-BITF--OMG--USD',
     'ORDER-BITF--OMG--USD',
     'TRADE-BITF--RRT--BTC',
     'ORDER-BITF--RRT--BTC',
     'TRADE-BITF--RRT--USD',
     'ORDER-BITF--RRT--USD',
     'TRADE-BITF--SAN--BTC',
     'ORDER-BITF--SAN--BTC',
     'TRADE-BITF--SAN--ETH',
     'ORDER-BITF--SAN--ETH',
     'TRADE-BITF--SAN--USD',
     'ORDER-BITF--SAN--USD',
     'TRADE-BITF--XMR--BTC',
     'ORDER-BITF--XMR--BTC',
     'TRADE-BITF--XMR--USD',
     'ORDER-BITF--XMR--USD',
     'TRADE-BITF--XRP--BTC',
     'ORDER-BITF--XRP--BTC',
     'TRADE-BITF--XRP--USD',
     'ORDER-BITF--XRP--USD',
     'TRADE-BITF--ZEC--BTC',
     'ORDER-BITF--ZEC--BTC',
     'TRADE-BITF--ZEC--USD',
     'ORDER-BITF--ZEC--USD',
     'TRADE-OK--BTC--CNY',
     'ORDER-OK--BTC--CNY',
     'TRADE-OK--BTC--USD',
     'ORDER-OK--BTC--USD',
     'TRADE-OK--LTC--CNY',
     'ORDER-OK--LTC--CNY',
     'TRADE-OK--LTC--USD',
     'ORDER-OK--LTC--USD',
     'TRADE-GDAX--BTC--EUR',
     'ORDER-GDAX--BTC--EUR',
     'TRADE-GDAX--BTC--GBP',
     'ORDER-GDAX--BTC--GBP',
     'TRADE-GDAX--BTC--USD',
     'ORDER-GDAX--BTC--USD',
     'TRADE-GDAX--ETH--BTC',
     'ORDER-GDAX--ETH--BTC',
     'TRADE-GDAX--ETH--EUR',
     'ORDER-GDAX--ETH--EUR',
     'TRADE-GDAX--ETH--USD',
     'ORDER-GDAX--ETH--USD',
     'TRADE-GDAX--LTC--BTC',
     'ORDER-GDAX--LTC--BTC',
     'TRADE-GDAX--LTC--EUR',
     'ORDER-GDAX--LTC--EUR',
     'TRADE-GDAX--LTC--USD',
     'ORDER-GDAX--LTC--USD',
     'TRADE-KRKN--DASH--EUR',
     'ORDER-KRKN--DASH--EUR',
     'TRADE-KRKN--DASH--USD',
     'ORDER-KRKN--DASH--USD',
     'TRADE-KRKN--DASH--XBT',
     'ORDER-KRKN--DASH--XBT',
     'TRADE-KRKN--EOS--ETH',
     'ORDER-KRKN--EOS--ETH',
     'TRADE-KRKN--EOS--EUR',
     'ORDER-KRKN--EOS--EUR',
     'TRADE-KRKN--EOS--USD',
     'ORDER-KRKN--EOS--USD',
     'TRADE-KRKN--EOS--XBT',
     'ORDER-KRKN--EOS--XBT',
     'TRADE-KRKN--ETC--ETH',
     'ORDER-KRKN--ETC--ETH',
     'TRADE-KRKN--ETC--EUR',
     'ORDER-KRKN--ETC--EUR',
     'TRADE-KRKN--ETC--USD',
     'ORDER-KRKN--ETC--USD',
     'TRADE-KRKN--ETC--XBT',
     'ORDER-KRKN--ETC--XBT',
     'TRADE-KRKN--ETH--CAD',
     'ORDER-KRKN--ETH--CAD',
     'TRADE-KRKN--ETH--EUR',
     'ORDER-KRKN--ETH--EUR',
     'TRADE-KRKN--ETH--GBP',
     'ORDER-KRKN--ETH--GBP',
     'TRADE-KRKN--ETH--JPY',
     'ORDER-KRKN--ETH--JPY',
     'TRADE-KRKN--ETH--USD',
     'ORDER-KRKN--ETH--USD',
     'TRADE-KRKN--ETH--XBT',
     'ORDER-KRKN--ETH--XBT',
     'TRADE-KRKN--GNO--ETH',
     'ORDER-KRKN--GNO--ETH',
     'TRADE-KRKN--GNO--EUR',
     'ORDER-KRKN--GNO--EUR',
     'TRADE-KRKN--GNO--USD',
     'ORDER-KRKN--GNO--USD',
     'TRADE-KRKN--GNO--XBT',
     'ORDER-KRKN--GNO--XBT',
     'TRADE-KRKN--ICN--ETH',
     'ORDER-KRKN--ICN--ETH',
     'TRADE-KRKN--ICN--XBT',
     'ORDER-KRKN--ICN--XBT',
     'TRADE-KRKN--LTC--EUR',
     'ORDER-KRKN--LTC--EUR',
     'TRADE-KRKN--LTC--USD',
     'ORDER-KRKN--LTC--USD',
     'TRADE-KRKN--LTC--XBT',
     'ORDER-KRKN--LTC--XBT',
     'TRADE-KRKN--MLN--ETH',
     'ORDER-KRKN--MLN--ETH',
     'TRADE-KRKN--MLN--XBT',
     'ORDER-KRKN--MLN--XBT',
     'TRADE-KRKN--REP--ETH',
     'ORDER-KRKN--REP--ETH',
     'TRADE-KRKN--REP--EUR',
     'ORDER-KRKN--REP--EUR',
     'TRADE-KRKN--REP--USD',
     'ORDER-KRKN--REP--USD',
     'TRADE-KRKN--REP--XBT',
     'ORDER-KRKN--REP--XBT',
     'TRADE-KRKN--USDT--USD',
     'ORDER-KRKN--USDT--USD',
     'TRADE-KRKN--XBT--CAD',
     'ORDER-KRKN--XBT--CAD',
     'TRADE-KRKN--XBT--EUR',
     'ORDER-KRKN--XBT--EUR',
     'TRADE-KRKN--XBT--GBP',
     'ORDER-KRKN--XBT--GBP',
     'TRADE-KRKN--XBT--JPY',
     'ORDER-KRKN--XBT--JPY',
     'TRADE-KRKN--XBT--USD',
     'ORDER-KRKN--XBT--USD',
     'TRADE-KRKN--XDG--XBT',
     'ORDER-KRKN--XDG--XBT',
     'TRADE-KRKN--XLM--EUR',
     'ORDER-KRKN--XLM--EUR',
     'TRADE-KRKN--XLM--USD',
     'ORDER-KRKN--XLM--USD',
     'TRADE-KRKN--XLM--XBT',
     'ORDER-KRKN--XLM--XBT',
     'TRADE-KRKN--XMR--EUR',
     'ORDER-KRKN--XMR--EUR',
     'TRADE-KRKN--XMR--USD',
     'ORDER-KRKN--XMR--USD',
     'TRADE-KRKN--XMR--XBT',
     'ORDER-KRKN--XMR--XBT',
     'TRADE-KRKN--XRP--CAD',
     'ORDER-KRKN--XRP--CAD',
     'TRADE-KRKN--XRP--EUR',
     'ORDER-KRKN--XRP--EUR',
     'TRADE-KRKN--XRP--JPY',
     'ORDER-KRKN--XRP--JPY',
     'TRADE-KRKN--XRP--USD',
     'ORDER-KRKN--XRP--USD',
     'TRADE-KRKN--XRP--XBT',
     'ORDER-KRKN--XRP--XBT',
     'TRADE-KRKN--ZEC--EUR',
     'ORDER-KRKN--ZEC--EUR',
     'TRADE-KRKN--ZEC--USD',
     'ORDER-KRKN--ZEC--USD',
     'TRADE-KRKN--ZEC--XBT',
     'ORDER-KRKN--ZEC--XBT',
     'TRADE-PLNX--BTC--AMP',
     'ORDER-PLNX--BTC--AMP',
     'TRADE-PLNX--BTC--ARDR',
     'ORDER-PLNX--BTC--ARDR',
     'TRADE-PLNX--BTC--BCN',
     'ORDER-PLNX--BTC--BCN',
     'TRADE-PLNX--BTC--BCY',
     'ORDER-PLNX--BTC--BCY',
     'TRADE-PLNX--BTC--BELA',
     'ORDER-PLNX--BTC--BELA',
     'TRADE-PLNX--BTC--BLK',
     'ORDER-PLNX--BTC--BLK',
     'TRADE-PLNX--BTC--BTCD',
     'ORDER-PLNX--BTC--BTCD',
     'TRADE-PLNX--BTC--BTM',
     'ORDER-PLNX--BTC--BTM',
     'TRADE-PLNX--BTC--BTS',
     'ORDER-PLNX--BTC--BTS',
     'TRADE-PLNX--BTC--BURST',
     'ORDER-PLNX--BTC--BURST',
     'TRADE-PLNX--BTC--CLAM',
     'ORDER-PLNX--BTC--CLAM',
     'TRADE-PLNX--BTC--DASH',
     'ORDER-PLNX--BTC--DASH',
     'TRADE-PLNX--BTC--DCR',
     'ORDER-PLNX--BTC--DCR',
     'TRADE-PLNX--BTC--DGB',
     'ORDER-PLNX--BTC--DGB',
     'TRADE-PLNX--BTC--DOGE',
     'ORDER-PLNX--BTC--DOGE',
     'TRADE-PLNX--BTC--EMC2',
     'ORDER-PLNX--BTC--EMC2',
     'TRADE-PLNX--BTC--ETC',
     'ORDER-PLNX--BTC--ETC',
     'TRADE-PLNX--BTC--ETH',
     'ORDER-PLNX--BTC--ETH',
     'TRADE-PLNX--BTC--EXP',
     'ORDER-PLNX--BTC--EXP',
     'TRADE-PLNX--BTC--FCT',
     'ORDER-PLNX--BTC--FCT',
     'TRADE-PLNX--BTC--FLDC',
     'ORDER-PLNX--BTC--FLDC',
     'TRADE-PLNX--BTC--FLO',
     'ORDER-PLNX--BTC--FLO',
     'TRADE-PLNX--BTC--GAME',
     'ORDER-PLNX--BTC--GAME',
     'TRADE-PLNX--BTC--GNO',
     'ORDER-PLNX--BTC--GNO',
     'TRADE-PLNX--BTC--GNT',
     'ORDER-PLNX--BTC--GNT',
     'TRADE-PLNX--BTC--GRC',
     'ORDER-PLNX--BTC--GRC',
     'TRADE-PLNX--BTC--HUC',
     'ORDER-PLNX--BTC--HUC',
     'TRADE-PLNX--BTC--LBC',
     'ORDER-PLNX--BTC--LBC',
     'TRADE-PLNX--BTC--LSK',
     'ORDER-PLNX--BTC--LSK',
     'TRADE-PLNX--BTC--LTC',
     'ORDER-PLNX--BTC--LTC',
     'TRADE-PLNX--BTC--MAID',
     'ORDER-PLNX--BTC--MAID',
     'TRADE-PLNX--BTC--NAUT',
     'ORDER-PLNX--BTC--NAUT',
     'TRADE-PLNX--BTC--NAV',
     'ORDER-PLNX--BTC--NAV',
     'TRADE-PLNX--BTC--NEOS',
     'ORDER-PLNX--BTC--NEOS',
     'TRADE-PLNX--BTC--NMC',
     'ORDER-PLNX--BTC--NMC',
     'TRADE-PLNX--BTC--NOTE',
     'ORDER-PLNX--BTC--NOTE',
     'TRADE-PLNX--BTC--NXC',
     'ORDER-PLNX--BTC--NXC',
     'TRADE-PLNX--BTC--NXT',
     'ORDER-PLNX--BTC--NXT',
     'TRADE-PLNX--BTC--OMNI',
     'ORDER-PLNX--BTC--OMNI',
     'TRADE-PLNX--BTC--PASC',
     'ORDER-PLNX--BTC--PASC',
     'TRADE-PLNX--BTC--PINK',
     'ORDER-PLNX--BTC--PINK',
     'TRADE-PLNX--BTC--POT',
     'ORDER-PLNX--BTC--POT',
     'TRADE-PLNX--BTC--PPC',
     'ORDER-PLNX--BTC--PPC',
     'TRADE-PLNX--BTC--RADS',
     'ORDER-PLNX--BTC--RADS',
     'TRADE-PLNX--BTC--REP',
     'ORDER-PLNX--BTC--REP',
     'TRADE-PLNX--BTC--RIC',
     'ORDER-PLNX--BTC--RIC',
     'TRADE-PLNX--BTC--SBD',
     'ORDER-PLNX--BTC--SBD',
     'TRADE-PLNX--BTC--SC',
     'ORDER-PLNX--BTC--SC',
     'TRADE-PLNX--BTC--SJCX',
     'ORDER-PLNX--BTC--SJCX',
     'TRADE-PLNX--BTC--STEEM',
     'ORDER-PLNX--BTC--STEEM',
     'TRADE-PLNX--BTC--STR',
     'ORDER-PLNX--BTC--STR',
     'TRADE-PLNX--BTC--STRAT',
     'ORDER-PLNX--BTC--STRAT',
     'TRADE-PLNX--BTC--SYS',
     'ORDER-PLNX--BTC--SYS',
     'TRADE-PLNX--BTC--VIA',
     'ORDER-PLNX--BTC--VIA',
     'TRADE-PLNX--BTC--VRC',
     'ORDER-PLNX--BTC--VRC',
     'TRADE-PLNX--BTC--VTC',
     'ORDER-PLNX--BTC--VTC',
     'TRADE-PLNX--BTC--XBC',
     'ORDER-PLNX--BTC--XBC',
     'TRADE-PLNX--BTC--XCP',
     'ORDER-PLNX--BTC--XCP',
     'TRADE-PLNX--BTC--XEM',
     'ORDER-PLNX--BTC--XEM',
     'TRADE-PLNX--BTC--XMR',
     'ORDER-PLNX--BTC--XMR',
     'TRADE-PLNX--BTC--XPM',
     'ORDER-PLNX--BTC--XPM',
     'TRADE-PLNX--BTC--XRP',
     'ORDER-PLNX--BTC--XRP',
     'TRADE-PLNX--BTC--XVC',
     'ORDER-PLNX--BTC--XVC',
     'TRADE-PLNX--BTC--ZEC',
     'ORDER-PLNX--BTC--ZEC',
     'TRADE-PLNX--ETH--ETC',
     'ORDER-PLNX--ETH--ETC',
     'TRADE-PLNX--ETH--GNO',
     'ORDER-PLNX--ETH--GNO',
     'TRADE-PLNX--ETH--GNT',
     'ORDER-PLNX--ETH--GNT',
     'TRADE-PLNX--ETH--LSK',
     'ORDER-PLNX--ETH--LSK',
     'TRADE-PLNX--ETH--REP',
     'ORDER-PLNX--ETH--REP',
     'TRADE-PLNX--ETH--STEEM',
     'ORDER-PLNX--ETH--STEEM',
     'TRADE-PLNX--ETH--ZEC',
     'ORDER-PLNX--ETH--ZEC',
     'TRADE-PLNX--USDT--BTC',
     'ORDER-PLNX--USDT--BTC',
     'TRADE-PLNX--USDT--DASH',
     'ORDER-PLNX--USDT--DASH',
     'TRADE-PLNX--USDT--ETC',
     'ORDER-PLNX--USDT--ETC',
     'TRADE-PLNX--USDT--ETH',
     'ORDER-PLNX--USDT--ETH',
     'TRADE-PLNX--USDT--LTC',
     'ORDER-PLNX--USDT--LTC',
     'TRADE-PLNX--USDT--NXT',
     'ORDER-PLNX--USDT--NXT',
     'TRADE-PLNX--USDT--REP',
     'ORDER-PLNX--USDT--REP',
     'TRADE-PLNX--USDT--STR',
     'ORDER-PLNX--USDT--STR',
     'TRADE-PLNX--USDT--XMR',
     'ORDER-PLNX--USDT--XMR',
     'TRADE-PLNX--USDT--XRP',
     'ORDER-PLNX--USDT--XRP',
     'TRADE-PLNX--USDT--ZEC',
     'ORDER-PLNX--USDT--ZEC',
     'TRADE-PLNX--XMR--BCN',
     'ORDER-PLNX--XMR--BCN',
     'TRADE-PLNX--XMR--BLK',
     'ORDER-PLNX--XMR--BLK',
     'TRADE-PLNX--XMR--BTCD',
     'ORDER-PLNX--XMR--BTCD',
     'TRADE-PLNX--XMR--DASH',
     'ORDER-PLNX--XMR--DASH',
     'TRADE-PLNX--XMR--LTC',
     'ORDER-PLNX--XMR--LTC',
     'TRADE-PLNX--XMR--MAID',
     'ORDER-PLNX--XMR--MAID',
     'TRADE-PLNX--XMR--NXT',
     'ORDER-PLNX--XMR--NXT',
     'TRADE-PLNX--XMR--ZEC',
     'ORDER-PLNX--XMR--ZEC',
     'TRADE-BTRX--1ST--BTC',
     'ORDER-BTRX--1ST--BTC',
     'TRADE-BTRX--1ST--ETH',
     'ORDER-BTRX--1ST--ETH',
     'TRADE-BTRX--2GIVE--BTC',
     'ORDER-BTRX--2GIVE--BTC',
     'TRADE-BTRX--ABY--BTC',
     'ORDER-BTRX--ABY--BTC',
     'TRADE-BTRX--ADT--BTC',
     'ORDER-BTRX--ADT--BTC',
     'TRADE-BTRX--ADT--ETH',
     'ORDER-BTRX--ADT--ETH',
     'TRADE-BTRX--ADX--BTC',
     'ORDER-BTRX--ADX--BTC',
     'TRADE-BTRX--ADX--ETH',
     'ORDER-BTRX--ADX--ETH',
     'TRADE-BTRX--AEON--BTC',
     'ORDER-BTRX--AEON--BTC',
     'TRADE-BTRX--AGRS--BTC',
     'ORDER-BTRX--AGRS--BTC',
     'TRADE-BTRX--AMP--BTC',
     'ORDER-BTRX--AMP--BTC',
     'TRADE-BTRX--ANS--BTC',
     'ORDER-BTRX--ANS--BTC',
     'TRADE-BTRX--ANS--ETH',
     'ORDER-BTRX--ANS--ETH',
     'TRADE-BTRX--ANT--BTC',
     'ORDER-BTRX--ANT--BTC',
     'TRADE-BTRX--ANT--ETH',
     'ORDER-BTRX--ANT--ETH',
     'TRADE-BTRX--APX--BTC',
     'ORDER-BTRX--APX--BTC',
     'TRADE-BTRX--ARDR--BTC',
     'ORDER-BTRX--ARDR--BTC',
     'TRADE-BTRX--ARK--BTC',
     'ORDER-BTRX--ARK--BTC',
     'TRADE-BTRX--AUR--BTC',
     'ORDER-BTRX--AUR--BTC',
     'TRADE-BTRX--BAT--BTC',
     'ORDER-BTRX--BAT--BTC',
     'TRADE-BTRX--BAT--ETH',
     'ORDER-BTRX--BAT--ETH',
     'TRADE-BTRX--BAY--BTC',
     'ORDER-BTRX--BAY--BTC',
     'TRADE-BTRX--BCY--BTC',
     'ORDER-BTRX--BCY--BTC',
     'TRADE-BTRX--BITB--BTC',
     'ORDER-BTRX--BITB--BTC',
     'TRADE-BTRX--BLITZ--BTC',
     'ORDER-BTRX--BLITZ--BTC',
     'TRADE-BTRX--BLK--BTC',
     'ORDER-BTRX--BLK--BTC',
     'TRADE-BTRX--BLOCK--BTC',
     'ORDER-BTRX--BLOCK--BTC',
     'TRADE-BTRX--BNT--BTC',
     'ORDER-BTRX--BNT--BTC',
     'TRADE-BTRX--BNT--ETH',
     'ORDER-BTRX--BNT--ETH',
     'TRADE-BTRX--BRK--BTC',
     'ORDER-BTRX--BRK--BTC',
     'TRADE-BTRX--BRX--BTC',
     'ORDER-BTRX--BRX--BTC',
     'TRADE-BTRX--BSD--BTC',
     'ORDER-BTRX--BSD--BTC',
     'TRADE-BTRX--BTA--BTC',
     'ORDER-BTRX--BTA--BTC',
     'TRADE-BTRX--BTC--BITCNY',
     'ORDER-BTRX--BTC--BITCNY',
     'TRADE-BTRX--BTC--USDT',
     'ORDER-BTRX--BTC--USDT',
     'TRADE-BTRX--BTCD--BTC',
     'ORDER-BTRX--BTCD--BTC',
     'TRADE-BTRX--BTS--BTC',
     'ORDER-BTRX--BTS--BTC',
     'TRADE-BTRX--BURST--BTC',
     'ORDER-BTRX--BURST--BTC',
     'TRADE-BTRX--BYC--BTC',
     'ORDER-BTRX--BYC--BTC',
     'TRADE-BTRX--CANN--BTC',
     'ORDER-BTRX--CANN--BTC',
     'TRADE-BTRX--CFI--BTC',
     'ORDER-BTRX--CFI--BTC',
     'TRADE-BTRX--CFI--ETH',
     'ORDER-BTRX--CFI--ETH',
     'TRADE-BTRX--CLAM--BTC',
     'ORDER-BTRX--CLAM--BTC',
     'TRADE-BTRX--CLOAK--BTC',
     'ORDER-BTRX--CLOAK--BTC',
     'TRADE-BTRX--CLUB--BTC',
     'ORDER-BTRX--CLUB--BTC',
     'TRADE-BTRX--COVAL--BTC',
     'ORDER-BTRX--COVAL--BTC',
     'TRADE-BTRX--CPC--BTC',
     'ORDER-BTRX--CPC--BTC',
     'TRADE-BTRX--CRB--BTC',
     'ORDER-BTRX--CRB--BTC',
     'TRADE-BTRX--CRB--ETH',
     'ORDER-BTRX--CRB--ETH',
     'TRADE-BTRX--CRW--BTC',
     'ORDER-BTRX--CRW--BTC',
     'TRADE-BTRX--CURE--BTC',
     'ORDER-BTRX--CURE--BTC',
     'TRADE-BTRX--CVC--BTC',
     'ORDER-BTRX--CVC--BTC',
     'TRADE-BTRX--CVC--ETH',
     'ORDER-BTRX--CVC--ETH',
     'TRADE-BTRX--DAR--BTC',
     'ORDER-BTRX--DAR--BTC',
     'TRADE-BTRX--DASH--BTC',
     'ORDER-BTRX--DASH--BTC',
     'TRADE-BTRX--DASH--ETH',
     'ORDER-BTRX--DASH--ETH',
     'TRADE-BTRX--DASH--USDT',
     'ORDER-BTRX--DASH--USDT',
     'TRADE-BTRX--DCR--BTC',
     'ORDER-BTRX--DCR--BTC',
     'TRADE-BTRX--DCT--BTC',
     'ORDER-BTRX--DCT--BTC',
     'TRADE-BTRX--DGB--BTC',
     'ORDER-BTRX--DGB--BTC',
     'TRADE-BTRX--DGD--BTC',
     'ORDER-BTRX--DGD--BTC',
     'TRADE-BTRX--DGD--ETH',
     'ORDER-BTRX--DGD--ETH',
     'TRADE-BTRX--DMD--BTC',
     'ORDER-BTRX--DMD--BTC',
     'TRADE-BTRX--DOGE--BTC',
     'ORDER-BTRX--DOGE--BTC',
     'TRADE-BTRX--DOPE--BTC',
     'ORDER-BTRX--DOPE--BTC',
     'TRADE-BTRX--DRACO--BTC',
     'ORDER-BTRX--DRACO--BTC',
     'TRADE-BTRX--DTB--BTC',
     'ORDER-BTRX--DTB--BTC',
     'TRADE-BTRX--DYN--BTC',
     'ORDER-BTRX--DYN--BTC',
     'TRADE-BTRX--EBST--BTC',
     'ORDER-BTRX--EBST--BTC',
     'TRADE-BTRX--EDG--BTC',
     'ORDER-BTRX--EDG--BTC',
     'TRADE-BTRX--EFL--BTC',
     'ORDER-BTRX--EFL--BTC',
     'TRADE-BTRX--EGC--BTC',
     'ORDER-BTRX--EGC--BTC',
     'TRADE-BTRX--EMC--BTC',
     'ORDER-BTRX--EMC--BTC',
     'TRADE-BTRX--EMC2--BTC',
     'ORDER-BTRX--EMC2--BTC',
     'TRADE-BTRX--ENRG--BTC',
     'ORDER-BTRX--ENRG--BTC',
     'TRADE-BTRX--ERC--BTC',
     'ORDER-BTRX--ERC--BTC',
     'TRADE-BTRX--ETC--BTC',
     'ORDER-BTRX--ETC--BTC',
     'TRADE-BTRX--ETC--ETH',
     'ORDER-BTRX--ETC--ETH',
     'TRADE-BTRX--ETC--USDT',
     'ORDER-BTRX--ETC--USDT',
     'TRADE-BTRX--ETH--BTC',
     'ORDER-BTRX--ETH--BTC',
     'TRADE-BTRX--ETH--USDT',
     'ORDER-BTRX--ETH--USDT',
     'TRADE-BTRX--EXCL--BTC',
     'ORDER-BTRX--EXCL--BTC',
     'TRADE-BTRX--EXP--BTC',
     'ORDER-BTRX--EXP--BTC',
     'TRADE-BTRX--FAIR--BTC',
     'ORDER-BTRX--FAIR--BTC',
     'TRADE-BTRX--FCT--BTC',
     'ORDER-BTRX--FCT--BTC',
     'TRADE-BTRX--FLDC--BTC',
     'ORDER-BTRX--FLDC--BTC',
     'TRADE-BTRX--FLO--BTC',
     'ORDER-BTRX--FLO--BTC',
     'TRADE-BTRX--FTC--BTC',
     'ORDER-BTRX--FTC--BTC',
     'TRADE-BTRX--FUN--BTC',
     'ORDER-BTRX--FUN--BTC',
     'TRADE-BTRX--FUN--ETH',
     'ORDER-BTRX--FUN--ETH',
     'TRADE-BTRX--GAM--BTC',
     'ORDER-BTRX--GAM--BTC',
     'TRADE-BTRX--GAME--BTC',
     'ORDER-BTRX--GAME--BTC',
     'TRADE-BTRX--GBG--BTC',
     'ORDER-BTRX--GBG--BTC',
     'TRADE-BTRX--GBYTE--BTC',
     'ORDER-BTRX--GBYTE--BTC',
     'TRADE-BTRX--GCR--BTC',
     'ORDER-BTRX--GCR--BTC',
     'TRADE-BTRX--GEO--BTC',
     'ORDER-BTRX--GEO--BTC',
     'TRADE-BTRX--GLD--BTC',
     'ORDER-BTRX--GLD--BTC',
     'TRADE-BTRX--GNO--BTC',
     'ORDER-BTRX--GNO--BTC',
     'TRADE-BTRX--GNO--ETH',
     'ORDER-BTRX--GNO--ETH',
     'TRADE-BTRX--GNT--BTC',
     'ORDER-BTRX--GNT--BTC',
     'TRADE-BTRX--GNT--ETH',
     'ORDER-BTRX--GNT--ETH',
     'TRADE-BTRX--GOLOS--BTC',
     'ORDER-BTRX--GOLOS--BTC',
     'TRADE-BTRX--GRC--BTC',
     'ORDER-BTRX--GRC--BTC',
     'TRADE-BTRX--GRS--BTC',
     'ORDER-BTRX--GRS--BTC',
     'TRADE-BTRX--GUP--BTC',
     'ORDER-BTRX--GUP--BTC',
     'TRADE-BTRX--GUP--ETH',
     'ORDER-BTRX--GUP--ETH',
     'TRADE-BTRX--HKG--BTC',
     'ORDER-BTRX--HKG--BTC',
     'TRADE-BTRX--HMQ--BTC',
     'ORDER-BTRX--HMQ--BTC',
     'TRADE-BTRX--HMQ--ETH',
     'ORDER-BTRX--HMQ--ETH',
     'TRADE-BTRX--INCNT--BTC',
     'ORDER-BTRX--INCNT--BTC',
     'TRADE-BTRX--INFX--BTC',
     'ORDER-BTRX--INFX--BTC',
     'TRADE-BTRX--IOC--BTC',
     'ORDER-BTRX--IOC--BTC',
     'TRADE-BTRX--ION--BTC',
     'ORDER-BTRX--ION--BTC',
     'TRADE-BTRX--IOP--BTC',
     'ORDER-BTRX--IOP--BTC',
     'TRADE-BTRX--KMD--BTC',
     'ORDER-BTRX--KMD--BTC',
     'TRADE-BTRX--KORE--BTC',
     'ORDER-BTRX--KORE--BTC',
     'TRADE-BTRX--LBC--BTC',
     'ORDER-BTRX--LBC--BTC',
     'TRADE-BTRX--LGD--BTC',
     'ORDER-BTRX--LGD--BTC',
     'TRADE-BTRX--LGD--ETH',
     'ORDER-BTRX--LGD--ETH',
     'TRADE-BTRX--LMC--BTC',
     'ORDER-BTRX--LMC--BTC',
     'TRADE-BTRX--LSK--BTC',
     'ORDER-BTRX--LSK--BTC',
     'TRADE-BTRX--LTC--BTC',
     'ORDER-BTRX--LTC--BTC',
     'TRADE-BTRX--LTC--ETH',
     'ORDER-BTRX--LTC--ETH',
     'TRADE-BTRX--LTC--USDT',
     'ORDER-BTRX--LTC--USDT',
     'TRADE-BTRX--LUN--BTC',
     'ORDER-BTRX--LUN--BTC',
     'TRADE-BTRX--LUN--ETH',
     'ORDER-BTRX--LUN--ETH',
     'TRADE-BTRX--MAID--BTC',
     'ORDER-BTRX--MAID--BTC',
     'TRADE-BTRX--MCO--BTC',
     'ORDER-BTRX--MCO--BTC',
     'TRADE-BTRX--MCO--ETH',
     'ORDER-BTRX--MCO--ETH',
     'TRADE-BTRX--MEME--BTC',
     'ORDER-BTRX--MEME--BTC',
     'TRADE-BTRX--MLN--BTC',
     'ORDER-BTRX--MLN--BTC',
     'TRADE-BTRX--MONA--BTC',
     'ORDER-BTRX--MONA--BTC',
     'TRADE-BTRX--MTL--BTC',
     'ORDER-BTRX--MTL--BTC',
     'TRADE-BTRX--MTL--ETH',
     'ORDER-BTRX--MTL--ETH',
     'TRADE-BTRX--MUE--BTC',
     'ORDER-BTRX--MUE--BTC',
     'TRADE-BTRX--MUSIC--BTC',
     'ORDER-BTRX--MUSIC--BTC',
     'TRADE-BTRX--MYR--BTC',
     'ORDER-BTRX--MYR--BTC',
     'TRADE-BTRX--MYST--BTC',
     'ORDER-BTRX--MYST--BTC',
     'TRADE-BTRX--MYST--ETH',
     'ORDER-BTRX--MYST--ETH',
     'TRADE-BTRX--NAUT--BTC',
     'ORDER-BTRX--NAUT--BTC',
     'TRADE-BTRX--NAV--BTC',
     'ORDER-BTRX--NAV--BTC',
     'TRADE-BTRX--NBT--BTC',
     'ORDER-BTRX--NBT--BTC',
     'TRADE-BTRX--NEOS--BTC',
     'ORDER-BTRX--NEOS--BTC',
     'TRADE-BTRX--NLG--BTC',
     'ORDER-BTRX--NLG--BTC',
     'TRADE-BTRX--NMR--BTC',
     'ORDER-BTRX--NMR--BTC',
     'TRADE-BTRX--NMR--ETH',
     'ORDER-BTRX--NMR--ETH',
     'TRADE-BTRX--NXC--BTC',
     'ORDER-BTRX--NXC--BTC',
     'TRADE-BTRX--NXS--BTC',
     'ORDER-BTRX--NXS--BTC',
     'TRADE-BTRX--NXT--BTC',
     'ORDER-BTRX--NXT--BTC',
     'TRADE-BTRX--OK--BTC',
     'ORDER-BTRX--OK--BTC',
     'TRADE-BTRX--OMG--BTC',
     'ORDER-BTRX--OMG--BTC',
     'TRADE-BTRX--OMG--ETH',
     'ORDER-BTRX--OMG--ETH',
     'TRADE-BTRX--OMNI--BTC',
     'ORDER-BTRX--OMNI--BTC',
     'TRADE-BTRX--PART--BTC',
     'ORDER-BTRX--PART--BTC',
     'TRADE-BTRX--PAY--BTC',
     'ORDER-BTRX--PAY--BTC',
     'TRADE-BTRX--PAY--ETH',
     'ORDER-BTRX--PAY--ETH',
     'TRADE-BTRX--PDC--BTC',
     'ORDER-BTRX--PDC--BTC',
     'TRADE-BTRX--PINK--BTC',
     'ORDER-BTRX--PINK--BTC',
     'TRADE-BTRX--PIVX--BTC',
     'ORDER-BTRX--PIVX--BTC',
     'TRADE-BTRX--PKB--BTC',
     'ORDER-BTRX--PKB--BTC',
     'TRADE-BTRX--POT--BTC',
     'ORDER-BTRX--POT--BTC',
     'TRADE-BTRX--PPC--BTC',
     'ORDER-BTRX--PPC--BTC',
     'TRADE-BTRX--PTC--BTC',
     'ORDER-BTRX--PTC--BTC',
     'TRADE-BTRX--PTOY--BTC',
     'ORDER-BTRX--PTOY--BTC',
     'TRADE-BTRX--PTOY--ETH',
     'ORDER-BTRX--PTOY--ETH',
     'TRADE-BTRX--QRL--BTC',
     'ORDER-BTRX--QRL--BTC',
     'TRADE-BTRX--QRL--ETH',
     'ORDER-BTRX--QRL--ETH',
     'TRADE-BTRX--QTUM--BTC',
     'ORDER-BTRX--QTUM--BTC',
     'TRADE-BTRX--QTUM--ETH',
     'ORDER-BTRX--QTUM--ETH',
     'TRADE-BTRX--QWARK--BTC',
     'ORDER-BTRX--QWARK--BTC',
     'TRADE-BTRX--RADS--BTC',
     'ORDER-BTRX--RADS--BTC',
     'TRADE-BTRX--RBY--BTC',
     'ORDER-BTRX--RBY--BTC',
     'TRADE-BTRX--RDD--BTC',
     'ORDER-BTRX--RDD--BTC',
     'TRADE-BTRX--REP--BTC',
     'ORDER-BTRX--REP--BTC',
     'TRADE-BTRX--REP--ETH',
     'ORDER-BTRX--REP--ETH',
     'TRADE-BTRX--RISE--BTC',
     'ORDER-BTRX--RISE--BTC',
     'TRADE-BTRX--RLC--BTC',
     'ORDER-BTRX--RLC--BTC',
     'TRADE-BTRX--RLC--ETH',
     'ORDER-BTRX--RLC--ETH',
     'TRADE-BTRX--SBD--BTC',
     'ORDER-BTRX--SBD--BTC',
     'TRADE-BTRX--SC--BTC',
     'ORDER-BTRX--SC--BTC',
     'TRADE-BTRX--SC--ETH',
     'ORDER-BTRX--SC--ETH',
     'TRADE-BTRX--SEC--BTC',
     'ORDER-BTRX--SEC--BTC',
     'TRADE-BTRX--SEQ--BTC',
     'ORDER-BTRX--SEQ--BTC',
     'TRADE-BTRX--SHIFT--BTC',
     'ORDER-BTRX--SHIFT--BTC',
     'TRADE-BTRX--SIB--BTC',
     'ORDER-BTRX--SIB--BTC',
     'TRADE-BTRX--SLR--BTC',
     'ORDER-BTRX--SLR--BTC',
     'TRADE-BTRX--SLS--BTC',
     'ORDER-BTRX--SLS--BTC',
     'TRADE-BTRX--SNGLS--BTC',
     'ORDER-BTRX--SNGLS--BTC',
     'TRADE-BTRX--SNGLS--ETH',
     'ORDER-BTRX--SNGLS--ETH',
     'TRADE-BTRX--SNRG--BTC',
     'ORDER-BTRX--SNRG--BTC',
     'TRADE-BTRX--SNT--BTC',
     'ORDER-BTRX--SNT--BTC',
     'TRADE-BTRX--SNT--ETH',
     'ORDER-BTRX--SNT--ETH',
     'TRADE-BTRX--SPHR--BTC',
     'ORDER-BTRX--SPHR--BTC',
     'TRADE-BTRX--SPR--BTC',
     'ORDER-BTRX--SPR--BTC',
     'TRADE-BTRX--START--BTC',
     'ORDER-BTRX--START--BTC',
     'TRADE-BTRX--STEEM--BTC',
     'ORDER-BTRX--STEEM--BTC',
     'TRADE-BTRX--STORJ--BTC',
     'ORDER-BTRX--STORJ--BTC',
     'TRADE-BTRX--STORJ--ETH',
     'ORDER-BTRX--STORJ--ETH',
     'TRADE-BTRX--STRAT--BTC',
     'ORDER-BTRX--STRAT--BTC',
     'TRADE-BTRX--SWIFT--BTC',
     'ORDER-BTRX--SWIFT--BTC',
     'TRADE-BTRX--SWT--BTC',
     'ORDER-BTRX--SWT--BTC',
     'TRADE-BTRX--SYNX--BTC',
     'ORDER-BTRX--SYNX--BTC',
     'TRADE-BTRX--SYS--BTC',
     'ORDER-BTRX--SYS--BTC',
     'TRADE-BTRX--THC--BTC',
     'ORDER-BTRX--THC--BTC',
     'TRADE-BTRX--TIME--BTC',
     'ORDER-BTRX--TIME--BTC',
     'TRADE-BTRX--TIME--ETH',
     'ORDER-BTRX--TIME--ETH',
     'TRADE-BTRX--TKN--BTC',
     'ORDER-BTRX--TKN--BTC',
     'TRADE-BTRX--TKN--ETH',
     'ORDER-BTRX--TKN--ETH',
     'TRADE-BTRX--TKS--BTC',
     'ORDER-BTRX--TKS--BTC',
     'TRADE-BTRX--TRIG--BTC',
     'ORDER-BTRX--TRIG--BTC',
     'TRADE-BTRX--TRST--BTC',
     'ORDER-BTRX--TRST--BTC',
     'TRADE-BTRX--TRST--ETH',
     'ORDER-BTRX--TRST--ETH',
     'TRADE-BTRX--TRUST--BTC',
     'ORDER-BTRX--TRUST--BTC',
     'TRADE-BTRX--TX--BTC',
     'ORDER-BTRX--TX--BTC',
     'TRADE-BTRX--UBQ--BTC',
     'ORDER-BTRX--UBQ--BTC',
     'TRADE-BTRX--UNB--BTC',
     'ORDER-BTRX--UNB--BTC',
     'TRADE-BTRX--UNO--BTC',
     'ORDER-BTRX--UNO--BTC',
     'TRADE-BTRX--VIA--BTC',
     'ORDER-BTRX--VIA--BTC',
     'TRADE-BTRX--VOX--BTC',
     'ORDER-BTRX--VOX--BTC',
     'TRADE-BTRX--VRC--BTC',
     'ORDER-BTRX--VRC--BTC',
     'TRADE-BTRX--VRM--BTC',
     'ORDER-BTRX--VRM--BTC',
     'TRADE-BTRX--VTC--BTC',
     'ORDER-BTRX--VTC--BTC',
     'TRADE-BTRX--VTR--BTC',
     'ORDER-BTRX--VTR--BTC',
     'TRADE-BTRX--WAVES--BTC',
     'ORDER-BTRX--WAVES--BTC',
     'TRADE-BTRX--WINGS--BTC',
     'ORDER-BTRX--WINGS--BTC',
     'TRADE-BTRX--WINGS--ETH',
     'ORDER-BTRX--WINGS--ETH',
     'TRADE-BTRX--XAUR--BTC',
     'ORDER-BTRX--XAUR--BTC',
     'TRADE-BTRX--XBB--BTC',
     'ORDER-BTRX--XBB--BTC',
     'TRADE-BTRX--XCP--BTC',
     'ORDER-BTRX--XCP--BTC',
     'TRADE-BTRX--XDN--BTC',
     'ORDER-BTRX--XDN--BTC',
     'TRADE-BTRX--XEL--BTC',
     'ORDER-BTRX--XEL--BTC',
     'TRADE-BTRX--XEL--ETH',
     'ORDER-BTRX--XEL--ETH',
     'TRADE-BTRX--XEM--BTC',
     'ORDER-BTRX--XEM--BTC',
     'TRADE-BTRX--XEM--ETH',
     'ORDER-BTRX--XEM--ETH',
     'TRADE-BTRX--XLM--BTC',
     'ORDER-BTRX--XLM--BTC',
     'TRADE-BTRX--XLM--ETH',
     'ORDER-BTRX--XLM--ETH',
     'TRADE-BTRX--XMG--BTC',
     'ORDER-BTRX--XMG--BTC',
     'TRADE-BTRX--XMR--BTC',
     'ORDER-BTRX--XMR--BTC',
     'TRADE-BTRX--XMR--ETH',
     'ORDER-BTRX--XMR--ETH',
     'TRADE-BTRX--XMR--USDT',
     'ORDER-BTRX--XMR--USDT',
     'TRADE-BTRX--XRP--BTC',
     'ORDER-BTRX--XRP--BTC',
     'TRADE-BTRX--XRP--ETH',
     'ORDER-BTRX--XRP--ETH',
     'TRADE-BTRX--XRP--USDT',
     'ORDER-BTRX--XRP--USDT',
     'TRADE-BTRX--XST--BTC',
     'ORDER-BTRX--XST--BTC',
     'TRADE-BTRX--XVC--BTC',
     'ORDER-BTRX--XVC--BTC',
     'TRADE-BTRX--XVG--BTC',
     'ORDER-BTRX--XVG--BTC',
     'TRADE-BTRX--XWC--BTC',
     'ORDER-BTRX--XWC--BTC',
     'TRADE-BTRX--XZC--BTC',
     'ORDER-BTRX--XZC--BTC',
     'TRADE-BTRX--ZCL--BTC',
     'ORDER-BTRX--ZCL--BTC',
     'TRADE-BTRX--ZEC--BTC',
     'ORDER-BTRX--ZEC--BTC',
     'TRADE-BTRX--ZEC--ETH',
     'ORDER-BTRX--ZEC--ETH',
     'TRADE-BTRX--ZEC--USDT',
     'ORDER-BTRX--ZEC--USDT',
     'TRADE-BTRX--ZEN--BTC',
     'ORDER-BTRX--ZEN--BTC',
     'TRADE-HUOB--BTC--CNY',
     'ORDER-HUOB--BTC--CNY',
     'TRADE-HUOB--BTC--USD',
     'ORDER-HUOB--BTC--USD',
     'TRADE-HUOB--LTC--CNY',
     'ORDER-HUOB--LTC--CNY',
]