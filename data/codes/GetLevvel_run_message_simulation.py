#!/usr/bin/python
# System Importsimport os, sys, json, inspect, uuid, argparse, datetime, logging, copyfrom time import sleep
# Local Importsfrom src.logger             import Loggerfrom src.utils              import *from src.message_simulator  import MessageSimulator

####################################################################### Start Arg Processing:#action              = "Run Message Simulation"parser              = argparse.ArgumentParser(description="Parser for: " + str(action))parser.add_argument('-f', '--simfile', required=True, dest='simfile', help='Run Test Simulation')parser.add_argument('-d', '--debug',    help='Debug Flag')args                = parser.parse_args()
path_to_test        = "./NOTREAL"debug               = True
if args.simfile:    path_to_test    = str(args.simfile)
if args.debug:    debug = True## End Arg Processing######################################################################

if os.path.isfile(path_to_test) == False:    lg("\nERROR: Did not find Simulation File at Path(" + str(path_to_test) + ")\n", 0)    sys.exit(1) 
else:    lg("", 6)    lg("Running Simulation(" + str(path_to_test) + ")", 5)    lg("", 6)
    test_config         = json.loads(open(path_to_test, "r").read())    exit_status         = 1    summary_report      = {}    debug               = False    logger              = None    logger              = Logger("RSM", "/dev/log", logging.DEBUG)    server              = MessageSimulator(test_config, logger, debug)
    not_done            = True while not_done:        still_processing = server.run_states()
 if still_processing:            not_done    = False else:            not_done    = True
 # now done     lg("Done Simulation(" + str(path_to_test) + ")", 6)    lg("", 6)
    sys.exit(exit_status)# end of processing









