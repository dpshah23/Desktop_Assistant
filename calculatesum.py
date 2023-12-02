import wolframalpha as wf
import speak as sp
def calc(query):
    api_key="3YU5G2-7R28U63576"
    requester=wf.Client(api_key)
    requested=requester.query(query)

    try:
        answer=next(requested.results).text
        return answer
    except:
        sp.speak("The Value is not answerable")


def calcu(query):
    term=str(query)
    term=term.replace("calculate","")
    term=term.replace("multiply","*")
    term=term.replace("into","*")
    term=term.replace("plus","+")
    term=term.replace("minus","-")
    term=term.replace("subtract","-")
    term=term.replace("divide","/")

    final=str(term)
    
    try:
        result=calc(final)
        print(f"The answer is  {result}")
        sp.speak(f"The answer is  {result}")

    except:
        print("The value is not answerable")
        sp.speak("The value is not answerable")


