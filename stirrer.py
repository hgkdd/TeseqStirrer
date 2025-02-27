#!/usr/bin/env python3
import time
import serial


class Stirrer(object):
    """
    """
    # the read termination is a space with a carriage return!
    read_termination = ' \r'
    write_termination = '\r'

    _timeout = 20
    # delay between query calls
    _status_query_delay = 0.3
    _angle_error = 0.5
    _inter_cmd_wait_time = 0.05  # in seconds

    lock_message = ("STIRRER Controller V1.50 is locked. "
                    "Please check SYNC position and restart the controller!")

    default_port_parameters = {
        'port': '/dev/stirrer',
        'baudrate': 9600,
        'bytesize': serial.EIGHTBITS,
        'parity': serial.PARITY_NONE,
        'stopbits': serial.STOPBITS_ONE,
        'xonxoff': True,
        'rtscts': False,
        'dsrdtr': False,
        'inter_byte_timeout': None,
        'exclusive': False}

    # currently these values are ignored
    stirrer_parameters = {
        'maxspeed': 6,
        'minspeed': 0.18,
        'acc': 65
        }

    def __init__(
            self,
            port_parameters={},
            status_retries=10,
            do_not_open=False):
        self.status_retries = status_retries
        self.port_parameters = port_parameters
        self._create_serial_port()
        if not do_not_open:
            self._status()
        self.next_angle = None

    def _create_serial_port(self):
        self.port = serial.Serial(
            **{**Stirrer.default_port_parameters,
               **self.port_parameters})

    def _write(self, command):
        self.port.reset_input_buffer()
        self.port.reset_output_buffer()
        bytes_written = self.port.write(
            f"{command}{self.write_termination}".encode())
        self.port.flush()
        return bytes_written

    def _read(self, size):
        answer = self.port.read_until(
            expected=self.read_termination.encode(),
            size=size)
        # drop the carriage return
        return answer.decode()[:-len(self.read_termination)]

    def _query(self, command):
        self._write(command)
        while self.port.in_waiting == 0:
            time.sleep(self._status_query_delay)
        answer = []
        while self.port.in_waiting > 0:
            partial = self._read(self.port.in_waiting)
            answer.append(partial)
            time.sleep(.01)
        answer = ''.join(answer)
        return answer

    @property
    def current_angle(self):
        self._status()
        return self._current_angle

    def _clip_angle(self, angle):
        # angle only values 0 <= angle < 360 are allowed
        # check if the angle needs unwraping
        while angle >= 360:
            angle -= 360
        while angle < 0:
            angle += 360
        return angle

    @current_angle.setter
    def current_angle(self, angle):
        angle = self._clip_angle(angle)
        # Move Absolute
        self._write(f'RMA:{angle}')
        self._wait()

        if self._angle_error < abs(self.current_angle - angle):
            raise AngleError(
                angle,
                self.current_angle,
                self._angle_error)
        if self._error:
            raise Exception(self._error_message)

    @property
    def motor_running(self):
        self._status()
        return self._motor_running

    @property
    def drive_initialized(self):
        self._status()
        if self.motor_running:
            return False
        # print(self._drive_initialized)
        return self._drive_initialized

    @property
    def error(self):
        self._status()
        return self._error

    @property
    def error_message(self):
        self._status()
        return self._error_message

    def initialize_drive(self):
        self._status()
        if not self.drive_initialized:
            self._write('INIT')
            self._wait()
        return self.drive_initialized

    def stop_motor(self):
        self._write('STOP')
        self._wait()
        return self.motor_running

    def run_clockwise(self):
        self._write('DIR:1')
        time.sleep(self._inter_cmd_wait_time)
        self._write('RMS')
        self._wait2()
        return self.motor_running

    def step_clockwise_by(self, step):
        self._write('DIR:1')
        time.sleep(self._inter_cmd_wait_time)
        pos = self.current_angle + step
        pos = self._clip_angle(pos)
        self._write(f'RMA:{abs(int(pos))}')
        self._wait2()
        return self.motor_running

    def run_anti_clockwise(self):
        self._write('DIR:0')
        time.sleep(self._inter_cmd_wait_time)
        self._write('RMS')
        self._wait2()
        return self.motor_running

    def step_anti_clockwise_by(self, step):
        self._write('DIR:0')
        time.sleep(self._inter_cmd_wait_time)
        pos = self.current_angle - step
        pos = self._clip_angle(pos)
        self._write(f'RMA:{abs(int(pos))}')
        self._wait2()
        return self.motor_running

    def goto_angle(self, angle, direction = 1):
        """
        direction = 1 -> clockwise
        """
        if direction == 1:
            self._write('DIR:1')
        else:
            self._write('DIR:0')
        time.sleep(self._inter_cmd_wait_time)
        angle = self._clip_angle(angle)
        self._write(f'RMA:{abs(int(angle))}')
        self._wait2()
        return self.motor_running


    #wait while motor is running
    def _wait(self):
        wait_interval = 0.3
        wait_duration = 0

        time.sleep(wait_interval)
        wait_duration += wait_interval

        while self.motor_running:
            time.sleep(wait_interval)
            wait_duration += wait_interval
            if wait_duration >= self._timeout:
                print(f"Waiting for motor to finish movement "
                      f"timed out. Waited {wait_duration} s.")
                break
        return self._current_angle
    
    # wait until motor is running
    def _wait2(self):
        wait_interval = 0.3
        wait_duration = 0

        time.sleep(wait_interval)
        wait_duration += wait_interval

        while not self.motor_running:
            time.sleep(wait_interval)
            wait_duration += wait_interval
            if wait_duration >= self._timeout:
                print(f"Waiting for motor to start movement "
                      f"timed out. Waited {wait_duration} s.")
                break
        return self._current_angle

    def _status(self):
        for attempt in range(self.status_retries):
            try:
                answer = self._query('?')

                if "is locked" in answer:
                    print(f"The Stirrer answers: {answer}")
                    print("Stirrer is locked!\n"
                          "Try to turn it off and on again ;)")
                    raise StirrerLockedError()

                answer = answer.split(',')

                self._motor_running = (answer[0] == '0')
                self._current_angle = float(answer[1])
                self._drive_initialized = (answer[2] == '0')
                self._error = (answer[3] == '1')
                self._error_message = ""
                if self._error:
                    # hier funktionert was nicht,
                    # der Controller gibt Müll zurück
                    try:
                        self._error_message = self._query('ERREAD')
                    except UnicodeDecodeError:
                        print("WARNING: could not decode error message")

                return (
                    self._motor_running,
                    self._current_angle,
                    self._drive_initialized,
                    self._error,
                    self._error_message
                )

            except IndexError:
                time.sleep(self._status_query_delay)
            except ValueError:
                print(f"Unparsable device message {answer}")
                time.sleep(self._status_query_delay)
            else:
                # querying the status successful
                break
        else:
            exception = Exception(
                f"Current Stirrer State could not be queried, "
                f"Received: \"{answer}\"")
            raise exception

    def set_next_angle(self, angle):
        self.next_angle = self._clip_angle(angle)
        self._write(f'DEG:{self.next_angle}')

    def goto_next_angle(self):
        if not self.next_angle:
            return
        # Move Absolute to stored position
        self._write('RMT')
        self._wait()

        if self._angle_error < abs(self.current_angle - self.next_angle):
            raise AngleError(
                self.next_angle,
                self.current_angle,
                self._angle_error)
        if self._error:
            raise Exception(self._error_message)


    def close(self):
        self.port.close()
        self._drive_initialized = False
        #self._

    def __del__(self):
        self.port.close()

