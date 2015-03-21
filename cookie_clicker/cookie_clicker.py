#!/usr/bin/env python
import sys
from runner.runner import CodeJamRunner

def cookie_clicker(C, F, X):
    r = 2.0
    t = 0
    while True:
        t_farm = C/r
        t_final = X/r
        r += F
        if t_final <= t_farm + (X / r):
            break
        t += t_farm
    return t + t_final

class CookieClickerRunner(CodeJamRunner):

    def read_test(self, f):
            value = [float(n) for n in f.readline().split(' ')]
            return {
                'C': value[0], 
                'F': value[1],
                'X': value[2]
                }

    def execute(self, **kwargs):
        return '{0:.7f}'.format(cookie_clicker(**kwargs))


if __name__ == '__main__':
    if len(sys.argv) == 1:
        sys.stderr.write('Use %s <filename>\n' % sys.argv[0])
        sys.exit(1)
    runner = CookieClickerRunner(sys.argv[1])
    runner.print_result()