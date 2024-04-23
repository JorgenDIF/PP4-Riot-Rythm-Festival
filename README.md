
# Riot Rythm Festival 2024

![alt text](assets/images/riotlogo.png)

Welcome to the Riot Rythm Festival 2024! Here, you'll experience the pinnacle of musical freedom and create memories that last a lifetime.

## Table of Contents
- [Introduction](#introduction)
- [Agile Methodology](#agile-methodology)
- [User Experience (UX)](#user-experience-ux)
  - [The Strategy](#the-strategy)
  - [The Scope](#the-scope)
  - [The Structure](#the-structure)
  - [The Skeleton](#the-skeleton)
  - [The Surface](#the-surface)
- [Am I Responsive](#am-i-responsive)
- [Project Overview](#project-overview)
  - [Learning Objectives](#learning-objectives)
  - [Assignment Requirements](#assignment-requirements)
  - [Self-Assessment](#self-assessment)
- [Features](#features)
- [Technologies](#technologies)
  - [Language](#language)
  - [Tools](#tools)
  - [Frameworks & Libraries](#frameworks--libraries)
  - [Design](#design)
- [Data Modeling and Database Design](#data-modeling-and-database-design)
  - [ERD](#erd)
  - [API Integration](#api-integration)
- [Testing](#testing)
  - [Bugs](#bugs)
- [Setup and Deployment](#setup-and-deployment)
  - [Create Repository](#create-repository)
  - [Initialize in VS Code](#initialize-in-vs-code)
  - [Set Up Virtual Environments](#set-up-virtual-environments)
  - [Create Django Project](#create-django-project)
  - [Deployment to Github](#deployment-to-github)
  - [Deployment to Heroku](#deployment-to-heroku)
  - [Local Deployment](#local-deployment)
- [Credits](#credits)
  - [Content](#content)
  - [Images](#images)
  - [Thank You](#thank-you)

## <a id="introduction">Introduction</a>
Welcome to this freedom of music. This is where you will have your best time in 2024.

## <a id="agile-methodology">Agile Methodology</a>
This project is managed using Agile principles tailored for a solo developer, focusing on iterative development and continuous improvement. I utilize a flexible approach to project management that allows for adapting to changes and refining features based on ongoing evaluation and feedback. To help manage tasks and progress, I employ a Kanban board. The link to the board can be found [Here](https://github.com/users/JorgenDIF/projects/4). It provides a visual overview of ongoing, upcoming, and completed work, ensuring that I stay organized and focused on the most critical tasks at hand. This personal agility ensures that the development process remains aligned with the evolving project goals and my learning objectives.

## <a id="user-experience-ux">User Experience (UX)</a>
### <a id="the-strategy">The Strategy</a>
- The core objective is to develop a festival site that is an engaging community hub where users can influence the lineup selection. It will be a fusion of interaction and collaboration, with the following key features:

Included:
1. **User Suggestions via Email:** Users can send direct suggestions for the festival lineup, fostering a sense of personal contribution.
2. **Band Selection from a Bank:** Users choose their preferred bands from a curated list, submitting motivations for their choices, which adds depth to their involvement.
3. **Community Endorsement:** Users can 'like' or support others' band suggestions, creating an interactive and communal decision-making process.
4. **User-Influenced Lineup:** The site will be streamlined to ensure ease of use, aiming to create an exciting and user-influenced festival experience, where the popularity and engagement around bands will guide the organizers in curating the final lineup.

### <a id="the-scope">The Scope</a>
- The project will be a user-centric platform for influencing a festival lineup with the following features:

Included:
1. **User Account Creation:** Allows users to register and engage with band suggestions.
2. **Band Suggestion Submission:** Offers a way for users to propose bands via an online interface or email.
3. **Band Selection:** Lets users pick from a pre-listed selection of bands, providing reasons for their choices.
4. **Likes for Band Suggestions:** Users can show support for other users' band suggestions.
5. **Admin Panel:** Enables administrators to manage band suggestions and user interactions.

Excluded:
- Detailed user analytics, real-time updates, and direct messaging functionalities will not be included in the initial version to maintain simplicity and focus on the core features.


### <a id="the-structure">The Structure</a>
- The project's structure will be organized to facilitate easy navigation and interaction, ensuring that users can quickly understand and engage with the site's functionality.

Main Sections:
1. **Home Page**: Introduces the concept and navigates to main features.
2. **Registration/Login**: For user account creation and access.
3. **Suggestion Form**: Where users can submit their band suggestions.
4. **Band List**: Displays available bands for selection and user submissions.
5. **Like Mechanism**: Associated with each band suggestion for community endorsement.
6. **Admin Dashboard**: Accessible by site administrators for content management and oversight.

Connections:
- The Home Page links to both the Registration/Login section for new users and the Band List for returning visitors.
- The Suggestion Form is directly connected to the Band List, allowing users to view and select from existing options or add new ones.
- Likes for suggestions are immediately reflected on the Band List to showcase popularity.
- The Admin Dashboard has controls to manage the Band List and review submissions from the Suggestion Form.

This logical flow ensures users can seamlessly move from signing up, making suggestions, browsing bands, and interacting with the community's choices.

### <a id="the-skeleton">The Skeleton</a>
The skeleton of the project lays out the wireframes and basic layouts that dictate the user interface's organization and visual flow, including specific areas for general information and administrative functions.

Key Layouts:
1. **Home Page Layout:** Provides a welcoming introduction to the festival concept with direct navigation to other sections.
2. **User Registration/Login Layout:** Features streamlined forms for easy user onboarding or access.
3. **Band Suggestion Layout:** Offers a simple form for users to suggest bands, designed to engage users effectively.
4. **Band List Layout:** Displays suggested and selectable bands with 'like' buttons and motivation texts.
5. **Admin Dashboard Layout:** A functional interface for content management, including user activity and band suggestions.
6. **Information Page Layout:** Delivers detailed information about the festival, guidelines for participation, and general FAQs.
7. **Add Band Layout (Admin Only):** An admin-exclusive layout to input new bands into the system, featuring necessary fields such as band name, genre, and image uploads.

Wireframes Placeholder:
- [Insert Home Page Wireframe]
- [Insert Registration/Login Wireframe]
- [Insert Band Suggestion Wireframe]
- [Insert Band List Wireframe]
- [Insert Admin Dashboard Wireframe]
- [Insert Information Page Wireframe]
- [Insert Add Band Wireframe] (Admin Only)

These layouts and placeholders will guide the development of the user interface. The wireframes, once created and inserted, will illustrate how each page is structured to facilitate user interactions and administrative tasks, ensuring a seamless experience across the platform.

### <a id="the-surface">The Surface</a>
The surface level of the project focuses on the aesthetic and sensory aspects, detailing the design choices including typography, color schemes, and visual elements that enhance the user experience and brand identity of the festival site.

1. **Typography:**
  - Primary Typeface: A modern sans-serif font for headings and user interface elements to convey clarity and accessibility.
  - Secondary Typeface: A contrasting serif font for body text to add a touch of elegance and improve readability.

2. **Color Scheme:**
  - Primary Colors: A vibrant palette that includes electric blue and bright magenta, reflecting the dynamic and energetic nature of a music festival.
  - Secondary Colors: Neutral shades like light gray and off-white to provide balance and ensure content readability.
  - Accent Color: Neon green for calls to action and interactive elements, which stands out against both primary and secondary colors.

3. **Visual Elements:**
  - Icons: Use of bold and thematic icons to direct users and enhance navigation.
  - Images: High-quality images of bands and crowds, giving a real-life feel of the festival atmosphere.
  - Animations: Subtle animations for user interactions like button clicks and transitions to keep the interface lively and engaging.

4. **Layout:**
  - Consistency: Uniform layouts across pages to ensure a seamless user experience.
  - Spacing: Ample spacing between elements to create a clean and organized appearance.
  - Responsive Design: Ensuring the website is fully responsive for optimal viewing on various devices and screen sizes.

5. **User Interface Components:**
  - Buttons: Styled with rounded corners and shadows to provide a tactile feel.
  - Forms: Designed for ease of use with clear labeling and spacious input fields.
  - Menus: Dropdown and hamburger menus for a compact and accessible navigation structure.

These design elements are chosen to create a welcoming and interactive online environment that reflects the festival's vibrant community and provides an engaging user experience. The combination of visual appeal and functional design will make the site not only a tool for interaction but also a pleasing space to explore.

## <a id="am-i-responsive">Am I Responsive</a>
Discussion on the website's responsiveness and its adaptation to various devices.

## <a id="project-overview">Project Overview</a>
### <a id="learning-objectives">Learning Objectives</a>
What the project aims to achieve in terms of learning and development
1. **Mastery of Django:** Gain deep understanding and hands-on experience with Django, focusing on its ORM, views, templates, and forms.
2. **Proficiency in Bootstrap:** Learn to implement responsive web designs that automatically adjust for different device screens.
3. **Full Stack Development:** Develop front-end and back-end skills to create a comprehensive web application.
4. **Kanban Board Implementation:** Utilize Kanban methodology for effective project management and task tracking.
5. **Project Management and Version Control:** Manage software development using Git for version control, enhancing collaboration and project tracking abilities.
6. **Testing and User Feedback:** Engage in thorough testing practices and gather user feedback to refine the application.

### <a id="assignment-requirements">Assignment Requirements</a>
A detailed list of project requirements as outlined by the educational curriculum:
1. Functionality: Create a fully functional web application where users can suggest, select, and like bands.
2. User Authentication: Implement secure user registration and login capabilities.
3. Database Management: Design and utilize a database to store user data and band information.
4. Responsive Design: Ensure the website is responsive and accessible on all devices.
5. User Interface: Develop a clean and intuitive user interface using Bootstrap.
6. Project Documentation: Maintain comprehensive documentation of the development process and code.
7. Version Control: Use Git to manage the project repository, with consistent commits and clear commit messages.
8. Kanban Board: Set up and maintain a Kanban board for task management throughout the project duration.

### <a id="self-assessment">Self-Assessment</a>

**Learning Reflection:**
I've grown to really appreciate Django for its robustness and Bootstrap for its utility in responsive design, despite the initial challenges of mastering these technologies.

**Highlights:**
Integrating Django's extensive pre-built functionalities with Bootstrap's front-end tools has been the highlight, allowing me to focus on both efficiency and detail.

**Challenges:**
The complexity of Django's features and Bootstrap's layout systems were initially daunting but became manageable with persistence and practice.

**Achievements:**
Successfully developing a full-stack application that is both functional and user-friendly stands out as a major achievement.

**Areas for Improvement:**
There's always room to enhance my skills. With more experience, I aim to improve my backend optimization and front-end customization abilities.




## <a id="features">Features</a>
A detailed list of features that enhance user interactions.

## <a id="technologies">Technologies</a>
### <a id="language">Language</a>
The programming languages employed in the project.

### <a id="tools">Tools</a>
The development tools and software used to build and maintain the project.

### <a id="frameworks--libraries">Frameworks & Libraries</a>
Details on the frameworks and libraries integrated into the project.

### <a id="design">Design</a>
Discussion of the design principles and aesthetics adopted in the project.

## <a id="data-modeling-and-database-design">Data Modeling and Database Design</a>
### <a id="erd">ERD</a>
Entity Relationship Diagram showing the database schema.

### <a id="api-integration">API Integration</a>
Details of any APIs integrated into the project.

## <a id="testing">Testing</a>
### <a id="bugs">Bugs</a>
Documentation of known bugs and their status.

## <a id="setup-and-deployment">Setup and Deployment</a>
### <a id="create-repository">Create Repository</a>
Steps to create a new repository, highlighting best practices.

### <a id="initialize-in-vs-code">Initialize in VS Code</a>
Instructions for setting up the project in Visual Studio Code.

### <a id="set-up-virtual-environments">Set Up Virtual Environments</a>
How to create and manage virtual environments.

### <a id="create-django-project">Create Django Project</a>
Detailed steps on initializing a new Django project.

### <a id="deployment-to-github">Deployment to Github</a>
Step-by-step guide on pushing the project to GitHub.

### <a id="deployment-to-heroku">Deployment to Heroku</a>
Detailed procedure for deploying the project on Heroku.

### <a id="local-deployment">Local Deployment</a>
Guidelines for deploying the project locally.

## <a id="credits">Credits</a>
### <a id="content">Content</a>
Credits for textual and multimedia content used throughout the project.

### <a id="images">Images</a>
Credits for images used in the project, including sources and copyrights.

### <a id="thank-you">Thank You</a>
A thank note to everyone who contributed, supported, or guided the project.
