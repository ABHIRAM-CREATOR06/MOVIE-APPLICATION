import tkinter as tk
from tkinter import messagebox, simpledialog
import requests
from bs4 import BeautifulSoup
import re

# Dictionary to map genres to IMDb URLs
GENRE_URLS = {
    "Drama": 'https://www.imdb.com/search/title/?title_type=feature&genres=drama',
    "Action": 'https://www.imdb.com/search/title/?title_type=feature&genres=action',
    "Comedy": 'https://www.imdb.com/search/title/?title_type=feature&genres=comedy',
    "Horror": 'https://www.imdb.com/search/title/?title_type=feature&genres=horror',
    "Crime": 'https://www.imdb.com/search/title/?title_type=feature&genres=crime',
    "Noir": 'https://www.imdb.com/search/title/?title_type=feature&genres=film-noir',
    "Animation": 'https://www.imdb.com/search/title/?title_type=feature&genres=animation',
    "Western": 'https://www.imdb.com/search/title/?title_type=feature&genres=western',
    "Science Fiction": 'https://www.imdb.com/search/title/?title_type=feature&genres=sci-fi',
    "History": 'https://www.imdb.com/search/title/?title_type=feature&genres=history',
    "Romance": 'https://www.imdb.com/search/title/?title_type=feature&genres=romance',
    "Thriller": 'https://www.imdb.com/search/title/?title_type=feature&genres=thriller',
    "Mystery": 'https://www.imdb.com/search/title/?title_type=feature&genres=mystery',
    "Adventure": 'https://www.imdb.com/search/title/?title_type=feature&genres=adventure',
    "Fantasy": 'https://www.imdb.com/search/title/?title_type=feature&genres=fantasy',
    "Anime": 'https://www.imdb.com/search/title/?title_type=feature&genres=animation&countries=jp',
}

def suggest_movie():
    genre = simpledialog.askstring("Input", "Enter the genre:")
    if not genre:
        return

    genre_url = GENRE_URLS.get(genre.title())
    if not genre_url:
        messagebox.showerror("Error", "Invalid genre. Please enter a valid genre.")
        return

    messagebox.showinfo("Selected Genre", f"You selected: {genre.title()}")

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        response = requests.get(genre_url, headers=headers)
        response.raise_for_status()  # Check for HTTP errors
    except requests.RequestException as e:
        messagebox.showerror("Error", f"Error fetching data: {e}")
        return

    soup = BeautifulSoup(response.text, "lxml")

    # Extract movie titles
    titles = [a.get_text() for a in soup.find_all('a', href=re.compile(r'/title/tt\d+/'))]

    if not titles:
        messagebox.showinfo("No Titles", "No titles found.")
    else:
        max_titles = 14 if genre.title() in ["Drama", "Action", "Comedy", "Horror", "Crime", "Noir", "Animation", "Western", "Science Fiction", "History"] else 12
        result = "\n".join(titles[:max_titles])
        messagebox.showinfo("Suggested Movies", result)

def search_movie():
    movie_name = simpledialog.askstring("Input", "Enter the movie name:")
    if not movie_name:
        return

    url = f"https://www.imdb.com/find?q={movie_name}&s=tt&ttype=ft&ref_=fn_ft"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Check for HTTP errors
    except requests.RequestException as e:
        messagebox.showerror("Error", f"Error fetching data: {e}")
        return

    soup = BeautifulSoup(response.text, "lxml")

    # Extract movie titles
    titles = [a.get_text() for a in soup.find_all('a', href=re.compile(r'/title/tt\d+/'))]

    if not titles:
        messagebox.showinfo("No Titles", "No titles found.")
    else:
        result = "\n".join(titles)
        messagebox.showinfo("Search Results", result)

def get_cast_and_crew():
    movie_name = simpledialog.askstring("Input", "Enter the movie name:")
    if not movie_name:
        return

    url = f"https://www.imdb.com/find?q={movie_name}&s=tt&ttype=ft&ref_=fn_ft"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Check for HTTP errors
    except requests.RequestException as e:
        messagebox.showerror("Error", f"Error fetching data: {e}")
        return

    soup = BeautifulSoup(response.text, "lxml")
    movie_link = soup.find('a', href=re.compile(r'/title/tt\d+/'))
    if not movie_link:
        messagebox.showinfo("No Results", "No movie found.")
        return

    movie_url = f"https://www.imdb.com{movie_link['href']}"
    try:
        response = requests.get(movie_url, headers=headers)
        response.raise_for_status()  # Check for HTTP errors
    except requests.RequestException as e:
        messagebox.showerror("Error", f"Error fetching data: {e}")
        return

    soup = BeautifulSoup(response.text, "lxml")
    cast_list = soup.find_all('a', href=re.compile(r'/name/nm\d+/'))
    cast = set(a.get_text() for a in cast_list)  # Use a set to avoid duplicates

    if not cast:
        messagebox.showinfo("No Cast", "No cast found.")
    else:
        result = "\n".join(list(cast)[:10])  # Limit to top 10 unique cast members
        messagebox.showinfo("Cast and Crew", result)

def toggle_theme():
    global dark_mode
    dark_mode = not dark_mode
    if dark_mode:
        root.config(bg="#26242f")
        for widget in root.winfo_children():
            widget.config(bg="#26242f", fg="white")
    else:
        root.config(bg="white")
        for widget in root.winfo_children():
            widget.config(bg="white", fg="black")

def toggle_fullscreen(event=None):
    global fullscreen
    fullscreen = not fullscreen
    root.attributes("-fullscreen", fullscreen)
    if fullscreen:
        for widget in root.winfo_children():
            widget.config(font=("Helvetica", 20))
    else:
        for widget in root.winfo_children():
            widget.config(font=("Helvetica", 12))

def main():
    global root, dark_mode, fullscreen
    dark_mode = False
    fullscreen = False
    root = tk.Tk()
    root.title("Movie Suggestion Machine")

    root.bind("<F11>", toggle_fullscreen)
    root.bind("<Escape>", toggle_fullscreen)

    tk.Label(root, text="WELCOME TO THE PROJECT OF MOVIE SUGGESTION MACHINE", font=("Helvetica", 16)).pack(pady=10)
    tk.Button(root, text="Suggest Movie", command=suggest_movie, width=20, font=("Helvetica", 12)).pack(pady=5)
    tk.Button(root, text="Search Movie", command=search_movie, width=20, font=("Helvetica", 12)).pack(pady=5)
    tk.Button(root, text="Get Cast and Crew", command=get_cast_and_crew, width=20, font=("Helvetica", 12)).pack(pady=5)
    tk.Button(root, text="Toggle Theme", command=toggle_theme, width=20, font=("Helvetica", 12)).pack(pady=5)
    tk.Button(root, text="Exit", command=root.destroy, width=20, font=("Helvetica", 12)).pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
