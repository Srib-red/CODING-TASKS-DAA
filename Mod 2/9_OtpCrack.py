import random
import time

def generate_4digit_otp():
    # generate integer 0..9999 and format as 4-digit string '0000'..'9999'
    return f"{random.randint(0, 9999):04d}"

def otp_function(candidate, real_otp):
    return candidate == real_otp

def otp_crack(real_otp):
    attempts = 0
    start = time.time()
    for i in range(10000):                 # 0000 .. 9999
        candidate = f"{i:04d}"
        attempts += 1
        if otp_function(candidate, real_otp):
            return candidate, attempts, time.time() - start
    return None, attempts, time.time() - start  # should not happen

if __name__ == "__main__":
    real_otp = generate_4digit_otp()
    print("Generated OTP (secret):", real_otp)

    found, tries, elapsed = otp_crack(real_otp)
    print("Found OTP:", found)
    print("Attempts:", tries)
    print("Time elapsed: {:.4f} seconds".format(elapsed))
