function on_msg_receive (msg)

	if msg.out then
		return
	end
	if (msg.text=='Hello') then
         	send_msg (msg.from.print_name, 'Hello, My name is Jarvis, i am your homebot.', ok_cb, false)
	elseif (msg.text=='Armed motion buzzer') then
         	send_msg (msg.from.print_name, 'Home Motion Sensor Alarm Armed.', ok_cb, false)
         	os.execute('python /home/pi/homepi/motion-sensor-alarm/motion-trigered-buzzer.py &')
	elseif (msg.text=='What time') then
         	send_msg (msg.from.print_name, os.date("The time is now is %H:%M:%S, on %x."), ok_cb, false)
	elseif (msg.text=='Disarmed motion buzzer') then
     		os.execute('python /home/pi/homepi/motion-sensor-alarm/trigger-off-alarm.py &')
        	send_msg (msg.from.print_name, 'Home Motion Sensor Alarm DisArmed.', ok_cb, false)
	elseif (msg.text=='Armed buzzer') then
         	send_msg (msg.from.print_name, 'Alarm Actived.', ok_cb, false)
         	os.execute('python /home/pi/homepi/motion-sensor-alarm/buzzer-on.py &')
	elseif (msg.text=='Disarmed buzzer') then
     		os.execute('python /home/pi/homepi/motion-sensor-alarm/buzzer-off.py &')
        	send_msg (msg.from.print_name, 'Alarm Diactived.', ok_cb, false)
      	elseif (msg.text=='Armed camera') then
        	send_msg (msg.from.print_name, 'Security Camera Arming need to be done in the termail.', ok_cb, false)
	elseif (msg.text=='Disarmed camera') then
     		os.execute('pkill -f main.py')
        	send_msg (msg.from.print_name, 'Security Camera Offline', ok_cb, false)
        elseif (msg.text=='Photo') then
     		os.execute('/home/pi/camera/camera.sh')
        	send_photo (msg.from.print_name, '/home/pi/camera/photo.jpg', ok_cb, false)
	elseif (msg.text=='Room temperature reading') then
                os.execute('python /home/pi/homepi/temperature-sensor/Board.py &')
        	local data = io.open("/home/pi/homepi/temperature-sensor/sensor.txt","r")    
		reading = data:read()
		data.close() 
		send_msg (msg.from.print_name, reading , ok_cb, false)
      	elseif (msg.text=='Help') then
	 	send_msg (msg.from.print_name, '1)| cmd: Armed motion buzzer < - Active Alarm | 2)| cmd: Disarmed motion buzzer < - Deactive Alarm | 3)| cmd: Armed camera < - Start Secuirty Camera | 4)| cmd: Disarmed camera < - Stop Secuirty Camera  | 5)| cmd: Photo < - Take photograph* | 6)| cmd: Armed buzzer < - Start Alarm | 7)| cmd: Disarmed buzzer < - Sop Alarm | 8)| cmd: Room temperature reading < - Room Temperature reading from the sensor | 9)| cmd: What time < - The time now |',ok_cb, false)
      	else
	 	send_msg (msg.from.print_name, 'I cannot comprehens what you want. Can he tell me what you want again?', ok_cb, false)
      	end
    

end

function on_our_id (our_id)
end

function on_secret_chat_update (user, what_changed)
end

function on_user_update (user, what_changed)
end

function on_chat_update (user, what_changed)
end

function on_get_difference_end ()
end

function on_binlog_replay_end ()
end