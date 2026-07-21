# from langchain_core.messages import HumanMessage

# from graph.builder import graph


# def run_test(question: str):

#     result = graph.invoke(
#         {
#             "messages": [
#                 HumanMessage(content=question)
#             ],
#             "route": "",
#             "answer": ""
#         }
#     )

#     print("=" * 100)
#     print("QUESTION:")
#     print(question)
#     print("=" * 100)
#     print("ANSWER:")
#     print(result["answer"])
#     print("=" * 100)


# if __name__ == "__main__":

#     # # Summary
#     # run_test("Generate summary of my resume")

#     # ATS
#     run_test("Generate ATS score")

#     # # Interview
#     # run_test("Generate interview questions")

#     # # Career
#     # run_test("Give career advice")

from langchain_core.messages import HumanMessage

from graph.builder import graph


result = graph.invoke(
    {
        "messages": [
            HumanMessage(
                content="Match my resume with the job description"
            )
        ],
        "route": "",
        "answer": "",
        "job_description": ""
    }
)

print("=" * 100)
print(result["answer"])
print("=" * 100)