#  Copyright (c) 2015-2016 by Rocky Bernstein
"""
Python 2.5 bytecode ingestion

This overlaps Python's 2.5's dis module, but it can be run from
Python 3 and other versions of Python. Also, we save token
information for later use in deparsing.
"""

import uncompyle6.ingest.scanner26 as ingest

# bytecode verification, verify(), uses JUMP_OPs from here
from xdis.opcodes import opcode_25
JUMP_OPs = opcode_25.JUMP_OPs

# We base this off of 2.6 instead of the other way around
# because we cleaned things up this way.
# The history is that 2.7 support is the cleanest,
# then from that we got 2.6 and so on.
class Scanner25(ingest.Scanner26):
    def __init__(self, show_asm):
        # There are no differences in initialization between
        # 2.5 and 2.6
        self.opc = opcode_25
        self.opname = opcode_25.opname
        ingest.Scanner26.__init__(self, show_asm)
        self.version = 2.5
        return