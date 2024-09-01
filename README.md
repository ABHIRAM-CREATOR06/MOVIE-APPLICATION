# Movie Suggestion Machine

Welcome to the Movie Suggestion Machine! This project is a GUI-based application that suggests movies based on genres, allows you to search for movies, and provides cast and crew information. It also includes features like light/dark mode and full-screen mode.

## Features

- **Suggest Movies**: Get movie suggestions based on selected genres.
- **Search Movies**: Search for movies by name.
- **Get Cast and Crew**: Retrieve cast and crew information for a specific movie.
- **Toggle Theme**: Switch between light and dark modes.
- **Full-Screen Mode**: Enable full-screen mode with larger icons and buttons.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/movie-suggestion-machine.git
    cd movie-suggestion-machine
    ```

2. **Install the required packages**:
    ```bash
    pip install requests beautifulsoup4 lxml
    ```

3. **Run the application**:
    ```bash
    python movie_suggestion_machine.py
    ```

## Usage

1. **Suggest Movie**: Click on the "Suggest Movie" button and enter a genre to get movie suggestions.
2. **Search Movie**: Click on the "Search Movie" button and enter the movie name to search for movies.
3. **Get Cast and Crew**: Click on the "Get Cast and Crew" button and enter the movie name to retrieve cast and crew information.
4. **Toggle Theme**: Click on the "Toggle Theme" button to switch between light and dark modes.
5. **Full-Screen Mode**: Press `F11` to toggle full-screen mode. Press `Escape` to exit full-screen mode.

## How It Works

### Suggest Movies

1. **Input Genre**: When you click the "Suggest Movie" button, a dialog box prompts you to enter a genre.
2. **Fetch Data**: The application uses the IMDb URL corresponding to the selected genre to fetch movie data.
3. **Display Genre**: The selected genre is displayed in a message box.
4. **Parse Data**: BeautifulSoup parses the HTML content to extract movie titles.
5. **Show Suggestions**: The top movie titles are displayed in a message box.

### Search Movies

1. **Input Movie Name**: When you click the "Search Movie" button, a dialog box prompts you to enter the movie name.
2. **Fetch Data**: The application constructs a search URL using the entered movie name and fetches data from IMDb.
3. **Parse Data**: BeautifulSoup parses the HTML content to extract movie titles.
4. **Show Results**: The search results are displayed in a message box.

### Get Cast and Crew

1. **Input Movie Name**: When you click the "Get Cast and Crew" button, a dialog box prompts you to enter the movie name.
2. **Fetch Data**: The application constructs a search URL using the entered movie name and fetches data from IMDb.
3. **Parse Data**: BeautifulSoup parses the HTML content to find the movie link and then fetches the cast and crew data.
4. **Show Cast and Crew**: The top cast and crew members are displayed in a message box.

### Toggle Theme

1. **Switch Modes**: Clicking the "Toggle Theme" button switches between light and dark modes.
2. **Update UI**: The background and text colors of the application are updated accordingly.

### Full-Screen Mode

1. **Enable Full-Screen**: Press `F11` to toggle full-screen mode.
2. **Adjust UI**: The font size of the widgets is increased for better visibility in full-screen mode.
3. **Exit Full-Screen**: Press `Escape` to exit full-screen mode.

## Screenshots

!Light Mode
!Dark Mode
!Full-Screen Mode

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements

- IMDb for providing movie data.
- BeautifulSoup for web scraping.
- Requests for handling HTTP requests.

## Contact

For any questions or suggestions, feel free to reach out to your-email@example.com.

---

Happy coding! 😊
