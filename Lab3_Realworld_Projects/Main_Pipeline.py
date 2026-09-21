# Module 2: Main Pipeline and Final Diagnostic Report
import Telemetry

LAST_NAME = "AMISTAD"
SEED_NUM = 8
FAVORITE_ARTIST = "THE BEATLES"

print("=" * 80)
print(f"{'INTELLIGENT EQUIPMENT MONITORING PIPELINE':^80}")
print("=" * 80)

raw_stream = list(Telemetry.generate_telemetry_stream(LAST_NAME, SEED_NUM, FAVORITE_ARTIST))
valid_readings = []
invalid_count = 0

print(f"\n--- Phase 1: Stream Ingestion & Parsing ---")
for raw in raw_stream:
    processed = Telemetry.Process_Stream(raw)
    if processed is not None:
        valid_readings.append(processed)
    else:
        invalid_count += 1

calibrate = lambda x: round(x * 1.05, 2)
calibrated_readings = list(map(calibrate, valid_readings))

total_processed = len(raw_stream)
valid_count = len(valid_readings)
avg_reading = sum(calibrated_readings) / valid_count if valid_count > 0 else 0

print(f"\n--- Phase 2: Recursive Abnormal Fault Trace ---")
initial_fault_code = int((len(LAST_NAME) * 50) + (SEED_NUM * 12))
trace_path = Telemetry.Trace_Abnormal_Condition(initial_fault_code)

if avg_reading > 100:
    overall_status = "CRITICAL OVERLOAD"
elif avg_reading > 60:
    overall_status = "NOMINAL / HEALTHY"
else:
    overall_status = "LOW POWER"

print("\n" + "=" * 80)
print(f"{'FINAL DIAGNOSTIC REPORT':^80}")
print("=" * 80)
print(f"Student Inputs          : Surname = {LAST_NAME} | Seed = {SEED_NUM} | Artist = {FAVORITE_ARTIST}")
print(f"Raw Telemetry Stream    : {raw_stream}")
print(f"Total Processed Items   : {total_processed}")
print(f"Valid Readings          : {valid_readings}")
print(f"Invalid Readings Count  : {invalid_count}")
print(f"Calibrated Data (Lambda): {calibrated_readings}")
print(f"Average Metric          : {round(avg_reading, 2)}")
print(f"Recursive Trace Depth   : {len(trace_path)}")
print(f"Recursive Trace Path    : {trace_path}")
print(f"Overall Equipment Status: {overall_status}")
print("=" * 80)