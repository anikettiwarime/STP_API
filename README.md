# Student Teacher Portal - E-learning Website

Welcome to the Student Teacher Portal, an E-learning website designed to facilitate online education during the pandemic. This project was developed using HTML, CSS, and JavaScript for the frontend, with Django powering the backend. Below, you'll find a comprehensive guide on setting up and using the platform.

To view the live demo, click [here](https://stp.anikettiwari.tech/api/).
Note: This is a demo version of the website, and some features may not be available.

## Project Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/anikettiwarime/STP_API.git
   ```

2. **Navigate to the Project Directory:**

   ```bash
   cd STP_API
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations:**

   ```bash
   python manage.py migrate
   ```

5. **Create Superuser (Admin):**

   ```bash
   python manage.py createsuperuser
   ```

6. **Start the Development Server:**

   ```bash
   python manage.py runserver
   ```

7. **Access the Admin Panel:**
   Open your browser and go to [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) to log in as the admin.

8. **Access the Student Teacher Portal:**
   Open your browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to explore the E-learning platform.

## Features

### Authentication

- **Admins:** Full access to the system.
- **Teachers:** Can post lectures and manage subjects and classrooms.
- **Students:** Can download/watch online lectures.

### Management Features

- **Classroom and Subjects Management:** Organize classes and subjects efficiently.
- **Event Announcements:** Keep users informed about upcoming events.
- **Video Lectures Engagement and Feedback:** Enable students to engage with video lectures and provide valuable feedback.
- **Time Table Feature:** Easily manage and view class schedules.

## Contributing

If you'd like to contribute to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature: `git checkout -b feature-name`
3. Commit your changes: `git commit -m 'Add new feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request.

## Support

If you encounter any issues or have questions, please feel free to [open an issue](https://github.com/anikettiwarime/STP_API.git/issues).

Thank you for contributing to the Student Teacher Portal project! Happy learning!
