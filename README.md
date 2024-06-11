# InspiredReads
The InspiredReads is a web application designed to provide personalized book recommendations based on user-selected genres. Utilizing the Google Books API, the platform allows users to explore a wide range of books, offering a tailored reading experience that caters to individual preferences. This project leverages Django, a high-level Python web framework, to manage user authentication, genre selection, and book fetching functionalities.

Key Features

1.User Authentication
-Secure user registration and login system.
-Password hashing and session management.
2.Genre Selection
-Users can select their favorite genres from a predefined list.
-Genre preferences are stored and associated with individual user accounts.
3.Personalized Book Recommendations
-Fetches books from the Google Books API based on selected genres.
-Displays a curated list of books, including titles, authors, and other relevant details.
-Interactive Book Fetching
-Users can dynamically fetch books by selecting genres from a dropdown menu.
-Results are displayed in real-time without requiring a page reload.
4.Writing and Editing
InspiredReads allows writing of novels and editing of the same which alows user to be part of the writing community.
4.Responsive Design
-The application is designed to be responsive and user-friendly, ensuring a seamless experience across various devices and screen sizes.

Technical Overview
1.Backend
-Framework: Django
2.Database: SQLite (default Django database for development purposes)
3.APIs: Integration with Google Books API for fetching book data.
4.Logging: Comprehensive logging for debugging and monitoring.
5.Frontend
-HTML/CSS: Structured and styled templates.
-JavaScript: Dynamic content loading and API interaction using Fetch API.
6.Security
-CSRF Protection: Ensures secure forms and API interactions.
-User Authentication: Secure handling of user credentials and sessions.
