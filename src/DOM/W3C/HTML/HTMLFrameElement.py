#!/usr/bin/env python
from __future__ import with_statement

from HTMLElement import HTMLElement
from attr_property import attr_property

class HTMLFrameElement(HTMLElement):
    frameBorder     = attr_property("frameborder")
    longDesc        = attr_property("longdesc")
    marginHeight    = attr_property("marginheight")
    marginWidth     = attr_property("marginwidth")
    name            = attr_property("name")
    noResize        = attr_property("noresize", bool)
    scrolling       = attr_property("scrolling")
    src             = attr_property("src")

    # Introduced in DOM Level 2
    @property
    def contentDocument(self):
        return self.doc if self.doc else None
