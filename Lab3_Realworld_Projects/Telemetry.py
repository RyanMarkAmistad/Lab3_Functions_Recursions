# Module 1: Telemetry Generation



def logger(func):
    def wrapper(*args, **kwargs):
        print(f"[LOGGER] Executing Pipeline Phase: '{func.__name__}'")
        return func(*args, **kwargs)
    return wrapper\

# Student-Specific Telemetry Data
def generate_telemetry_stream(surname, seed_num, artist):
    base_val = len(surname) * 10
    yield base_val + (seed_num * 2.5)
    yield base_val + (len(artist) * 12.0)
    yield "ERR_INVALID_DATA"
    yield float(round(seed_num * 11, 2))
    yield base_val * 2.2

@logger
def Process_Stream(raw_val):
    try:
        val = float(raw_val)
        return val
    except (ValueError, TypeError):
        print(f"  [WARNING] Exception Handled: Skipping unparseable stream value '{raw_val}'")
        return None

def Trace_Abnormal_Condition(code, depth=1):
    print(f"  [Depth {depth}] Tracing Code Signal: {code}")
    if code <= 10:
        print(f"  [Base Case] Root cause isolated at code {code}.")
        return [code]
    
    return [code] + Trace_Abnormal_Condition(code // 2, depth + 1)