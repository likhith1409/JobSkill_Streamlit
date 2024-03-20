import streamlit as st
import csv

# CSV reading function
def read_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        data = {row['Job Title']: [row[f'Skill {i+1}'] for i in range(13)] for row in reader}
    return data

# Function to find matching job titles
def find_matching_job_titles(user_skills, data):
    matching_job_titles = set()

    for job_title, skills in data.items():
        matching_count = sum(skill in user_skills for skill in skills)
        if matching_count > 0 and job_title not in matching_job_titles:
            matching_job_titles.add(job_title)

    return matching_job_titles

def main():
    st.set_page_config(page_title="JobSkills: Uncover Your Potential", page_icon=":briefcase:")

    # Title and description
    st.title("JobSkills: Uncover Your Potential")
    st.write("""
        Welcome to JobSkills, your personalized career exploration platform. We understand that your unique skills define your professional journey. With JobSkills, embark on a transformative experience where you can seamlessly discover job titles perfectly aligned with your expertise. Our intuitive platform empowers you to navigate through a curated list of opportunities tailored to your skills, ensuring that your career path is not just a choice but a reflection of your true capabilities. Explore, discover, and shape your professional future with JobSkills – where your skills meet their ideal job titles.
    """)
    st.markdown("---")

    # Navbar
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "About"])

    if page == "Home":
        # Input bar for skills
        user_input_skills = st.text_input("Enter your skills (comma-separated) and small letters like(python,java):")
        skills = user_input_skills.strip().split(',')[:7]

        # Load CSV data
        file_path = 'jobdetails.csv'
        data = read_csv(file_path)

        # Submit button
        if st.button("Submit"):
            # Find matching job titles
            matching_job_titles = find_matching_job_titles(skills, data)

            # Display results
            st.subheader("Matching Job Titles:")
            if matching_job_titles:
                for title in matching_job_titles:
                    st.write(title)
            else:
                st.write("No matching job titles found.")

    elif page == "About":
        # About Us section
        st.title("About Us")
        st.write("""
            Welcome to JobSkills, where we revolutionize the way you connect your skills with the perfect job titles. Our mission is to simplify the job search process by providing a seamless platform for individuals to showcase their skills and expertise. At JobSkills, we understand that finding the right job can be a challenging journey, and we are here to make it easier for you. Our innovative approach allows you to effortlessly add the skills you possess, enabling our advanced system to match you with the most relevant job titles in real-time. Say goodbye to tedious searches and welcome a more streamlined and efficient way to navigate your skills towards the career path you desire. Join us in shaping the future of employment connections and let your skills pave the way to success.
        """)

        # Image
        st.image("images/logo.png", caption="JobSkills Logo")

if __name__ == '__main__':
    main()

