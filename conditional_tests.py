pressure = 101.3
print(pressure == 101.3)
print(pressure != 101.3)
print(pressure > 150.0)
# ----
temperature = 85.0
if temperature > 100:
    print("Warning: Temperature exceeds limit!")
else:
    print("Temperature is within safe limits")
# ----
pressure = 21.0
if pressure > 150:
    print("Emergency: High pressure shutdown!")
elif 20 < pressure < 50:
    print("Warning: Low pressure alert")
else:
    print("System pressure is stable")
# ----
temperature = 110.0
pressure = 120.0
if temperature > 100 or pressure > 150.0:
    print("Alarm: Safety limits exceeded!")
else:
    print("System is running safely")
# ----
active_pumps = ["pump_01", "pump_03", "pump_04"]
target_pump = "pump_02"
if target_pump in active_pumps:
    print("Status: Pump is running.")
else:
    print("Status: Pump is currently offline.")
if target_pump not in active_pumps:
    print("Warning: Schedule immediate inspection for pump_02")
# ----
alarms = ["high_pressure", "temp_exceeded"]
if alarms:
    for alarm in alarms:
        print(f"active alarm: [{alarm}]".upper())
else:
    print("System status: Normal. No active alarms.")
