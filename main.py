print("hello, mars")

def read_log_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                print(line.strip())
    except Exception as e:
        print(f"에러 발생: {e}")

log_file = "mission_computer_main.log"
read_log_file(log_file)

