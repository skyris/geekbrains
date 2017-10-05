#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Script for creating fake emails and getting emails.
"""

import random
from grab import Grab


__author__ = "Victor Klimov"
__copyright__ = "Creative Commons License"



email = "Grem1962@fleckens.hu"

class FakeEmail:
    def __init__(self):
        self.email_sites = ("@armyspy.com", "@cuvox.de", "@dayrep.com", "@einrot.com", "@fleckens.hu",
                   "@gustr.com", "@jourrapide.com", "@rhyta.com", "@superrito.com", "@teleworm.us")
        self.url_template = "http://www.fakemailgenerator.com/#/{}/{}/"

    def get_new_address(self):
        base_url = "http://www.fakemailgenerator.com/"
        g = Grab()
        g.setup(connect_timeout=20, timeout=20)
        g.go(base_url)
        if g.response.code == 200:
            email_name = g.doc('//*[@id="home-email"]/@value').text()
            email_site = g.doc('//*[@id="domain"]').text()
            self.full_email = email_name, email_site

    def generate_address(self, email_name):
        self.full_email = email_name, random.choice(self.email_sites)

    @property
    def email(self):
        return "{}{}".format(self.full_email[0], self.full_email[1])

    @property
    def email_url(self):
        return self.url_template.format(self.full_email[0], self.full_email[1].strip("@"))

    def check_inbox(self):
        g = Grab()
        g.setup(connect_timeout=20, timeout=20)
        g.go(self.email_url)
        if g.response.code == 200:
            print(g.response.unicode_body())



fake_email = FakeEmail()
fake_email.get_new_address()
fake_email.check_inbox()

"""

Ginfortiect1954@rhyta.com
Proryurs78775@superrito.com
Noths1954@cuvox.de
Sevours43@dayrep.com
Trands53@einrot.com

"http://www.fakemailgenerator.com/#/superrito.com/Proyurs785/"

"http://www.fakemailgenerator.com/#/fleckens.hu/Grem1962/"
"""

# TODO Сделать скрипт создающий фейковый емейл и отслеживающий поступление почты на него



