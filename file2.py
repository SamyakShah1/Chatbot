import requests
import pandas as pd
from py2neo import Graph, Node, Relationship
# Fetch book data from Open Library API
book_url = "https://openlibrary.org/search.json?q=harry+potter&limit=5"
response = requests.get(book_url)
books_data = response.json()

books_list = []
for book in books_data["docs"]:
    books_list.append({
        "Title": book.get("title"),
        "Author": book["author_name"][0] if "author_name" in book else None,
        "Genre": book.get("subject", ["Unknown"])[0]  # Extract first subject if available
    })

books_df = pd.DataFrame(books_list)
print(books_df.head())
def fetch_author_info(author_name):
    """Fetch author details from Wikipedia API"""
    wiki_url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{author_name.replace(' ', '_')}"
    response = requests.get(wiki_url)
    
    if response.status_code == 200:
        data = response.json()
        return {
            "Author": author_name,
            "Birthdate": data.get("birth_date", "Unknown"),
            "Nationality": data.get("description", "Unknown")
        }
    return None

# Fetch details for each author
authors_list = [fetch_author_info(author) for author in books_df["Author"].dropna()]
authors_df = pd.DataFrame(authors_list)
print(authors_df.head())
# Fill missing values
books_df.fillna("Unknown", inplace=True)
authors_df.fillna("Unknown", inplace=True)

# Merge books and authors on Author Name
merged_df = pd.merge(books_df, authors_df, on="Author", how="left")
print(merged_df.head())
for _, row in merged_df.iterrows():
    author_node = Node("Author", name=row["Author"], nationality=row["Nationality"])
    book_node = Node("Book", title=row["Title"], genre=row["Genre"])
    wrote_relation = Relationship(author_node, "WROTE", book_node)
    graph.merge(author_node, "Author", "name")
    graph.merge(book_node, "Book", "title")
    graph.merge(wrote_relation)
    