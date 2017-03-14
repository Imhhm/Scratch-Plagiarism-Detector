node_type = dict()
#classifying all the possible nodes into their node types
#node_type["motion"] = ["turnRight","turnLeft","heading","pointTowards","gotoX:y:","gotoSpriteOrMouse:","glideSecs:toX:y:elapsed:from:","changeXposBy:","xpos:","changeYposBy:","ypos:","bounceOffEdge","setRotationStyle"]}
#motion - motion_data and motion (motion is the operation
node_type["forward:"] = "motion" #in the editor: eg. move 10 steps
node_type["turnRight:"] = "motion" #clockwise
node_type["turnLeft:"] =  "motion" #anticlockwise
node_type["heading:"] =  "motion" #in the editor: point in direction 
node_type["pointTowards:"] =  "motion" #eg. pointTowards mouse pointer
node_type["gotoX:y:"] =  "motion" 
node_type["gotoSpriteOrMouse:"] =  "motion"
node_type["glideSecs:toX:y:elapsed:from:"] =  "motion"
node_type["changeXposBy:"] =  "motion"
node_type["changeYposBy:"] =  "motion"
node_type["xpos:"] =  "motion"
node_type["ypos:"] =  "motion"
node_type["bounceOffEdge"] =  "motion"
node_type["setRotationStyle"] =  "motion"
node_type["xpos"] =  "motion_data"
node_type["ypos"] =  "motion_data"
node_type["heading"] =  "motion_data" #in the scratch editor, it's direction. it means which direction (angle) it's pointing to


#looks - looks data and looks (looks is the operation)
node_type["say:duration:elapsed:from:"] =  "looks"
node_type["say:"] =  "looks"
node_type["think:duration:elapsed:from:"] =  "looks"
node_type["think:"] =  "looks"
node_type["show"] =  "looks"
node_type["hide"] =  "looks"
node_type["lookLike:"] =  "looks"
node_type["nextCostume"] =  "looks"
node_type["startScene"] =  "looks"
node_type["startSceneAndWait"] =  "looks" #for the stage. switch backdrop and wait
node_type["nextScene"] =  "looks" #for the stage. next backdrop
node_type["changeGraphicEffect:by:" ] =  "looks"
node_type["setGraphicEffect:to:"] =  "looks"
node_type["filterReset"] =  "looks"
node_type["changeSizeBy:"] =  "looks"
node_type["setSizeTo:"] =  "looks"
node_type["comeToFront"] =  "looks"
node_type["goBackByLayers:"] =  "looks"
node_type["scale"] =  "looks_data" 				#size in the scratch editor
node_type["sceneName"] =  "looks_data" 			#backdrop name
node_type["costumeIndex"] =  "looks_data" 		#costume number


#sound - sound_data and sound
node_type["playSound:"] = "sound"
node_type["doPlaySoundAndWait"] = "sound"
node_type["stopAllSounds"] = "sound"
node_type["playDrum"] = "sound"
node_type["rest:elapsed:from:"] = "sound"
node_type["noteOn:duration:elapsed:from:"] = "sound"
node_type["drum:duration:elapsed:from:"] = "sound"
node_type["instrument:"] = "sound"
node_type["changeVolumeBy:"] = "sound"
node_type["setVolumeTo:"] = "sound"
node_type["changeTempoBy:"] = "sound"
node_type["setTempoTo:"] = "sound"
node_type["volume"] = "sound_data"
node_type["tempo"] = "sound_data"


#pen
node_type["clearPenTrails"] = "pen"
node_type["stampCostume"] = "pen"
node_type["putPenDown"] = "pen"
node_type["putPenUp"] = "pen"
node_type["penColor:"] = "pen" #choose by clicking 
node_type["changePenHueBy:"] = "pen"
node_type["setPenHueTo:"] = "pen" #enter the colour through text
node_type["changePenShadeBy:"] = "pen"
node_type["setPenShadeTo:"] = "pen"
node_type["changePenSizeBy:"] = "pen"
node_type["penSize:"] = "pen"

#events - event_cond and event (event is the operation)
node_type["whenSensorGreaterThan"] = "event_cond"	
node_type["whenIReceive"] = "event_cond"	
node_type["broadcast:"] = "event"	
node_type["doBroadcastAndWait"] = "event"	
node_type["whenGreenFlag"] = "event_cond"	
node_type["whenSceneStarts"] = "event_cond"	
node_type["whenKeyPressed"] = "event_cond"	
node_type["whenClicked"] = "event_cond"	

