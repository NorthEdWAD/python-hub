This project is designed to give students a quick, hands-on introduction to version control using GitHub Desktop. By the end of this activity, students will have a live repository containing their first web files.

---

**Project Overview:** In this activity, students will learn the fundamental workflow of Git and GitHub by creating a local project and publishing it to the cloud. They will use GitHub Desktop to manage their files, commit changes, and push their work to a remote repository.

**Learning Objectives:**
* Students will be able to create a local project folder and initialize it as a GitHub repository.
* Students will be able to author basic HTML and CSS files to serve as project assets.
* Students will be able to perform "Commit" and "Push" operations to sync local changes with GitHub.
* Students will be able to verify their uploaded content on the GitHub web interface.

**Skill Level:** Beginner

**Estimated Time:** Project will take 1 class session (approx. 30 minutes) to complete

**Technical Requirements:**
* **Required HTML elements:** `<!DOCTYPE html>`, `<html>`, `<head>`, `<title>`, `<body>`, `<h1>`, `<p>`
* **Required CSS properties:** `background-color`, `color`, `text-align` 
* **Software:** GitHub Desktop, a code editor (e.g., VS Code), and a GitHub account.

---

### **Step-by-Step Instructions:**

1.  **Set up your local folder:** Create a new folder on your computer named `github-practice`.
2.  **Initialize the Repository:** Open GitHub Desktop. Select "File" > "Add Local Repository" (or "Create New Repository") and point it to your `github-practice` folder.
3.  **Create your HTML file:** Inside your folder, create a file named `index.html`. Add a basic HTML5 structure with a heading that says "My GitHub Test".
4.  **Create your CSS file:** Create a file named `style.css`. Add a rule to change the `background-color` of the body to any color you like.
    > **Check your work:** Open `index.html` in a browser. Does your background color appear? Is your heading visible? 
5.  **Link the files:** In the `<head>` of your `index.html`, add the `<link>` tag to connect your `style.css`.
6.  **View changes in GitHub Desktop:** Open the GitHub Desktop app. You should see your new files listed in the "Changes" tab on the left.
7.  **Craft your first commit:** In the "Summary" box at the bottom left, type "Initial commit." Click the blue **Commit to main** button.
8.  **Publish to GitHub:** Click the **Publish repository** button at the top. Ensure "Keep this code private" is unchecked if you want others to see it, then click **Publish**.
    > **Check your work:** Log into GitHub.com in your browser. Look at your profile—do you see the `github-practice` repository listed? 
9.  **Make a change:** Go back to `style.css` and change the text color of your `<h1>`. Save the file.
10. **Push the update:** Return to GitHub Desktop. You will see the change. Enter a summary like "Updated heading color," click **Commit**, and then click **Push origin**.

---

**Submission Requirements:** * Ensure your `github-practice` folder contains both `index.html` and `style.css`.
* Upload/Sync all project files to your GitHub repository.
* Provide the URL of your GitHub repository to your instructor.

**Assessment:** Your project will be evaluated on the successful creation of the GitHub repository, the correct syntax of your HTML/CSS files, and the presence of at least two distinct commits in your GitHub history.
