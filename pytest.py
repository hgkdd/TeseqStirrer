import time
import serial # pyserial

class stirrer(object):
    """
    Class to control TESEQ stirrer.
    """
    def __init__(self, port=2):
        self.dev=serial.Serial(port=port, # 2 -> COM3 
                            baudrate=9600,
                            bytesize=serial.EIGHTBITS,
                            parity=serial.PARITY_NONE,
                            stopbits=serial.STOPBITS_ONE,
                            timeout=None)
    def _state(self):
        for i in range(10):
            ans=self._ask('?') # ask for status
            ans=ans.split(",")
            try:
                stopped=(ans[0]=='1')
                ca=float(ans[1]) # current angle
                drive_init_ok=(ans[2]=='0')
                fail=(ans[3]=='1')
                break
            except (IndexError, ValueError):
                continue
        return stopped, ca, drive_init_ok, fail
                            
    def _wait(self):
        stopped=False
        while not stopped: # loop until stirrer is stopped
            stopped, self.ca, self.drive_init_ok, fail = self._state()
            time.sleep(0.2) # don't jam the serial bus
        return self.ca
    
    def _write(self, cmd):
        self.dev.flushInput() # flus input buffer before new cmd is send
        n=self.dev.write('%s\r'%cmd)
        return n-1
    
    def _read(self):
        ans=self.dev.readline(eol='\r')
        return ans
        
    def _ask(self, cmd):
        self._write(cmd)
        while self.dev.inWaiting() == 0: # wait until something is ready to read
            time.sleep(0.1)
        ans=[]
        while self.dev.inWaiting() > 0: # read until there's no more to read
            time.sleep(0.1)
            d=self._read()
            #print d
            ans.append(d)
        ans=''.join(ans)
        #print cmd, '->', ans
        return ans
    
    def Init(self, maxspeed=None, minspeed=None, acc=None):
        ans=self._ask('INIT')
        self._wait()
        if not self.drive_init_ok:
            raise ValueError("Drive init failed.")
        # set maxspeed, minspeed and acc to save and valid values
        if maxspeed is None:
            maxspeed=6
        else:
            maxspeed=min(6,maxspeed)
            maxspeed=max(0.18,maxspeed)
        if minspeed is None:
            minspeed=0.18
        else:
            minspeed=min(6,minspeed)
            minspeed=max(0.18,minspeed)
        if acc is None:
            acc=65
        else:
            acc=min(65, acc)
            acc=max(40, acc)
        cmds=('MAXSPEED:%f'%maxspeed,
              'MINSPEED:%f'%minspeed,
              'ACC:%f'%acc)
        for cmd in cmds:
            #print cmd
            ans=self._ask(cmd)
            #print ans
        return self.ca
    
    def Goto(self, pos):
        # wrap angle
        pos=pos%360
        self._ask('RMA:%f'%pos)
        # wait until stirrer stopped
        self._wait()
        return self.ca

    def Move(self, dir):
        if dir==1:
            self._write('DIR:1')
            time.sleep(0.1)
            self._write('RMS')
        elif dir==-1:
            self._write('DIR:0')
            time.sleep(0.1)
            self._write('RMS')
        else:
            self._write('Stop')
            self._wait()
        return dir

        
    def Info(self):
        ans=self._ask('INFO')
        return ans
    
if __name__ == '__main__':
    from numpy import linspace
    dev=stirrer()
    print("Init stirrer ...")
    ang=dev.Init()
    print("Angle after INIT:", ang)
    #info=dev.Info()
    #print "Drive parameters:", info 
    
    dev.Move(1)
    time.sleep(5)
    dev.Move(0)
    time.sleep(1)
    dev.Move(1)
    time.sleep(5)
    dev.Move(0)
    time.sleep(1)
        
    for pos in linspace(-100, 400, num=5, endpoint=True):
        ang=dev.Goto(pos)
        print(time.time(), pos, ang)