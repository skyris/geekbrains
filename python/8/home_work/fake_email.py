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
    email_sites = ("@armyspy.com", "@cuvox.de", "@dayrep.com", "@einrot.com", "@fleckens.hu",
                   "@gustr.com", "@jourrapide.com", "@rhyta.com", "@superrito.com", "@teleworm.us")
    email_url_template = "http://www.fakemailgenerator.com/#/{}/{}/"

    def get_new_email_address(self):
        base_url = "http://www.fakemailgenerator.com/"
        g = Grab()
        g.setup(connect_timeout=20, timeout=20)
        g.go(base_url)
        if g.response.code == 200:
            email_name = g.doc('//*[@id="home-email"]/@value').text()
            email_site = g.doc('//*[@id="domain"]').text()
            self.email = email_name + email_site
            self.full_http = self.url_template.format(email_name, email_site.strip("@"))
            return self.full_http

    def generate_new_email_address(self):
        new_email_site = random.choice(self.email_sites)

    def check_new_emails(self, url):
        g = Grab()
        g.setup(connect_timeout=20, timeout=20)
        g.go(url)
        if g.response.code == 200:
            print(g.response.body)

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



