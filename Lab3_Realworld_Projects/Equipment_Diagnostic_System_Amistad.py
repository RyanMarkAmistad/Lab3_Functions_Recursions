# Diagnostic System
LAST_NAME = "AMISTAD"
SEED_NUM = 8
FAVORITE_ARTIST = "THE BEATLES"

def logger(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Executing diagnostic module: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@logger
def Generated_Readings():
    readings = [
        len(LAST_NAME) * 7.5,
        (SEED_NUM + 1) * 8.0,
        len(FAVORITE_ARTIST) * 8.2,
        "almost done"
    ]
    return readings

@logger
def Validation(readings):
    valid_readings = []
    for val in readings:
        try:
            numeric_val = float(val)
            valid_readings.append(round(numeric_val, 2))
        except (ValueError, TypeError):
            print(f"[WARN] Skipped invalid telemetry data: '{val}'")
    return valid_readings

@logger
def Classification(avg):
    if avg > 80:
        return "CRITICAL OVERLOAD"
    elif avg > 50:
        return "NOMINAL OPERATIONAL"
    else:
        return "LOW POWER|STANDBY"

print("=== EQUIPMENT DIAGNOSTIC SYSTEM ===")
raw_data = Generated_Readings()
clean_data = Validation(raw_data)
average_val = sum(clean_data) / len(clean_data)
status = Classification(average_val)

print("\n--- DIAGNOSTIC SUMMARY ---")
print(f"Raw Telemetry: {raw_data}")
print(f"Valid Telemetry: {clean_data}")
print(f"Average Operational Metric: {round(average_val, 2)}")
print(f"System Status: {status}")