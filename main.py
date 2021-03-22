import Leap, sys, thread, time
from pandas.core import frame

class SampleListener(Leap.Listener):
    finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
    bone_names = ['Metacarpal', 'Proximal', 'Intermediate', 'Distal']
    state_names = ['STATE_INVALID', 'STATE_START', 'STATE_UPDATE', 'STATE_END']

    def on_init(self, controller):
        print("Initialized")

    def on_connect(self, controller):
        print("Motion Sensor Connected!")

        controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE);
        controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP);
        controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP);
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);

        def on_disconnect(self, controller):
            print("Motion Sensor Disconnected!")

        def on_exit(self, controller):
            print("Exited")

    def on_frame(self, controller):
        frame = controller.frame()

''' print "Frame ID: " + str(frame.id) \
                     + " Timestamps: " + str(frame.timestamp) \
                     + " # of Hands: " + str(len(frame.hands)) \
                     + " # of Fingers: " + str(len(frame.fingers)) \
                     + " # of Tools: " + str(len(frame.tools)) \
                     + " # of Gestures: " + str(len(frame.gestures()))

'''

''' 
           handType = "Left Hand" if hand.is_left else "Right Hand"

            print handType + "Hand ID" + str(hand.id) + "Palm Position" + str(hand.palm_position)

            normal = hand.palm_normal
            direction = hand.direction

            print "pitch: " + str(direction.pitch * Leap.RAD_TO_DEG) + " Roll: " + str(normal.roll * Leap.RAD_TO_DEG) + " Yaw: " + str(direction.yaw * Leap.RAD_TO_DEG)
           # print "Frame id: %d, timestamp: %d, hands: %d, fingers: %d, tools: %d, gestures: %d"\ # %( frame.id, frame.timestamp, len(frame.hands), len(frame.fingers), len(frame.tools), len(frame.gestures()))
arm = hand.arm
print "Arm direction" + str(arm.direction) + "wrist Position: " + str(arm.wrist_position) + "Elbow Position" +str(arm.elbow_position) 
'''

for hand in frame.hands:
    for finger in hand.fingers:    '''print "Type: " + self.fingers_names[finger.type()]'''
    print" type: " + self.finger_names[finger.type]+ "ID: " + str(finger.id) + "Length (mm): " + str(finger.length) + " width (mm)" + str(finger.width)

for b in range(0, 4):
          bone = finger.bone(b)
          print "Bone: " + self.bone_names[bone.type] + "Start: " + str(bone.prev_joint) + "End: " + str(bone.next_joint) + "Direction: " + str(bone.direction)


def main():

    # Create listener and controller
    listener = SampleListener()
    controller = Leap.Controller()

    # Add listener event to controller
    controller.add_listener(listener)

    # Remove listener at the end
    print "Press Enter to quit..."
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        # Remove the sample listener when done
        controller.remove_listener(listener)

if __name__ == "__main__":
    main()


