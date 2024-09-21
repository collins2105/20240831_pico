from machine import Timer,Pin

#tim = Timer(period=5000, mode=Timer.ONE_SHOT, callback=lambda t:print(1))
#tim.init(period=1000, mode=Timer.PERIODIC, callback=lambda t:print("^^"))
yellow_led = Pin("LED",Pin.OUT)
yellow_count = 0

def yellow_led_mycallback(t:Timer):
    global yellow_count
    yellow_count += 1
    #print(f"目前mycallback執行{count}次")
    yellow_led.toggle()
    print("yellow")
    if yellow_count >= 10:
        t.deinit()
        yellow_led.off()
        
yellow_led_timer = Timer(period=1000,mode=Timer.PERIODIC,callback=yellow_led_mycallback)

red_count = 0
red_led = Pin(15,Pin.OUT)
def red_led_mycallback(t:Timer):
    global red_count
    red_count += 1
    #print(f"目前mycallback執行{count}次")
    red_led.toggle()
    print("red")
    if red_count >= 10:
        t.deinit()
        
red_led_timer = Timer(period=2000,mode=Timer.PERIODIC,callback=red_led_mycallback)