#!/usr/bin/env python
import sys

'''https://code.google.com/codejam/contest/2974486/dashboard#s=p0'''
from runner.runner import CodeJamRunner

def magic_trick(arr1, ans1, arr2, ans2):
    (r1, r2) = (arr1[ans1 - 1], arr2[ans2 - 1])
    cards = [i for j in r2 for i in r1 if i == j]
    return cards[0] if len(cards) == 1 else "Bad magician!" if len(cards) > 1 else "Volunteer cheated!"


class MagicTrickRunner(CodeJamRunner):

    def read_test(self, f):
            return {
                'ans1': int(f.readline()), 
                'arr1': [[int(i) for i in f.readline().split(' ')] for _ in xrange(4)],
                'ans2': int(f.readline()),
                'arr2': [[int(i) for i in f.readline().split(' ')] for _ in xrange(4)]
                }

    def execute(self, **kwargs):
        return magic_trick(**kwargs)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        sys.stderr.write('Use %s <filename>\n' % sys.argv[0])
        sys.exit(1)
    runner = MagicTrickRunner(sys.argv[1])
    runner.print_result()
