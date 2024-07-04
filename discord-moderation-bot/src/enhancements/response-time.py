import time

def calculate_response_time(start_time, end_time):
    response_time = end_time - start_time
    return response_time

def main():
    start_time = time.time()

    # Perform some moderation actions here...

    end_time = time.time()
    response_time = calculate_response_time(start_time, end_time)

    print(f"Response Time: {response_time} seconds")

if __name__ == "__main__":
    main()