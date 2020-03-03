#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import happy

sequences = ["AATAA", "GAA", "TAA", "GCTA", "AGCTA", "AAGAA", "AAATA", "TTATT", "TTGTT", "ATA"]


def score(letA: str, letB: str) -> int:
    return 0


print(happy.needleman_wunsch_alignment("CGGTG", "ATT", gap=-1, scorefct=score))

