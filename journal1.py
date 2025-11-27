import sys

if len(sys.argv) == 4:
   principal = float(sys.argv[1])
    rate = float(sys.argv[2])
    time = float(sys.argv[3])
else:
    principal = 900
    rate = 0.1
    time = 5

interest = (principal * rate * time) / 100

print("\n--- Simple Interest Calculator ---")
print(f"Principal Amount: ₹{principal}")
print(f"Rate of Interest: {rate}%")
print(f"Time Period: {time} years")
print(f"Simple Interest: ₹{interest:.2f}")
