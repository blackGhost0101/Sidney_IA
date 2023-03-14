import openai
import speech_recognition as sr

openai.api_key = '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'

def ask_chat_gpt(question):
    if not question:
        return "Desculpe, não entendi a pergunta."
    
    prompt = f"Q: {question}"
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        temperature=0.4,
        max_tokens=612,
        n=1,
        stop=None,
        timeout=15,
    )
    answer = response.choices[0].text.strip()
    return answer

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Olá! Como posso ajudar?')
        audio = r.listen(source)
        print('Processando...')
    try:
        command = r.recognize_google(audio, language='pt-PT')
        if 'fechar' in command or 'encerrar' in command:
            return False
        answer = ask_chat_gpt(command)
        print(answer)
    except Exception as e:
        print(f"Desculpe, não consegui entender. Erro: {e}")
    finally:
        print('Posso ajudar com mais alguma coisa?')
    return True

if __name__ == "__main__":
    while True:
        if not listen():
            break

