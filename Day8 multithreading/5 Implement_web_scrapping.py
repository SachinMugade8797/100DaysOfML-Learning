
import threading  # For multi-threading operations
import requests   # For making HTTP requests to fetch web pages
from bs4 import BeautifulSoup  # For parsing HTML content

# List of URLs to scrape
# These URLs were shown in the video as examples of LangChain tutorial pages.
URLs = [
    "https://python.langchain.com/docs/use_cases/question_answering/",
    "https://python.langchain.com/docs/use_cases/question_answering/vector_stores",
    "https://python.langchain.com/docs/use_cases/summarization/"
]

def fetch_contents(URL):
    """
    Fetches content from a given URL and prints the number of characters.
    This function simulates an I/O-bound task (network request).
    """
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, "html.parser")
    print(f"Fetched {len(soup.text)} characters from {URL}")

if __name__ == "__main__":
    threads = []  # List to store all created thread objects

    # Create and start a thread for each URL
    for URL in URLs:
        # Create a new thread targeting the 'fetch_contents' function
        # The URL is passed as an argument to the function
        thread = threading.Thread(target=fetch_contents, args=(URL,))
        threads.append(thread) # Add the thread to our list
        thread.start() # Start the thread's execution

    # Wait for all threads to complete
    # .join() ensures the main program waits for each thread to finish
    for thread in threads:
        thread.join()

    print("All web pages fetched.")
