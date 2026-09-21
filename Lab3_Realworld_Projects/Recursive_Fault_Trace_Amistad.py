# Recursive Fault Trace

LAST_NAME = "AMISTAD"
SEED_NUM = 8
FAVORITE_ARTIST = "THE BEATLES"

fault_code = (len(LAST_NAME) * 100) + (SEED_NUM * 10) + len(FAVORITE_ARTIST)

def trace_fault(code, depth=1):
    print(f"[Level {depth}] Processing Fault Code Signal: {code}")
    if code <= 10:
        print(f"[Base Condition Reached] Root fault isolated at terminal code {code}.")
        return [code]
    reduced_code = code // 2
    return [code] + trace_fault(reduced_code, depth + 1)

print("=== RECURSIVE FAULT TRACE ANALYSIS ===")
print(f"Initial Generated Fault Code: {fault_code}")
print("Tracing sequence through control hierarchy:")

trace_log = trace_fault(fault_code)

print("\n--- TRACE SUMMARY ---")
print(f"Total Traversal Depth: {len(trace_log)}")
print(f"Diagnostic Sequence Path: {trace_log}")