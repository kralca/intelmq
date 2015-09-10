# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import unittest

import intelmq.lib.test as test
from intelmq.bots.experts.cymru_whois.expert import CymruExpertBot

EXAMPLE_INPUT = {"__type": "Event",
                 "source.ip": "93.184.216.34",  # example.com
                 "time.observation": "2015-01-01T00:00:00+00:00",
                 }
EXAMPLE_OUTPUT = {"__type": "Event",
                  "source.ip": "93.184.216.34",
                  "source.geolocation.cc": "EU",
                  "source.registry": "ripencc",
                  "source.network": "93.184.216.0/24",
                  "source.allocated": "2008-06-02T00:00:00+00:00",
                  "source.asn": 15133,
                  "source.as_name": "EDGECAST - EdgeCast Networks, Inc.,US",
                  "time.observation": "2015-01-01T00:00:00+00:00",
                  }
EXAMPLE_INPUT6 = {"__type": "Event",
                  "destination.ip": "2001:500:88:200::8",  # iana.org
                  "time.observation": "2015-01-01T00:00:00+00:00",
                  }
EXAMPLE_OUTPUT6 = {"__type": "Event",
                   "destination.ip": "2001:500:88:200::8",  # iana.org
                   "destination.registry": "arin",
                   "destination.allocated": "2010-02-18T00:00:00+00:00",
                   "destination.as_name": "ICANN-DC - ICANN,US",
                   "destination.geolocation.cc": "US",
                   "time.observation": "2015-01-01T00:00:00+00:00",
                   "destination.asn": 16876,
                   "destination.network": "2001:500:88::/48",
                   }
UNICODE_INPUT = {"__type": "Event",
                 "destination.ip": "177.81.215.80",  # some brazil IP
                 "time.observation": "2015-01-01T00:00:00+00:00",
                 }
UNICODE_OUTPUT = {"__type": "Event",
                  "destination.ip": "177.81.215.80",  # some brazil IP
                  "time.observation": "2015-01-01T00:00:00+00:00",
                  "destination.registry": "lacnic",
                  "destination.allocated": "2011-08-30T00:00:00+00:00",
                  "destination.as_name": "NET Servi\xe7os de Comunica\xe7\xe3o"
                                         " S.A.,BR",
                  "destination.geolocation.cc": "BR",
                  "destination.asn": 28573,
                  "destination.network": "177.81.0.0/16",
                  }


class TestCymruExpertBot(test.BotTestCase, unittest.TestCase):
    """
    A TestCase for AbusixExpertBot.
    """

    @classmethod
    def set_bot(self):
        self.bot_reference = CymruExpertBot
        self.default_input_message = {'__type': 'Report'}

    def test_ipv4_lookup(self):
        self.input_message = EXAMPLE_INPUT
        self.run_bot()
        self.assertMessageEqual(0, EXAMPLE_OUTPUT)

    def test_ipv6_lookup(self):
        self.input_message = EXAMPLE_INPUT6
        self.run_bot()
        self.assertMessageEqual(0, EXAMPLE_OUTPUT6)

    def test_unicode_as_name(self):
        self.input_message = UNICODE_INPUT
        self.run_bot()
        self.assertMessageEqual(0, UNICODE_OUTPUT)


if __name__ == '__main__':
    unittest.main()