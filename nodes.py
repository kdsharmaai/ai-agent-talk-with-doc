from state import State
from langchain_community.document_loaders import PyPDFLoader
from langchain_openai.chat_models import ChatOpenAI

def load_pdf_text(file_path):
    loader = PyPDFLoader(file_path)
    pages = loader.load_and_split()
    return " ".join([page.page_content for page in pages])

# Agent node
def ingest_pdf(state: State):
    # Assume PDF path is in the first message
    pdf_path = state['messages'][0].content
    pdf_text = load_pdf_text(pdf_path)
    state['pdf_content'] = pdf_text
    return state

# Agent node
def answer_question(state: State):
    user_message = state['messages'][-1].content
    pdf_content = state['pdf_content']

    prompt = (
        f"Extract and format the answer to the following question or instruction from the PDF content below.\n\n"
        f"PDF Content:\n{pdf_content}\n\n"
        f"Question / Instruction: {user_message}\n\n"
        f"If the answer is not present, reply: 'No content found in PDF.'"
    )

    llm = ChatOpenAI(model="gpt-4o-mini")

    answer = llm.invoke(
        [{"role": "user", "content": prompt}]
    ).content

    state['messages'].append({"role": "assistant", "content": answer})
    return state