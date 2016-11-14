import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-c", "--caonimabi", help="this is helper", action="store_true", default=False)
group = parser.add_mutually_exclusive_group()
group.add_argument("--a001", action="store_false")
print parser.parse_args("--a001 --caonimabi".split())
args = parser.parse_args()
print args
if args.caonimabi:
    print "ai yo wo cao"

print vars(args)