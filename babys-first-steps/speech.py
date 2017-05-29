import cozmo
from cozmo.util import degrees

def cozmo_program(robot: cozmo.robot.Robot):
	### Names!
	robot.set_lift_height(0.0).wait_for_completed()
	robot.set_head_angle(degrees(45.0)).wait_for_completed()
	robot.say_text("Elayna").wait_for_completed()
	robot.set_head_angle(degrees(15.0)).wait_for_completed()
	robot.say_text("Scarlet", voice_pitch=1).wait_for_completed()
	robot.set_head_angle(degrees(-15.0)).wait_for_completed()
	robot.say_text("Oscar", voice_pitch=1).wait_for_completed()
    ### Song!
    # song = ["Doe, Ray, Mi, Fa", "So fucking done with you girl"];
    # robot.move_head(-5) # start moving head down so it mostly happens in parallel with lift
    # robot.set_lift_height(0.0).wait_for_completed()
    # robot.set_head_angle(degrees(-25.0)).wait_for_completed()
    # # robot.say_text("Do, re, mi, fa, so fucking done with you girl").wait_for_completed()
    # scale = [1, 1.5]
    # for idx, line in enumerate(song):
    # 	robot.say_text(line, voice_pitch=(0+1*idx), duration_scalar=scale[idx]).wait_for_completed()


cozmo.run_program(cozmo_program)
