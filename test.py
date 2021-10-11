#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
This document contains the object-oriented interface I will use for my testing.
Design is found in docs/test.xml

@author Mason Hicks
Created 10/11
'''

class TestBed:

    tests = None

    def __init__(self, tests=None):
        self.tests = []
        if (tests == None):
            # Nothing
        else if str(type(tests)) == '<class \'list\'>':
            self.add(tests)
        else if str(type(tests)) == '<class \'Test\'>':
            self.add(tests)
        else:
            raise Exception('TestBed accepts a Test object or a list of Test object as parameters!')

    def add(self, tests):
        initialSize = len(self.tests)
        if (str(type(tests)) == 'list'):
            for t in tests:
                try:
                    self.add(t)
                except:
                    # Do nothing
        else if (str(type(tests)) == 'Test'):
            self.tests.append(tests)
        else:
            raise Exception('TestBed#add accepts a TEst object or a list of Test objects as a parameter!')
        currSize = len(self.test)
        return currSize > initialSize

    def run(clear=False):
        if (str(type(clear)) != '<class \'bool\'>'):
            raise Exception('Must pass in a boolean or nothing to TestBed#run.')

        for t in tests:
            try:
                t.run()
                print('{}: Pass'.format(t.name))
            raise:
                print('{}: Fail'.format(t.name))
            if clear:
                tests.remove(t)
