# # logging 
# def log_decorator(func):
#     def inner():
#         print(f"Calling functions: {func.__name__}")
#         return func()
#     return inner

# @ log_decorator
# def say_hello():
#     print("Hello")

# say_hello()
import time
def log_decorator(func):
    def inner(patient_name):
        print(f"📄 Recording Patient details: {patient_name}")
        return func(patient_name)
    return inner

def timer_decorator(func):
    def inner(patient_name):
        start = time.time()
        result = func(patient_name)
        end = time.time()
        print(f"⌛ Consultation time: {end - start :.4f} seconds")
        return result
    return inner

@ log_decorator
@ timer_decorator
def doctor_consultation(patient_name):
    print(f"👩 Doctor is consulting : {patient_name}")
    time.sleep(1)
    print(f"📄 Prescription given to the {patient_name}")

doctor_consultation("waqas")