from backendai import ai_request
from dotenv import load_dotenv


def main():
    load_dotenv()
    try:
        request = input("Вводите свои запросы. Если хотите остановить программу, введите 'end' или завершите работу с помощью ctrl+c:\n")
        while request.lower() != "end":
            answer = ai_request(request=request)
            print("\n___Ответ на вопрос:___\n")
            print(answer)
            request = input("\n")
    except KeyboardInterrupt:
        print("\nСпасибо что пользовались моим ботом!")
    finally:
        pass

if __name__ == "__main__":
    main()