#control - contorl_cond, control_loop, control_loop_cond control (just control is an operation)
'''
node_type["doIf"] = "control_cond"	
node_type["createCloneOf"] = "control"	
node_type["wait:elapsed:from:"] = "control"	
node_type["doRepeat"] = "control_loop"	#repeat
node_type["doForever"] = "control_loop"	#repeat forever
node_type["doIfElse"] = "control_cond"	
node_type["doUntil"] = "control_loop_cond" #repeat until
node_type["deleteClone"] = "control"	
node_type["doWaitUntil"] = "control" #doesn't have a block
node_type["whenCloned"] = "control_cond"	
node_type["stopScripts"] = "control"
'''
node_type["doIf"] = "control_cond1"	#if then
node_type["createCloneOf"] = "control"	
node_type["wait:elapsed:from:"] = "control"	 
node_type["doRepeat"] = "control_loop_cond"	#repeat 10
node_type["doForever"] = "control_loop"	#repeat forever
node_type["doIfElse"] = "control_cond2"	
node_type["doUntil"] = "control_loop_cond" #repeat until
node_type["deleteClone"] = "control"	
node_type["doWaitUntil"] = "control"#wait	 
node_type["whenCloned"] = "event_cond"	
node_type["stopScripts"] = "control"


#data operations
#list - list_cond, list_data, list (list is an operation
node_type["append:toList:"] = "list"
node_type["deleteLine:ofList:"] = "list"
node_type["insert:at:ofList:"] = "list"
node_type["setLine:ofList:to:"] = "list" #replace
node_type["showList:"] = "list"
node_type["hideList:"] = "list"


node_type["list:contains:"] = "list_cond" #it is a condition
node_type["getLine:ofList:"] = "list_data" #eg. ["getLine:ofList:", "last", "c"], gets the item in the list with postition either relative(like last) or absolute
node_type["lineCountOfList:"] = "list_data" #lineCountOfList is the length of the list. eg. length of d is ["lineCountOfList:", "d"]

#variables: (all are operations)
node_type["setVar:to:"] = "var"
node_type["changeVar:by:"] = "var"
node_type["showVariable:"] = "var"
node_type["hideVariable:"] = "var"

#sensing: sensing_cond, sensing_data, sensing(sensing is an operation)
node_type["touching:"] = "sensing_cond"
node_type["touchingColor:"] = "sensing_cond"
node_type["keyPressed:"] = "sensing_cond"
node_type["mousePressed"] = "sensing_cond"
node_type["color:sees:"] = "sensing_cond" #(until one color is touching another) eg. ["color:sees:", 16255278, 699799]

node_type["soundLevel"] = "sensing_data" #loudness
node_type["answer"] = "sensing_data" 
node_type["timer"] = "sensing_data" 
node_type["distanceTo:"] = "sensing_data"
node_type["mouseX"] = "sensing_data"
node_type["mouseY"] = "sensing_data"
node_type["getUserName"] = "sensing_data" #username
node_type["timestamp"] = "sensing_data" #number of days since 2000

node_type["doAsk"] = "sensing"
node_type["timerReset"] = "sensing"
node_type["setVideoTransparency"] = "sensing"
node_type["setVideoState"] = "sensing"

#operators
node_type["&"] = "operator_cond"
node_type["|"] = "operator_cond"
node_type["not"] = "operator_cond"
node_type["="] = "operator_cond"
node_type[">"] = "operator_cond"
node_type["<"] = "operator_cond"

node_type["rounded"] = "operator_data"
node_type["+"] = "operator_data"
node_type["-"] = "operator_data"
node_type["*"] = "operator_data"
node_type["\/"] = "operator_data"
node_type["%"] = "operator_data" #mod
node_type["computeFunction:of:"] = "operator_data" #eg. sqrt/abs/floor/etc. of a number eg. (["computeFunction:of:", "sqrt", 9])
node_type["randomFrom:to:"] = "operator_data" #pick random 1 to 10 in scratch editor
node_type["concatenate:with:"] = "operator_data" #join in the scratch editor
node_type["letter:of:"] = "operator_data" #eg. letter 1 of world (letter <index starting from 1> of <string>)
node_type["stringLength:"] = "operator_data" #eg. letter 1 of world (letter <index starting from 1> of <string>)