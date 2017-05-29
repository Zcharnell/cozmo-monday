import cozmo
from cozmo.util import distance_mm, speed_mmps

def cozmo_program(robot: cozmo.robot.Robot):
	robot.drive_straight(distance_mm(350), speed_mmps(300)).wait_for_completed()

cozmo.run_program(cozmo_program)