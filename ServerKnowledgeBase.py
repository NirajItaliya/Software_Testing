import os
import os.path
import sys
import time
import logging

from pylstar.LSTAR import LSTAR
from pylstar.ActiveKnowledgeBase import ActiveKnowledgeBase
from pylstar.Letter import Letter, EmptyLetter
from pylstar.Word import Word
from pylstar.eqtests.RandomWalkMethod import RandomWalkMethod
from pylstar.eqtests.WpMethodEQ import WpMethodEQ

from mapper import *

from scapy_iquic_client import QUIC

class QUICServerKnowledgeBase(ActiveKnowledgeBase):
    def __init__(self, server_name, server, timeout=5):
        super(QUICServerKnowledgeBase, self).__init__()
        self._i = 1
        self.timeout = timeout
        self.server_name = server_name
        self.server = server

    def start(self):
        pass

    def stop(self):
        pass

    def start_target(self):
        pass

    def stop_target(self):
        pass

    def submit_word(self, word):
        output_letters = []

        print("-"*100)
        print("query : ",self._i)
        print("-"*100)

        s = QUIC()

        try:
            output_letters = [self._submit_letter(s, letter) for letter in word.letters]
            print("\nInput:- ",word.letters,"\nOutput:- ", output_letters)
        except:
            pass
        finally:
            # s.send(CloseConnectionEvent())
            del s
            # time.sleep(2)
            self._i+=1

        return Word(letters=output_letters)

    def _submit_letter(self, s, letter):
        output_letter = EmptyLetter()
        try:
            to_send = ''.join([symbol for symbol in letter.symbols])
            processed = QuicInputMapper(to_send, s)
            output = QuicOutputMapper(processed)
            output_letter = Letter(output)
        except Exception as e:
            print("error")

        return output_letter
