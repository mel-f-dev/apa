from datetime import date
import openai



class Chatbot:
    def __init__(self):
        self.__version__ = "gpt-3.5-turbo"
        self.__message__ = [{"role":"system", "content":""},
             {"role":"user", "content":""},
             ]

    def run_gpt(self, temperature = 0, n = 1):
        completion = openai.ChatCompletion.create(
            model = self.__version__,
            messages = self.__message__,
            n = n,
            temperature = temperature,
        )
        return completion
        
    def get_ans(self):
        for message in self.__message__:
            if message["role"] == "system":
                message["content"] = f"You are ChatGPT, a large language model trained by OpenAI. Answer as concisely as possible.\nKnowledge cutoff: 2019/09 \nCurrent date: {date.today()}"
            else:
                message["content"] = input("질문을 입력해주세요:")

        completion = self.run_gpt()

        self.__message__.append({"role":"assistant","content":completion["choices"][0]["message"]["content"]})
        # print(self.__message__)
        return self.__message__


class APA:
    def __init__(self):
        self.chat = Chatbot()
        self.messages = self.chat.get_ans()

    def revise(self):
        # switch
        for message in self.messages: 
            # if message["role"] == "user":
            #     self.messages.remove(message)
            # score
            if message["role"] == "system":
                message["content"] = """You are a good prompt engineer. Analyze if assistant's content is quite 
                                        right for user's intention of the content and give to the assistant's content 
                                        a score from 0 to 100.
                                        In addition, revise user's content with more detail to get a better answer 
                                        from generative AI.
                                        Give the score and a revised user's content as follow not an assistant's content. 
                                        If user's content needs more details, include them to the content: 
                                        ### score// ### revised user's content to get a better answer from assistant"""
        # self.messages[-1]["role"] = "user"

        print("*******************************messages:", self.messages)

        completion = self.chat.run_gpt()
        result = completion["choices"][0]["message"]["content"]

        return result

        

    def re_vise(self):
        # score
        origin = self.switch()
        # self.__message__.append({"role":"user","content":completion["choices"][0]["message"]["content"]})
        

        # revise
        pass

    def apa(self):
        result = self.revise()
        print(result)
        return result

apa = APA()
apa.apa()