import threading
import time

class TimerInterrupt:
    def __init__(self):
        self.timers = {}

    def start_timer(self, name, interval, callback):
        """Start a timer that runs a callback function at specified intervals."""
        if name in self.timers:
            print(f"Timer {name} already exists.")
            return
        
        timer_thread = threading.Thread(target=self._run_timer, args=(name, interval, callback), daemon=True)
        self.timers[name] = {'thread': timer_thread, 'stop_event': threading.Event()}
        timer_thread.start()

    def _run_timer(self, name, interval, callback):
        stop_event = self.timers[name]['stop_event']
        while not stop_event.is_set():
            time.sleep(interval)
            callback()
    
    def stop_timer(self, name):
        """Stop the specified timer."""
        if name in self.timers:
            self.timers[name]['stop_event'].set()
            self.timers[name]['thread'].join()
            del self.timers[name]
        else:
            print(f"Timer {name} does not exist.")
    
    def list_timers(self):
        """List all active timers."""
        return list(self.timers.keys())

# Example usage
def my_callback():
    print("Timer callback executed")

timers = TimerInterrupt()
timers.start_timer("timer1", 2, my_callback)  # Execute callback every 2 seconds

# Wait for some time to see the callback in action
time.sleep(10)

timers.stop_timer("timer1")
print("Timer stopped.")
