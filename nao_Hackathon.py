#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

"""Example: Use run Method"""

import qi
import argparse
import sys
import time
import almath


def main(session):
    """
    This .
    """
    # Get the services.
    tts_service  = session.service("ALTextToSpeech")
    motion_service  = session.service("ALMotion")
    animation_player_service = session.service("ALAnimationPlayer")

    asr_service = session.service("ALAnimatedSpeech")
    # set the local configuration
    configuration = {"bodyLanguageMode":"contextual"}


    if not motion_service.robotIsWakeUp():
        motion_service.wakeUp()


    # say the text with the local configuration
    asr_service.say("I am Multi-purpose Anthropomorphic Robot for Telepresence Assistance, but you can call me Marta!", configuration)
    #asr_service.say("Hello! ^start(animations/Stand/Gestures/Hey_1) Nice to meet you!")

    time.sleep(2.0)

    asr_service.say("Would you like to play a game? ^start(animations/Stand/Gestures/IDontKnow_1) I Spy?")


    #look around
    names  = ["HeadPitch","HeadYaw"]
    angleLists  = [[-25.0*almath.TO_RAD, 25.0*almath.TO_RAD, -25.0*almath.TO_RAD, 0.0,],
                [45.0*almath.TO_RAD, -45.0*almath.TO_RAD, 0.0]]
    timeLists   = [[1.0, 3.0, 6.0, 8.0], [ 2.0, 4.0, 8.0]]
    isAbsolute  = True
    motion_service.angleInterpolation(names, angleLists, timeLists, isAbsolute)

    time.sleep(2.0)

    #WRONG Answer animation
    asr_service.say("Wrong! ^start(animations/Stand/Gestures/No_3) You are embarrassingly bad at this game")

    time.sleep(2.0)

    #RiGHT Answer animation
    asr_service.say("Alright! ^start(animations/Stand/Gestures/Enthusiastic_5) alright, alright. You got this one!")

    #animation_player_service.run("animations/Stand/Gestures/Hey_6")


    time.sleep(1.0)

    motion_service.rest()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")

    args = parser.parse_args()
    session = qi.Session()
    try:
        session.connect("tcp://" + args.ip + ":" + str(args.port))
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
               "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)
    main(session)
