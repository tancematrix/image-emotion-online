/***************************** 
 * Image-Emotion-Online Test *
 *****************************/

// init psychoJS:
var psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0, 0, 0]),
  units: 'height',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'image-emotion-online';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'session': '001'};

// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin, trialsLoopScheduler);
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({expName, expInfo});

var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '3.2.4';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0/Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0/60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}

var trialClock;
var image;
var textQuestionEmo;
var key_resp;
var textGazePoint;
var textQuestionRecog;
var keyQuestionRecog;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.5, 0.5],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  textQuestionEmo = new visual.TextStim({
    win: psychoJS.window,
    name: 'textQuestionEmo',
    text: '画像に感じた感情を選んでください。\n\nhoge hoge hgoe',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  key_resp = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  textGazePoint = new visual.TextStim({
    win: psychoJS.window,
    name: 'textGazePoint',
    text: '+',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  textQuestionRecog = new visual.TextStim({
    win: psychoJS.window,
    name: 'textQuestionRecog',
    text: '画像中にあったオブジェクトを選んでください\n\nhoge hoge hoge\nhoge hoge hoge',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  keyQuestionRecog = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}

var trials;
var currentLoop;
var trialIterator;
function trialsLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 5, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'trials'});
  psychoJS.experiment.addLoop(trials); // add the loop to the experiment
  currentLoop = trials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trialIterator = trials[Symbol.iterator]();
  while(true) {
    let result = trialIterator.next();
    if (result.done);
      break;
    let thisTrial = result.value;
    thisScheduler.add(importConditions(trials));
    thisScheduler.add(trialRoutineBegin);
    thisScheduler.add(trialRoutineEachFrame);
    thisScheduler.add(trialRoutineEnd);
    thisScheduler.add(endLoopIteration({thisScheduler, isTrials : true}));
  }

  return Scheduler.Event.NEXT;
}


function trialsLoopEnd() {
  psychoJS.experiment.removeLoop(trials);

  return Scheduler.Event.NEXT;
}

var t;
var frameN;
var trialComponents;
function trialRoutineBegin() {
  //------Prepare to start Routine 'trial'-------
  t = 0;
  trialClock.reset(); // clock
  frameN = -1;
  routineTimer.add(8.000000);
  // update component parameters for each repeat
  image.setImage('../small_samples/');
  key_resp.keys = undefined;
  key_resp.rt = undefined;
  keyQuestionRecog.keys = undefined;
  keyQuestionRecog.rt = undefined;
  // keep track of which components have finished
  trialComponents = [];
  trialComponents.push(image);
  trialComponents.push(textQuestionEmo);
  trialComponents.push(key_resp);
  trialComponents.push(textGazePoint);
  trialComponents.push(textQuestionRecog);
  trialComponents.push(keyQuestionRecog);
  
  trialComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}

var frameRemains;
var continueRoutine;
function trialRoutineEachFrame() {
  //------Loop for each frame of Routine 'trial'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = trialClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *image* updates
  if (t >= 1.0 && image.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    image.tStart = t;  // (not accounting for frame time here)
    image.frameNStart = frameN;  // exact frame index
    image.setAutoDraw(true);
  }

  frameRemains = 1.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (image.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    image.setAutoDraw(false);
  }
  
  // *textQuestionEmo* updates
  if (t >= 3.0 && textQuestionEmo.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    textQuestionEmo.tStart = t;  // (not accounting for frame time here)
    textQuestionEmo.frameNStart = frameN;  // exact frame index
    textQuestionEmo.setAutoDraw(true);
  }

  frameRemains = 3.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (textQuestionEmo.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    textQuestionEmo.setAutoDraw(false);
  }
  
  // *key_resp* updates
  if (t >= 3.0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    key_resp.tStart = t;  // (not accounting for frame time here)
    key_resp.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
  }

  frameRemains = 3.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (key_resp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    key_resp.status = PsychoJS.Status.FINISHED;
  }

  if (key_resp.status === PsychoJS.Status.STARTED) {
    let theseKeys = key_resp.getKeys({keyList: ['y', 'n', 'left', 'right', 'space'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      key_resp.keys = [].concat(key_resp.keys, theseKeys[0].name).filter((i) => i !== undefined);  // storing all keys
      key_resp.rt = [].concat(key_resp.rt, theseKeys[0].rt).filter((i) => i !== undefined);
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  
  // *textGazePoint* updates
  if (t >= 0.0 && textGazePoint.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    textGazePoint.tStart = t;  // (not accounting for frame time here)
    textGazePoint.frameNStart = frameN;  // exact frame index
    textGazePoint.setAutoDraw(true);
  }

  frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (textGazePoint.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    textGazePoint.setAutoDraw(false);
  }
  
  // *textQuestionRecog* updates
  if (t >= 5.0 && textQuestionRecog.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    textQuestionRecog.tStart = t;  // (not accounting for frame time here)
    textQuestionRecog.frameNStart = frameN;  // exact frame index
    textQuestionRecog.setAutoDraw(true);
  }

  frameRemains = 5.0 + 3.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (textQuestionRecog.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    textQuestionRecog.setAutoDraw(false);
  }
  
  // *keyQuestionRecog* updates
  if (t >= 5.0 && keyQuestionRecog.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    keyQuestionRecog.tStart = t;  // (not accounting for frame time here)
    keyQuestionRecog.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { keyQuestionRecog.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { keyQuestionRecog.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { keyQuestionRecog.clearEvents(); });
  }

  frameRemains = 5.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (keyQuestionRecog.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    keyQuestionRecog.status = PsychoJS.Status.FINISHED;
  }

  if (keyQuestionRecog.status === PsychoJS.Status.STARTED) {
    let theseKeys = keyQuestionRecog.getKeys({keyList: ['y', 'n', 'left', 'right', 'space'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      keyQuestionRecog.keys = theseKeys[0].name;  // just the last key pressed
      keyQuestionRecog.rt = theseKeys[0].rt;
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  trialComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine && routineTimer.getTime() > 0) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function trialRoutineEnd() {
  //------Ending Routine 'trial'-------
  trialComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
  if (typeof key_resp.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
      routineTimer.reset();
      }
  
  key_resp.stop();
  psychoJS.experiment.addData('keyQuestionRecog.keys', keyQuestionRecog.keys);
  if (typeof keyQuestionRecog.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('keyQuestionRecog.rt', keyQuestionRecog.rt);
      routineTimer.reset();
      }
  
  keyQuestionRecog.stop();
  return Scheduler.Event.NEXT;
}


function endLoopIteration({thisScheduler, isTrials=true}) {
  // ------Prepare for next entry------
  return function () {
    // ------Check if user ended loop early------
    if (currentLoop.finished) {
      // Check for and save orphaned data
      if (Object.keys(psychoJS.experiment._thisEntry).length > 0) {
        psychoJS.experiment.nextEntry();
      }
      thisScheduler.stop();
    } else if (isTrials) {
      psychoJS.experiment.nextEntry();
    }
  return Scheduler.Event.NEXT;
  };
}


function importConditions(loop) {
  const trialIndex = loop.getTrialIndex();
  return function () {
    loop.setTrialIndex(trialIndex);
    psychoJS.importAttributes(loop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (Object.keys(psychoJS.experiment._thisEntry).length > 0) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});

  return Scheduler.Event.QUIT;
}
