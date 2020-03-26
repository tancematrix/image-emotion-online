#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.4),
    on Thu Mar 26 12:07:29 2020
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.2.4'
expName = 'image-sentiment-online'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/takeuchi/research/image-sentiment/gaze-and-emotion/online-experiment/image-emotion-online_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', 
    image=None, mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
text = visual.TextStim(win=win, name='text',
    text='画像に感じた感情を選んでください。\n\nhoge hoge hgoe',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp = keyboard.Keyboard()
textGazePoint = visual.TextStim(win=win, name='textGazePoint',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
textQuestionRecog = visual.TextStim(win=win, name='textQuestionRecog',
    text='画像中にあったオブジェクトを選んでください\n\nhoge hoge hoge\nhoge hoge hoge',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
keyQuestionRecog = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "trial"-------
routineTimer.add(8.000000)
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
keyQuestionRecog.keys = []
keyQuestionRecog.rt = []
# keep track of which components have finished
trialComponents = [image, text, key_resp, textGazePoint, textQuestionRecog, keyQuestionRecog]
for thisComponent in trialComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "trial"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = trialClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trialClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image* updates
    if image.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
        # keep track of start time/frame for later
        image.frameNStart = frameN  # exact frame index
        image.tStart = t  # local t and not account for scr refresh
        image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
        image.setAutoDraw(True)
    if image.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            image.tStop = t  # not accounting for scr refresh
            image.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
            image.setAutoDraw(False)
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 2.0-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
            text.setAutoDraw(False)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > key_resp.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            key_resp.tStop = t  # not accounting for scr refresh
            key_resp.frameNStop = frameN  # exact frame index
            win.timeOnFlip(key_resp, 'tStopRefresh')  # time at next scr refresh
            key_resp.status = FINISHED
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['y', 'n', 'left', 'right', 'space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp.keys.append(theseKeys.name)  # storing all keys
            key_resp.rt.append(theseKeys.rt)
            # a response ends the routine
            continueRoutine = False
    
    # *textGazePoint* updates
    if textGazePoint.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textGazePoint.frameNStart = frameN  # exact frame index
        textGazePoint.tStart = t  # local t and not account for scr refresh
        textGazePoint.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textGazePoint, 'tStartRefresh')  # time at next scr refresh
        textGazePoint.setAutoDraw(True)
    if textGazePoint.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > textGazePoint.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            textGazePoint.tStop = t  # not accounting for scr refresh
            textGazePoint.frameNStop = frameN  # exact frame index
            win.timeOnFlip(textGazePoint, 'tStopRefresh')  # time at next scr refresh
            textGazePoint.setAutoDraw(False)
    
    # *textQuestionRecog* updates
    if textQuestionRecog.status == NOT_STARTED and tThisFlip >= 5.0-frameTolerance:
        # keep track of start time/frame for later
        textQuestionRecog.frameNStart = frameN  # exact frame index
        textQuestionRecog.tStart = t  # local t and not account for scr refresh
        textQuestionRecog.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textQuestionRecog, 'tStartRefresh')  # time at next scr refresh
        textQuestionRecog.setAutoDraw(True)
    if textQuestionRecog.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > textQuestionRecog.tStartRefresh + 3.0-frameTolerance:
            # keep track of stop time/frame for later
            textQuestionRecog.tStop = t  # not accounting for scr refresh
            textQuestionRecog.frameNStop = frameN  # exact frame index
            win.timeOnFlip(textQuestionRecog, 'tStopRefresh')  # time at next scr refresh
            textQuestionRecog.setAutoDraw(False)
    
    # *keyQuestionRecog* updates
    waitOnFlip = False
    if keyQuestionRecog.status == NOT_STARTED and tThisFlip >= 5.0-frameTolerance:
        # keep track of start time/frame for later
        keyQuestionRecog.frameNStart = frameN  # exact frame index
        keyQuestionRecog.tStart = t  # local t and not account for scr refresh
        keyQuestionRecog.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keyQuestionRecog, 'tStartRefresh')  # time at next scr refresh
        keyQuestionRecog.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(keyQuestionRecog.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(keyQuestionRecog.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if keyQuestionRecog.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > keyQuestionRecog.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            keyQuestionRecog.tStop = t  # not accounting for scr refresh
            keyQuestionRecog.frameNStop = frameN  # exact frame index
            win.timeOnFlip(keyQuestionRecog, 'tStopRefresh')  # time at next scr refresh
            keyQuestionRecog.status = FINISHED
    if keyQuestionRecog.status == STARTED and not waitOnFlip:
        theseKeys = keyQuestionRecog.getKeys(keyList=['y', 'n', 'left', 'right', 'space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            keyQuestionRecog.keys = theseKeys.name  # just the last key pressed
            keyQuestionRecog.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial"-------
for thisComponent in trialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image.started', image.tStartRefresh)
thisExp.addData('image.stopped', image.tStopRefresh)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('textGazePoint.started', textGazePoint.tStartRefresh)
thisExp.addData('textGazePoint.stopped', textGazePoint.tStopRefresh)
thisExp.addData('textQuestionRecog.started', textQuestionRecog.tStartRefresh)
thisExp.addData('textQuestionRecog.stopped', textQuestionRecog.tStopRefresh)
# check responses
if keyQuestionRecog.keys in ['', [], None]:  # No response was made
    keyQuestionRecog.keys = None
thisExp.addData('keyQuestionRecog.keys',keyQuestionRecog.keys)
if keyQuestionRecog.keys != None:  # we had a response
    thisExp.addData('keyQuestionRecog.rt', keyQuestionRecog.rt)
thisExp.addData('keyQuestionRecog.started', keyQuestionRecog.tStartRefresh)
thisExp.addData('keyQuestionRecog.stopped', keyQuestionRecog.tStopRefresh)
thisExp.nextEntry()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