class AngleError(Exception):

    def __init__(self, new_angle, current_angle, angle_error_threshold):
        """

        """
        self.new_angle = new_angle
        self.current_angle = current_angle
        self.angle_error_threshold = angle_error_threshold
        super().__init__(
            (
                f"Could not reach new angle {new_angle}, "
                f"from {current_angle} with a allowed "
                f"deviation of {angle_error_threshold} ")
        )


class StirrerLockedError(Exception):
    def __init__(self):

        super().__init__(
            'Try to turn it off and on again and reinit')

if __name__ == '__main__':
    import atexit
    stirrer = Stirrer()
    atexit.register(stirrer.stop_motor)
    if not stirrer.drive_initialized:
        stirrer.initialize_drive()

#    print('run clockwise for 20 sec')
    stirrer.run_clockwise()
    while True:
        pass
#    for i in range(20):
#        time.sleep(1)
#        print(i)
#    stirrer.stop_motor()

#    print('run anti-clockwise for 10 sec')
#    stirrer.run_anti_clockwise()
#    for i in range(10):
#        time.sleep(1)
#        print(i)
#    stirrer.stop_motor()

#    print("Step stirrer")
#    # step stirrer
#    for angle in range(0, 360, 10):
#        try:
#            # Set angle of RC Stirrer:
#            stirrer.current_angle = angle
#        except Exception:
#            pass
#        # Let RC stirrer settle (avoiding transients due to
#        # mechanical oscillations after stopping at a new angle):
#        print(angle)
#        time.sleep(1)
